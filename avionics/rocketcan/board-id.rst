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
   * - INJECTOR
     - Injector Board
     - 0x01
   * - CAMERA
     - Flight Camera Board
     - 0x02
   * - POWER
     - :doc:`Power Board</avionics/rocket-power-board/index>`
     - 0x03
   * - LOGGER
     - :doc:`CAN Logger Board</avionics/camera-logger-board/index>`
     - 0x04
   * - CANARD
     - :doc:`Canard Board</controls/processor-board/index>`
     - 0x05
   * - TELEMETRY
     - :doc:`Live Telemetry Board</avionics/live-telemetry/index>`
     - 0x06
   * - GPS
     - :doc:`COTS GPS Receiver Board</avionics/gps-board/index>`
     - 0x07
   * - ALTIMETER
     - :doc:`SRAD Altimeter</avionics/srad-altimeter/index>`
     - 0x08
   * - ARMING
     - :doc:`Remote Arming Board</avionics/remote-arming/index>`
     - 0x09
   * - PAYLOAD
     - Payload Board
     - 0x0A
   * - RLCS_GLS
     - :doc:`RLCS v4 Ground Launch Sequencer</electrical-gse/rlcs-v4/gls-board/index>`
     - 0x0B
   * - RLCS_RELAY
     - :doc:`RLCS v4 Relay Board</electrical-gse/rlcs-v4/relay-board/index>`
     - 0x0C
   * - DAQ
     - :doc:`DAQ(Data Acquisition System) CAN Support</electrical-gse/daq/index>`
     - 0x0D

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

Flight Camera Board
===================

.. list-table:: Flight Camera Board Instances
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Instance Name
     - ID
   * - SIDE_LOOKING
     - Side Looking Camera
     - 0x04
   * - DOWN_LOOKING
     - Down Looking Camera
     - 0x05
   * - RECOVERY
     - Recovery Looking Camera
     - 0x06

Remote Arming Board
===================

.. list-table:: Remote Arming Board Instances
   :widths: 25 60 15
   :header-rows: 1

   * - Enum Name
     - Board Instance Name
     - ID
   * - RA_RAVEN
     - Remote Arming for Raven
     - 0x07
   * - RA_STRATOLOGGER
     - Remote Arming for Stratologger
     - 0x08
