**************************************************
Payload Sensor Board Firmware Design Specification
**************************************************

.. warning::
    This is just a template, this is NOT a completed design doc, delete this line when the firmware specification is complete

Overview
========

Give an overview what does the firmware do, example:

Injector Sensor Hub firmware periodic reads analog sensors and report analog data to CAN, analog sensors includes pressure transducers and hall effect sensors.

Reference Documents
-------------------

List of reference documents (e.g. link to hardware Datasheets), example:

* `PIC18F26K83(MCU) Datasheet <https://ww1.microchip.com/downloads/en/DeviceDoc/40001943A.pdf>`_
* `IFM PT5402(Pressure Transducer) Datasheet <https://www.ifm.com/ca/en/product/PT5402#documents>`_

Note if the firmware involves data storage or transmission(e.g. Logger SD card log, telemetry packet format), then a separate rst need to be created in the same directory, to describe data format(see :doc:`Logger Data Specification<../../avionics/logger-board/data-format>` for example)

Initialization
==============

Describe step-by-step initialization sequence, example:

#. Use setup using external oscillator, with 4xPLL
#. Setup PPS(Peripheral Pin Select) for all peripherals
#. Initialize ADC, setup to use FVR(Fixed Voltage Reference)
#. Setup CAN module

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

* Firmware shall read Oxidizer pressure transducer every 50 ms, ADC voltage reading shall be convert to pressure use formula described in `Convert pressure transducer ADC pin voltage input to pressure`_ section, when the pressure output be send to can use ``SENSOR_ANALOG.PRESSURE_OX`` CAN message.

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
   * - SENSOR_ANALOG.PRESSURE_OX
     - Report oxidizer tank pressure
     - 10ms

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

Describe common used math equations in the firmware, if the equation is more than one line, then a link to a Matlab model should be provided.

Convert pressure transducer ADC pin voltage input to pressure
-------------------------------------------------------------

Insert formula here
