************************************************
Rocket Power Board Firmware Design Specification
************************************************

Overview
========

Rocket Power Board firmware is responsible for report various voltage and current data to CAN bus, and turn on/off 12V and 5V rail based on CAN command.

Reference Documents
-------------------

* `PIC18F26K83(MCU) Datasheet <https://ww1.microchip.com/downloads/en/DeviceDoc/40001943A.pdf>`_
* `eFuse Datasheet <https://www.ti.com/lit/ds/symlink/tps25947.pdf>`_

Initialization
==============

#. Setup to use external oscillator
#. Setup PPS(Peripheral Pin Select) for all peripherals
#. Initialize ADC, setup to use FVR(Fixed Voltage Reference)
#. Initialize CAN module with canlib

Runtime
=======

Heart Beat
----------

Blue LED shall toggle every 500ms.

Power output control
--------------------

Refer to `CAN Message Handled by Firmware`_ section below. 5V output enable is controlled by ``5V_Fuse_RST/EN`` pin on the eFuse, when 5V output is enabled , the White LED shall light up. 12V output enable is controlled by ``12V_Fuse_RST/EN`` pin on the eFuse, when 12V output is enabled , the Red LED shall light up. Both 5V and 12V output shall be enabled at power-up.

Sensor Reading
--------------

Refer to `CAN Message Sent by Firmware`_ section below.

Health Check
------------

Health check shall be performed every 250 ms, immediately after sensor polling. All health check erros are signaled through ``GENERAL_BOARD_STATUS`` CAN Message. Note ``12V_EFUSE_FAULT`` and ``5V_EFUSE_FAULT`` are board specific error, refer to `GENERAL_BOARD_STATUS board specific error field usage`_ section below.

.. list-table:: Errors signaled by health check
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Condition
   * - 5V_OVER_CURRENT
     - I :sub:`5V_out` > TBD Value determined by experiment mA
   * - 5V_OVER_VOLTAGE
     - V :sub:`5V_out` > 5.2 V
   * - 5V_UNDER_VOLTAGE
     - V :sub:`5V_out` < 4.5 V
   * - 12V_OVER_CURRENT
     - I :sub:`12V_out` > TBD Value determined by experiment mA
   * - BATT_OVER_CURRENT
     - I :sub:`BATT` > TBD Value determined by experiment mA
   * - BATT_OVER_VOLTAGE
     - V :sub:`BATT` > 12.7 V
   * - BATT_UNDER_VOLTAGE
     - V :sub:`BATT` < 11.4 V
   * - 12V_EFUSE_FAULT
     - ``12V_Fuse_FLT`` = 0 (Fault signal is active Low)
   * - 5V_EFUSE_FAULT
     - ``5V_Fuse_FLT`` = 0 (Fault signal is active Low)

CAN Communication
=================

CAN Message Sent by Firmware
----------------------------

.. list-table:: CAN Message Sent by Firmware
   :widths: 25 65 10
   :header-rows: 1

   * - Message Type
     - Description
     - Period
   * - SENSOR_ANALOG.BATT_VOLT
     - LiPo voltage
     - 250 ms
   * - SENSOR_ANALOG.BATT_CURR
     - LiPo output current
     - 250 ms
   * - SENSOR_ANALOG.12V_CURR
     - 12V rail output current
     - 250 ms
   * - SENSOR_ANALOG.5V_VOLT
     - 5V rail voltage
     - 250 ms
   * - SENSOR_ANALOG.5V_CURR
     - 5V rail output current
     - 250 ms

CAN Message Handled by Firmware
-------------------------------

CAN Message handled in both rocket and payload configuration

.. list-table:: CAN Message handled in both rocket and payload configuration
   :widths: 25 75
   :header-rows: 1

   * - Message Type
     - Description
   * - RESET_CMD
     - Reset board if targeted(check with ``check_board_need_reset`` function in canlib)

CAN Message handled in rocket configuration only (BOARD_INST_UNIQUE_ID = BOARD_UNIQUE_ID_ROCKET)

.. list-table:: CAN Message handled in rocket configuration only
   :widths: 25 75
   :header-rows: 1

   * - Message Type
     - Description
   * - ACTUATOR_CMD.12V_RAIL_ROCKET
     - Turn on/off 12V power output through eFuse
   * - ACTUATOR_CMD.5V_RAIL_ROCKET
     - Turn on/off 5V power output through eFuse

CAN Message handled in payload configuration only (BOARD_INST_UNIQUE_ID = BOARD_UNIQUE_ID_PAYLOAD)

.. list-table:: CAN Message handled in payload configuration only
   :widths: 25 75
   :header-rows: 1

   * - Message Type
     - Description
   * - ACTUATOR_CMD.12V_RAIL_PAYLOAD
     - Turn on/off 12V power output through eFuse
   * - ACTUATOR_CMD.5V_RAIL_PAYLOAD
     - Turn on/off 5V power output through eFuse

GENERAL_BOARD_STATUS board specific error field usage
-----------------------------------------------------

.. list-table:: GENERAL_BOARD_STATUS board_error_bitfield Bit definition
   :widths: 25 60 15
   :header-rows: 1

   * - Bitfield Name
     - Description
     - Offset
   * - 12V_EFUSE_FAULT
     - 12V output eFuse Fault
     - 0
   * - 5V_EFUSE_FAULT
     - 5V output eFuse Fault
     - 1
