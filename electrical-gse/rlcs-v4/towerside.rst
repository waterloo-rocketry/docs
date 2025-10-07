RLCS V4 Towerside
=================

.. toctree::
   :maxdepth: 2
   :caption: Boards

   ground-launch-sequencer-board.rst
   towerside-relay-board.rst

The towerside is the remote part of the RLCS system, It handles receiving commands from network and controls motorized valves/tank heating/ignition, and for rocket launch ops use case, communicate to electrical disconnect. The system has a single :doc:`Ground Launch Sequencer Board</electrical-gse/rlcs-v4/ground-launch-sequencer-board>` and multiple :doc:`Relay boards</electrical-gse/rlcs-v4/towerside-relay-board>`, which all the boards are connected through CAN, the ground launch sequencer board handles communication between ethernet and Relay Boards(via CAN), the Relay Boards controls power output based on received CAN command.

Refer to :doc:`RLCS v4</electrical-gse/rlcs-v4/index>` page for internal electrical connection diagram.

Requirements
============

Note this project do not have mechanical requirements, because the requirements are covered in EGSE Respin requirements.

.. list-table:: Towerside Requirements
   :widths: 15 30 55
   :header-rows: 1

   * - ELEC. 1
     - System have a 10/100 Mbps Ethernet connection
     - For communicate with towerside GLS board through local network
   * - ELEC. 2
     - System shall have a Type B USB port
     - For get power from another device, and optional data logging
   * - ELEC. 3
     - System shall be able to power from the USB port(ELEC.2) or a 3S LiPo battery
     - Redundant power supply
