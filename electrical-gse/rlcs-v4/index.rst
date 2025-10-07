Remote Launch Control System (RLCS) V4
======================================

.. toctree::
   :maxdepth: 2
   :caption: Components

   towerside.rst
   clientside.rst

RLCS V4 is the 4th generation of Waterloo Rocketry's Remote Launch Control System.

The system conprises two parts, one part Towerside is located in EGSE case at test site/launch pad, which is responsible for valve actuation and rocket communication, the other part is Clientside, located at Mission Control, responsible to communcate switch commands to towerside. The clientside and towerside communicate through Ethernet using UDP over IPv4.
   
.. image:: rlcsv4-system-architecture.png
   :align: center

