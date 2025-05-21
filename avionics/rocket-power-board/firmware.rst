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

Red LED shall toggle every 500ms.

Health Check
------------

Describe what health check need to be performed, example:

* Firmware shall check 12V input voltage every 500ms, and report voltage with ``SENSOR_ANALOG.SENSOR_12V_VOLT`` CAN message, if the voltage is below 11.5V or above 12.7V, the firmware shall signal error with ``GENERAL_BOARD_STATUS`` CAN message.

Sensor Reading
--------------

Describe what sensor shall be read and report to CAN bus, example:

* Firmware shall read Oxidizer pressure transducer every 50 ms, ADC voltage reading shall be convert to pressure use formula described in section, when the pressure output be send to can use ``SENSOR_ANALOG.PRESSURE_OX`` CAN message.

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
     - When BOARD_INST_UNIQUE_ID == BOARD_UNIQUE_ID_ROCKET, Turn on/off 12V power output
   * - ACTUATOR_CMD.5V_RAIL_ROCKET
     - When BOARD_INST_UNIQUE_ID == BOARD_UNIQUE_ID_ROCKET, Turn on/off 5V power output

CAN Message handled in payload configuration only (BOARD_INST_UNIQUE_ID = BOARD_UNIQUE_ID_PAYLOAD)

.. list-table:: CAN Message handled in payload configuration only
   :widths: 25 75
   :header-rows: 1

   * - Message Type
     - Description
   * - ACTUATOR_CMD.12V_RAIL_PAYLOAD
     - When BOARD_INST_UNIQUE_ID == BOARD_UNIQUE_ID_PAYLOAD, Turn on/off 12V power output
   * - ACTUATOR_CMD.5V_RAIL_PAYLOAD
     - When BOARD_INST_UNIQUE_ID == BOARD_UNIQUE_ID_PAYLOAD, Turn on/off 5V power output

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
