Remote Launch Control System (RLCS)
===================================

.. toctree::
   :maxdepth: 2
   :caption: Components

   towerside.rst
   clientside.rst
   timer.rst

The Remote Launch Control System (RLCS) is the primary means of interfacing with the rocket and supporting
fill plumbing during launch operations. The main objective of the system is to allow launching the rocket from up to
3,000 ft from the tower. Once the RLCS operator takes control of the launch process, no human intervention should be
required at the launch site in any possible error state that requires a human to approach the system. In the event of total failure, the system must put all engine and fill systems into a known safe state so that personnel can approach the rocket without placing themselves in danger.

RLCS is made up of two halves, Clientside and Towerside, which communicate over a radio link formed by a pair of
Litebeam 5ac gen2. Towerside is located beside the launch tower and handles actuating motorized valves and ignition.
Clientside is located at mission control and houses switches that map to the various actuators and an LCD to display
data to the operator. Both halves are built into weatherproof and robust Pelican cases to protect them from the elements.
