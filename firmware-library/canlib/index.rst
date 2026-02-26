******
canlib
******

.. toctree::
   :maxdepth: 1

   dev-dashboard.rst
   ref-driver.rst
   ref-serialize.rst

Introduction
============

Canlib is Waterloo Rocketry's firmware library for CAN communication.

Roles and Responsibilities
==========================

.. list-table:: Roles and Responsibilities
   :header-rows: 1
   :widths: 30 40 30

   * - **Role**
     - **Responsibilities**
     - **Names**
   * - Message Serialization Function Developer
     - - Writes Code
     - - `Jason Xu <https://github.com/JasonBrave>`_
   * - PIC18 CAN Controller Driver Developer
     - - Writes Code
	 - - Test on physical hardware
     - - `Jason Xu <https://github.com/JasonBrave>`_
   * - STM32 CAN Controller Driver Developer
     - - Writes Code
	 - - Test on physical hardware
     - - `Jason Xu <https://github.com/JasonBrave>`_
   * - Utility Function Developer
     - - Writes Code
     - - `Jason Xu <https://github.com/JasonBrave>`_
   * - Message + Utility Function Tester
     - - Writes Unit Test
     - - `Jason Xu <https://github.com/JasonBrave>`_

Release Schedule
================

A major release is released each time CAN packet format is updated, and a minor release is for bugfix only with compatiable function interface with last major release.


Links
=====

* :doc:`CAN Packet Format</avionics/rocketcan/packet-format>`
* `GitHub Repository <https://github.com/waterloo-rocketry/canlib>`_
