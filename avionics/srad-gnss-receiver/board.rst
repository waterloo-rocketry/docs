************************
SRAD GNSS Receiver Board
************************

Requirements
============

.. list-table:: SRAD GNSS Receiver Board Requirements
   :widths: 15 30 55
   :header-rows: 1

   * - Req. ID
     - Description
     - Justification/Parent Requirement
   * - ELEC. 1
     - Board should only draw power from 12V Rail
     - Reduce current draw on 5V line
   * - ELEC. 2
     - Board should have shielding for RF traces/IC
     - Protect noise-sensitive circuit from noises
   * - ELEC. 3
     - Board should have CAN 2.0 bus connection
     - For rocket avionics communication
   * - ELEC. 4
     - Board should have 3.3V LVCMOS UART connection
     - For debugging without CAN connection
   * - ELEC. 5
     - Board should have a JTAG connector
     - For FPGA programming
   * - ELEC. 6
     - Board should have a Micro-SD card connector
     - For raw data logging
   * - GPS. 1
     - Board should support all of GPS L1C/L2C/L5 frequency band
     - ??? Scope Creep ???
   * - MECH. 1
     - Board should have m3 mounting hole at 4 corners
     - For mounting to Recovery Electronics sled
