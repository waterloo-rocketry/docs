************************
RLCS V4 Clientside Board
************************

Requirements
============

.. list-table:: Clientside Board Requirements
   :widths: 15 30 55
   :header-rows: 1

   * - Req. ID
     - Description
     - Justification/Parent Requirement
   * - ELEC. 1
     - Board shall only draw power from 12V Rail
     - Reduce current draw on 5V line
   * - ELEC. 2
     - Board shall have shielding for RF traces/IC
     - Protect noise-sensitive circuit from noises
   * - ELEC. 3
     - Board shall have CAN 2.0 bus connection
     - For rocket avionics communication
   * - ELEC. 4
     - Board shall have 3.3V LVCMOS UART connection
     - For debugging without CAN connection
   * - ELEC. 5
     - Board shall have a JTAG connector
     - For FPGA programming
   * - ELEC. 6
     - Board shall have a Micro-SD card connector
     - For raw data logging
   * - GPS. 1
     - Board shall support L1 C/A and L2C code, and should support L1C and L5 code
     - Allows future development to support all GPS bands/codes
   * - MECH. 1
     - Board shall have m3 mounting hole at 4 corners
     - For mounting to Recovery Electronics sled
