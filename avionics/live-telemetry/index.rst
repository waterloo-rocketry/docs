Live Telemetry
==============

.. note::

   MCU: PIC18F26K83 | RF Transceiver: TI CC1200 + GRF5509 PA

Overview
--------

The LTT firmware runs on the RF telemetry board carried on the rocket and on
the ground stations. It relays every RocketCAN message it sees outward over
a sub-GHz RF link, and injects any messages it receives over RF back onto the
local CAN bus. This gives mission control a redundant, wireless path to send
commands (e.g. arming, actuator control) and receive telemetry while the
rocket is railed or in flight, independent of the umbilical/CAN connection.

The same firmware image runs on three instance types, distinguished at build
time by ``BOARD_INST_UNIQUE_ID``:

- **ROCKET** -- lives on the rocket, acts as the network master
- **TELEMETRY_GROUND_1 / TELEMETRY_GROUND_2** -- ground station radios

The ROCKET instance is the timing master: it round-robins the RF airtime
between the ground instances so that only one radio transmits at a time (see
`RF Link / State Machine`_).

Reference Documents
~~~~~~~~~~~~~~~~~~~~

- `PIC18F26K83 (MCU) Datasheet <https://ww1.microchip.com/downloads/en/DeviceDoc/40001943A.pdf>`_
- `CC1200 (RF Transceiver) Datasheet <https://www.ti.com/lit/gpn/cc1200>`_
- `CC1200 User's Guide <https://www.ti.com/lit/ug/swru346b/swru346b.pdf>`_
- `SmartRF Studio <https://www.ti.com/tool/SMARTRFTM-STUDIO>`_ -- used to generate the register table in ``cc1200.c``
- `GRF5509 (External PA) Datasheet <https://www.guerrilla-rf.com/products/detail/sku/GRF5509>`_

Initialization
--------------

``board_Init()`` runs the following sequence before entering the main loop:

1. ``timer0_init()`` -- start Timer0, which drives the ``millis()`` timebase (fires roughly every 500 us)
2. ``LED_Init()`` -- configure Red/Green/Blue status LED pins
3. ``OSC_Init()`` -- switch to the external HS oscillator, wait for ``ORDY``
4. ``ADC_Init()`` -- configure the ADC with the Fixed Voltage Reference (FVR, 2.048 V) and hardware low-pass filter, start continuous conversion on the current-sense input
5. ``SPI_Init()`` -- configure the SPI peripheral used to talk to the CC1200
6. ``CAN_Init()`` -- configure CAN TX/RX pins via PPS, compute bit timing from ``_XTAL_FREQ``, initialize the canlib TX/RX buffer pools
7. ``CC1200_Init()`` -- pulse the CC1200 ``RESET_n`` pin, configure the PA-enable pins as open-drain outputs, configure TMR3 to count received packets off the CC1200 ``PKT_CRC_OK`` GPIO, then write the full SmartRF-generated register table
8. ``SM_Init()`` -- set the top-level state machine to ``LTT_STATE_INIT``

The first pass through ``LTT_STATE_INIT`` (once the CC1200 confirms it has
reached ``IDLE``) additionally:

- Loads the persisted operating **frequency** and **TX power** from EEPROM
  (``eeprom_get_frequency()`` / ``eeprom_get_power()``) and applies them to
  the CC1200
- Enables antenna diversity on ground instances only
  (``CC1200_Set_Ant_Diversity(!channel_is_rocket())``)
- Reports the active frequency/power back onto CAN via ``CONFIG_STATUS`` messages
- Transitions to ``LTT_STATE_TX`` on the ROCKET instance, or ``LTT_STATE_RX``
  on ground instances

Runtime
-------

Heart Beat
~~~~~~~~~~

The Blue LED toggles once per periodic CAN status report (see
`Health Check`_), i.e. approximately every 500 ms, as a liveness indicator.

The Green and Red LEDs are used as RF activity indicators rather than a
fixed-period heartbeat:

- **Green** -- lit while this instance is transmitting (``LTT_STATE_TX``)
- **Red** -- lit while a message received over RF is being forwarded onto
  the local CAN bus

Health Check
~~~~~~~~~~~~

- Firmware samples the 12 V rail current every main-loop iteration through
  a 16 mOhm shunt and continuously filters it in software. The filtered
  value is reported every 500 ms via ``SENSOR_ANALOG.SENSOR_12V_CURR``. If
  the reading is at or above the overcurrent threshold (200, in the ADC's
  scaled mA units), the firmware sets the ``E_12V_OVER_CURRENT`` bit in
  ``GENERAL_BOARD_STATUS`` for that report period.
- Firmware tracks RF link quality per remote instance: **RSSI** and **LQI**
  are accumulated for every packet received during an RX period and
  exponentially averaged when that period ends. If no packet
  has been received from a given remote within the last 3 seconds, that
  remote's RSSI/LQI is reported as "no signal" (RSSI = -128, LQI = 0)
  rather than a stale value. This is reported every 500 ms via
  ``TELEMETRY_INFO``, one message per known remote channel.

RF Link / State Machine
~~~~~~~~~~~~~~~~~~~~~~~~

LTT communication is managed by two nested finite state machines.

**Top-level FSM** (``SM_LTT_State_Machine``) decides when this instance
should transmit vs. receive:

- ``INIT`` -- apply persisted RF configuration (frequency, power, antenna
  diversity), then move to ``TX`` (ROCKET) or ``RX`` (ground)
- ``TX`` -- pop queued CAN messages and transmit them over RF; if no
  message has been sent for 50 ms (``TX_TIMEOUT_MS``), or the state has
  been active for 200 ms total (``TX_TIME_MAX_MS``), move to ``TX_END``
