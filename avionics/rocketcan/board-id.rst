Board IDs
#########

Board Type IDs
**************

.. list-table:: Board Type IDs
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Name
     - ID
   * - ANY
     - Any Board
     - 0x00
   * - INJ_SENSOR
     - :doc:`Injector Sensor Hub Board</avionics/injector-sensor-hub/index>`
     - 0x01
   * - CANARD_MOTOR
     - :doc:`Canard Motor Control Board</controls/motor-control-board/index>`
     - 0x02
   * - CAMERA
     - :doc:`Flight Camera Board</avionics/camera-board/index>`
     - 0x03
   * - POWER
     - :doc:`Power Board</avionics/rocket-power-board/index>`
     - 0x04
   * - LOGGER
     - CAN Logger Board
     - 0x05
   * - PROCESSOR
     - :doc:`Canard Processor Board</controls/processor-board/index>`
     - 0x06
   * - TELEMETRY
     - :doc:`Live Telemetry Board</avionics/live-telemetry/index>`
     - 0x07
   * - GPS
     - :doc:`COTS GPS Receiver Board</avionics/gps-board/index>`
     - 0x08
   * - SRAD_GNSS
     - :doc:`SRAD GNSS Receiver Board</avionics/srad-gnss-receiver/index>`
     - 0x09
   * - ALTIMETER
     - :doc:`SRAD Altimeter</avionics/srad-altimeter/index>`
     - 0x0A
   * - ARMING
     - :doc:`Remote Arming Board</avionics/remote-arming/index>`
     - 0x0B
   * - PAY_SENSOR
     - Payload Sensor Board
     - 0x40
   * - PAY_MOTOR
     - Payload Motor Control Board
     - 0x41
   * - RLCS_GLS
     - :doc:`RLCS v4 Ground Launch Sequencer</electrical-gse/rlcs-v4/ground-launch-sequencer-board>`
     - 0x80
   * - RLCS_RELAY
     - :doc:`RLCS v4 Relay Board (Valve and Ignition)</electrical-gse/rlcs-v4/towerside-relay-board>`
     - 0x81
   * - RLCS_HEATING
     - :doc:`RLCS v4 Tank Heating Relay Board</electrical-gse/rlcs-v4/tank-heating-relay-board>`
     - 0x82
   * - DAQ
     - :doc:`DAQ(Data Acquisition System) CAN Support</electrical-gse/daq/index>`
     - 0x83
   * - CHARGING
     - Ground Side LiPo Charging Board
     - 0x84
   * - THERMOCOUPLE
     - :doc:`Thermocouple Board (K-type)</electrical-gse/daq/thermocouple-board>`
     - 0x85
   * - USB
     - :doc:`USB Debug</electrical-tools/usb-debug/index>`
     - 0x86
   * - FYDP25_TVCA
     - FYDP 25 TVC Actuator Board
     - 0xC0

Board Instance IDs
******************

Common Instance IDs
===================

.. list-table:: Common Instance IDs
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Instance Name
     - ID
   * - ANY
     - Any board
     - 0x00
   * - GROUND
     - Board on ground
     - 0x01
   * - ROCKET
     - Board on rocket
     - 0x02
   * - PAYLOAD
     - Board in payload
     - 0x03

Canard Motor Control Board
==========================

.. list-table:: Canard Motor Control Board Instances
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Instance Name
     - ID
   * - PRIMARY
     - Canard Motor Control Board Primary MCU
     - 0x04
   * - FAILSAFE
     - Canard Motor Control Board Failsafe MCU
     - 0x05

Flight Camera Board
===================

.. list-table:: Flight Camera Board Instances
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Instance Name
     - ID
   * - INJ_A
     - Injector Section Camera A
     - 0x06
   * - INJ_B
     - Injector Section Camera B
     - 0x07
   * - VENT_A
     - Vent Section Camera A
     - 0x08
   * - VENT_B
     - Vent Section Camera B
     - 0x09
   * - VENT_C
     - Vent Section Camera C
     - 0x0A
   * - VENT_D
     - Vent Section Camera D
     - 0x0B
   * - RECOVERY
     - Recovery Bulkhead Camera
     - 0x0C

Thermocouple Board (K-type)
===========================

.. list-table:: Thermocouple Board (K-type) Instances
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Instance Name
     - ID
   * - 1
     - Thermocouple board 1, reads channel 1 to 4
     - 0x0D
   * - 2
     - Thermocouple board 2, reads channel 5 to 8
     - 0x0E
   * - 3
     - Thermocouple board 3, reads channel 9 to 12
     - 0x0F
   * - 4
     - Thermocouple board 4, reads channel 13 to 16
     - 0x10
