********************************
Logger Data Format Specification
********************************

Overview
========

The logger binary format is organized in pages, each page is 4 KiB size for optimize write sector alignment. The total size of the logger log file shall be a multiple of 4 KiB.

.. list-table:: File structure example with 4 pages
   :widths: 25 75
   :header-rows: 1

   * - Offset (Hex)
     - Data
   * - 0x0000 - 0x0fff
     - Page 0
   * - 0x1000 - 0x1fff
     - Page 1
   * - 0x2000 - 0x2fff
     - Page 2
   * - 0x3000 - 0x3fff
     - Page 3

Page Structure
==============

Each page is start with a signature, the signature consist of 4 bytes, the sequence number is page number modulo 256(lower 8 bits of page number)

.. list-table:: Page signature
   :widths: 25 75
   :header-rows: 1

   * - Byte
     - Data
   * - 0
     - 0x4C (ASCII of L)
   * - 1
     - 0x4F (ASCII of O)
   * - 2
     - 0x47 (ASCII of G)
   * - 3
     - Sequence Number `(seq_number = page_number & 0xff)`

CAN message data are appended after page signature, up to the page boundry

.. list-table:: CAN Message Packing Structure
   :widths: 25 75
   :header-rows: 1

   * - Byte
     - Data
   * - 0 - 3
     - SID, little endian
   * - 4
     - DLC(Data Length Code)
   * - 5 - 12
     - CAN Data Payload

CAN Data Payload shall be DLC bytes, for example if DLC==1 then the size of CAN Message Packing structure shall be 6 bytes.
