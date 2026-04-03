*********************
Camera & Logger Board
*********************

.. toctree::
   :maxdepth: 1

   logger-firmware.rst
   logger-data-format.rst

.. mermaid::

    gantt
        title Logger Board Timeline
        dateFormat  YYYY-MM-DD
        section Electrical
            Assemble first board      :2026-04-01, 30d
            Fabricate more boards     :30d
        section Firmware
            Initial Firmware :2026-04-01, 30d
            Unit test        :30d

Logger Requirements
===================
Logging shall start automacally when the board is powered by 12V from harness. Green LED shall toggle every 500 ms, Red LED shall toggle everytime SD card has been written to.
