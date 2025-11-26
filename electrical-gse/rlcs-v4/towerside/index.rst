*****************
RLCS V4 Towerside
*****************

.. toctree::
   :maxdepth: 2
   :caption: Boards

   ../gls-board/index.rst
   ../relay-board/index.rst

The towerside is the remote part of the RLCS system, It handles receiving commands from network and controls motorized valves/tank heating/ignition, and for rocket launch ops use case, communicate to electrical disconnect. The system has a single :doc:`Ground Launch Sequencer Board</electrical-gse/rlcs-v4/gls-board/index>` and multiple :doc:`Relay boards</electrical-gse/rlcs-v4/relay-board/index>`, which all the boards are connected through CAN, the ground launch sequencer board handles communication between ethernet and Relay Boards(via CAN), the Relay Boards controls power output based on received CAN command.

Refer to :doc:`RLCS v4</electrical-gse/rlcs-v4/index>` page for internal electrical connection diagram.

Requirements (Towerside)
========================

Note this project do not have mechanical requirements, because the requirements are covered in EGSE Respin requirements.

.. list-table:: Towerside Requirements
   :widths: 15 30 55
   :header-rows: 1

   * - Req. ID
     - Description
     - Justification/Parent Requirement
   * - ELEC. 1
     - System have a 10/100 Mbps Ethernet connection
     - For communicate with clientside through local network
   * - OPS. 1
     - The Towerside shall have a external CAN connection to Rocket Electrical Disconnect
     - Control would need injector valve/QD state for unlocking
   * - RLCS. 1
     - The ED CAN bus shall be separated from internal CAN bus
     - If RocketCAN is fucked, we don’t want it to affect RLCS internal CAN bus operation
