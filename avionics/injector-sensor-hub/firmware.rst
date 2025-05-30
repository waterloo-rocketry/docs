*************************************************
Injector Sensor Hub Firmware Design Specification
*************************************************

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

#. Setup to use external oscillator with 1xPLL
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

Health check shall be performed every 500 ms. All health check erros are signaled through ``GENERAL_BOARD_STATUS`` CAN Message. 

.. list-table:: Errors signaled by health check
   :widths: 25 75
   :header-rows: 1

   * - Name
     - Condition
   * - 5V_OVER_CURRENT
     - I :sub:`5V_out` > 100 mA
   * - 12V_OVER_CURRENT
     - I :sub:`12V_out` > 150 mA

Sensor Reading
--------------

Firmware shall read from the following sensors:

* Oxidizer Pressure Transducer
* Fuel Pressure Transducer
* CC #1 Pressure Transducer
* CC #2 Pressure Transducer
* Fuel Hall Sensor
* Oxidizer Hall Sensor

ADC voltage reading from PTs shall be converted to pressure using formula described in `Convert pressure transducer ADC pin voltage input to pressure`_ section. Pressure output is to be send to CAN using ``SENSOR_ANALOG`` CAN message. 

TODO add blurb about how Hall Sensor reading is handled.

TODO add 4-20mA pressure transducer current check.

Refer to `CAN Message Sent by Firmware`_ section below for period of transmission and sensor IDs or refer to ``analog_sensor_id`` enum definitions.

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
   * - GENERAL_BOARD_STATUS
     - Report status_ok healthcheck
     - 500 ms
   * - SENSOR_ANALOG.PRESSURE_OX
     - Report Oxidizer Pressure Transducer pressure
     - 50 ms
   * - SENSOR_ANALOG.PRESSURE_FUEL
     - Report Fuel Pressure Transducer pressure
     - 50 ms
   * - SENSOR_ANALOG.PRESSURE_CC
     - Report CC #1 and #2 Pressure Transducer pressure
     - 50 ms
   * - TODO fill
     - Report Fuel Hall Sensor reading
     - 250 ms
   * - TODO fill
     - Report Oxidizer Hall Sensor reading
     - 250 ms

CAN Message Handled by Firmware
-------------------------------

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

TODO Insert formula here
