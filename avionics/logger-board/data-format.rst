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

CAN message data are appended after page signature, up to the page boundry. Unused bytes after last message in the page shall be filled with `0xff`

.. list-table:: CAN Message Packing Structure
   :widths: 25 75
   :header-rows: 1

   * - Byte
     - Data
   * - 0 - 3
     - SID, little endian
   * - 4 - 7
     - Timestamp, milli-second, little endian (time when logger received CAN message)
   * - 8
     - DLC(Data Length Code)
   * - 9 - 16
     - CAN Data Payload

CAN Data Payload shall be DLC bytes, `sizeof(packing_structure) = 9 + DLC`, for example if `DLC == 1` then the size of CAN Message Packing structure shall be 10 bytes. SID[31:29] shall be 0 for valid CAN messages. DLC shall be between 0 to 8 inclusive.

Implementation Note
===================

Writer (Logger Board)
---------------------
Before each message is written to the page buffer, the firmware shall check to make sure enough space is left in the page buffer, if there's not enough space left, then firmware shall fill remaining space with `0xff` and write the page to SD card, then write the message to the new page buffer.

Reader (Parsley)
----------------

.. code-block:: text

   while(4096-RPTR >= 6):
       sid = read_4_bytes()
       if((sid & 0xe0000000) == 0): # check SID[31:29]
           # Valid CAN message
       else:
           # End of page