- ``TX_END`` -- transmit a 1-byte end-of-transmission (EOT) frame naming
  the next instance that should transmit, then move to ``RX`` (or back to
  ``INIT`` if a configuration reload was requested)
- ``RX`` -- listen for packets; on ROCKET, if 60 ms (``RX_TIMEOUT_MS``)
  pass with nothing received, transmit anyway to guarantee telemetry keeps
  flowing even if ground receivers are too weak to reply. Non-ROCKET
  instances instead wait for an EOT frame addressed to their own instance
  ID before moving to ``TX``. Any other RF packet received while in ``RX``
  is pushed onto the local CAN TX queue and forwarded onto the bus.

The ROCKET instance is the only one that hands out transmit turns: it
addresses its EOT frame to the next ground instance in round-robin order, so
only one radio should ever be transmitting at a given moment. Ground instances
only ever address their EOT frames back to ROCKET.

**Low-level FSM** (``CC1200_State_Transition``) drives the CC1200's own
RX/TX FIFOs based on chip status read via ``SNOP``:

- ``RX`` -- decode any buffered packet, then fall through to ``IDLE`` handling
- ``IDLE`` -- if the top FSM wants to ``TX``, pop a queued CAN message and
  write it to the TX FIFO (``STX``); if the top FSM wants ``RX``, issue ``SRX``
- ``RX_FIFO_ERROR`` / ``TX_FIFO_ERROR`` -- flush the offending FIFO
  (``SFRX`` / ``SFTX``)

Received-packet counting is done in hardware: ``TMR3`` increments on every
``PKT_CRC_OK`` pulse from the CC1200, and the firmware compares that counter
against its own bookkeeping to know whether unread packets are waiting in
the RX FIFO, so a corrupted/dropped packet cannot desynchronize the two.

Frequency, Power, and Antenna Diversity Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Operating frequency and TX power are stored in EEPROM so they survive
  reset/power-cycle, and are only re-applied to the CC1200 when the board
  (re-)enters ``LTT_STATE_INIT``.
- Both values can be changed remotely over CAN with ``CONFIG_SET`` (see
  `CAN Communication`_); a successful write triggers
  ``SM_LTT_Reload_Config()``, which causes the current TX/RX cycle to
  finish normally before the FSM returns to ``INIT`` and re-applies
  configuration -- it does not interrupt an in-progress transmission.
- Antenna diversity is enabled only on ground instances, since the ground
  stations are the ones equipped with the second, SRAD antenna path.
- The Telemetry actuator command (``ACTUATOR_TELEMETRY``) can additionally:

  - **On ROCKET:** turn the PA on/off (``SM_LTT_Stop_TX``), acting as a
    transmit inhibit independent of frequency/power configuration
  - **On ground instances:** queue a one-shot telemetry "wake" packet
    (``SM_LTT_Wake_Remote``) that is transmitted the next time the RX
    timeout for that instance elapses without hearing from ROCKET -- used
    to solicit a response from a rocket-side radio that has otherwise gone
    quiet

CAN Communication
------------------

CAN Message Sent by Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: CAN Message Sent by Firmware
   :header-rows: 1

   * - Message Type
     - Description
     - Period
   * - ``SENSOR_ANALOG.SENSOR_12V_CURR``
     - Report filtered 12 V rail current
     - 500 ms
   * - ``GENERAL_BOARD_STATUS``
     - Report board error bitfield (e.g. overcurrent)
     - 500 ms
   * - ``TELEMETRY_INFO``
     - Report RSSI/LQI for one remote instance (one message per remote)
     - 500 ms per remote
   * - ``CONFIG_STATUS`` (``CAN_CONFIG_ID_FREQ``)
     - Report the currently-active RF frequency (offset from 900 MHz)
     - On entry to ``LTT_STATE_INIT``
   * - ``CONFIG_STATUS`` (``CAN_CONFIG_ID_POWER``)
     - Report the currently-active TX power (offset by +100)
     - On entry to ``LTT_STATE_INIT``
   * - *(any CAN message queued locally)*
     - Forwarded out over the RF link to the paired instance(s)
     - Best-effort, RF airtime permitting

CAN Message Handled by Firmware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: CAN Message Handled by Firmware
   :header-rows: 1

   * - Message Type
     - Description
   * - ``LEDS_ON``
     - Force all three status LEDs on (debug aid)
   * - ``LEDS_OFF``
     - Force all three status LEDs off (debug aid)
   * - ``ACTUATOR_CMD`` (actuator = ``ACTUATOR_TELEMETRY``)
     - ``ON``: enable TX on ROCKET, or queue a wake packet on ground
       instances. ``OFF``: disable TX (PA off) on ROCKET
   * - ``CONFIG_SET`` (config id = 0 ``CAN_CONFIG_ID_FREQ``)
     - Set persistent operating frequency (value is an offset from 900 MHz,
       in kHz) and request a config reload
   * - ``CONFIG_SET`` (config id = 1 ``CAN_CONFIG_ID_POWER``)
     - Set persistent TX power (value is offset by +100 to allow negative
       dBm) and request a config reload
   * - ``RESET_CMD``
     - Reset the board if targeted (``check_board_need_reset`` in canlib)
   * - *(any other CAN message)*
     - Queued for transmission out over the RF link

``CONFIG_SET`` is only actioned if it targets ``BOARD_TYPE_ID_TELEMETRY``
and either this instance's specific ID or ``BOARD_INST_ID_ANY``.

GENERAL_BOARD_STATUS board specific error field usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table:: GENERAL_BOARD_STATUS board_error_bitfield Bit definition
   :header-rows: 1

   * - Bitfield Name
     - Description
     - Offset
   * - ``E_12V_OVER_CURRENT``
     - 12 V rail current at or above the overcurrent threshold
     - 3
