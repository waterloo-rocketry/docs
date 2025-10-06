************************
RLCS V4 Clientside Board
************************

.. image:: clientside-board.png
   :align: center

RLCS V4 Clientside board
		   
Requirements
============

.. list-table:: Clientside Board Requirements
   :widths: 15 30 55
   :header-rows: 1

   * - Req. ID
     - Description
     - Justification/Parent Requirement
   * - MECH. 1
     - Board shall have M3 mounting holes
     - Mount to RLCS Clientside face plate
   * - MECH. 2
     - Board shall be stacked vertically with LCD Display, with matching mounting hole with LCD display
     - Vertical connector can be used to ensure stable connection
   * - ELEC. 1
     - Board should have power priority switching between LiPo 12V and USB VBUS(5V)
     - Usually USB is connected to a computer with "unlimited" power source, so it should be priority
   * - ELEC. 2
     - Board shall have a 10/100 Mbps Ethernet connection
     - For communicate with towerside GLS board through local network
   * - ELEC. 3
     - Board shall have 3.3V LVCMOS UART connection
     - Backup if ethernet doesn't work
