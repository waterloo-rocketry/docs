Data Management Guide
=====================

PCB and software/firmware shall not share a Git repository

PCB Design
----------
PCB should be placed in a Git repository for PCB, each KiCAD PCB design shall be in a folder in the root of Git repository. List of Git repositories

.. list-table:: Git Repository
   :widths: 40 60
   :header-rows: 1

   * - Link
     - Description
   * - `canhw <https://github.com/waterloo-rocketry/canhw>`_
     - Avionics PCB designs except Controls and Payload
   * - `payload-2025-electrical <https://github.com/waterloo-rocketry/payload-2025-electrical>`_
     - Payload PCB Design
   * - `controls-2025-electrical <https://github.com/waterloo-rocketry/controls-2025-electrical>`_
     - Controls PCB Design
   * - `rlcsv4-electrical <https://github.com/waterloo-rocketry/rlcsv4-electrical>`_
     - RLCS v4 PCB Design
   * - `daq <https://github.com/waterloo-rocketry/daq>`_
     - DAQ PCB Design
   * - `infrastructure <https://github.com/waterloo-rocketry/infrastructure.git>`_
     - GSPD and Tank Heater PCB Design

Software and Firmware
---------------------

Each software and firmware project should have it's own Git repository, for avionics firmware the repository name shall start with :code:`cansw_`
