*******************************************************
Injector Sensor Hub Firmware Design Specification [WIP]
*******************************************************

Overview
========

Injector Sensor Hub firmware periodically reads analog sensors and reports analog data to CAN, analog sensors include pressure transducers and hall effect sensors.

Reference Documents
-------------------

* `PIC18F26K83(MCU) Datasheet <https://ww1.microchip.com/downloads/en/DeviceDoc/40001943A.pdf>`_
* `IFM PT5402(Pressure Transducer) Datasheet <https://www.ifm.com/ca/en/product/PT5402#documents>`_

TODO add documentation for OX Hall and Fuel Hall sensors?

Initialization
==============

#. Setup to use external oscillator with 4xPLL
#. Setup PPS(Peripheral Pin Select) for CAN
#. Initialize ADC, setup to use FVR(Fixed Voltage Reference)
#. Initialize CAN module with canlib

Runtime
=======

Heart Beat
----------

Red LED shall toggle every 500ms.

Health Check
------------

TODO add 5V and 12V current check

TODO to we add current/voltage error checks for sensors?

TODO add 4-20mA pressure transducer current check, either here or in Sensor Reading

* Firmware shall check 12V input voltage every 500ms, and report voltage with ``SENSOR_ANALOG.SENSOR_12V_VOLT`` CAN message, if the voltage is below 11.5V or above 12.7V, the firmware shall signal error with ``GENERAL_BOARD_STATUS`` CAN message.

Sensor Reading
--------------

TODO add sensor reading for each sensor + brief methodology

* Firmware shall read Oxidizer pressure transducer every 50 ms, ADC voltage reading shall be convert to pressure use formula described in `Convert pressure transducer ADC pin voltage input to pressure`_ section, when the pressure output be send to can use ``SENSOR_ANALOG.PRESSURE_OX`` CAN message.

CAN Communication
=================

CAN Message Sent by Firmware
----------------------------

TODO add CAN message description for all sensor readings sent
TODO add CAN message for health check?

.. list-table:: CAN Message Sent by Firmware
   :widths: 25 65 10
   :header-rows: 1

   * - Message Type
     - Description
     - Period
   * - SENSOR_ANALOG.PRESSURE_OX
     - Report oxidizer tank pressure
     - 10ms

CAN Message Handled by Firmware
-------------------------------

TODO add handles board reset command and maybe also LED flash thing?

.. list-table:: CAN Message Handled by Firmware
   :widths: 25 75
   :header-rows: 1

   * - Message Type
     - Description
   * - RESET_CMD
     - Reset board if targeted(check with ``check_board_need_reset`` function in canlib)

GENERAL_BOARD_STATUS board specific error field usage
-----------------------------------------------------

.. list-table:: GENERAL_BOARD_STATUS board_error_bitfield Bit definition
   :widths: 25 60 15
   :header-rows: 1

   * - Bitfield Name
     - Description
     - Offset
   * - PT_OUT_OF_RANGE
     - 4-20 mA Pressure transducer signals less that 4mA or more than 20mA
     - 0

Mathematics Model
=================

TODO add ADC calculations including Vref and resolution for the sensors
TODO anything else that sensors are doing that I'm not aware of

Describe common used math equations in the firmware, if the equation is more than one line, then a link to a Matlab model should be provided.

Convert pressure transducer ADC pin voltage input to pressure
-------------------------------------------------------------

Insert formula here
