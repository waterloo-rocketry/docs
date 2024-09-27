RLCS V3 Clientside
==================

.. toctree::
   :maxdepth: 2
   :caption: Board

   clientside-board.rst

Clientside is used by the RLCS Control operator to control motorized valves and ignition. Clientside is a relatively simple system composed of an Arduino Mega, a LCD module several missile switches, and a custom PCB that regulates a 3S LiPo down to 5 V for power. Additionally, it exposes a USB port which allows it to send data to a computer for plotting and logging. Clientside contains a set of missile switch, each match to a motorized valve. There is also the ignition button paired with a arming missile switch for controlling current pass through nichrome ignition coil. The LCD module displays the state of all motorized value(open, closed, and not connected), and it also display voltage of LiPo batteries and ignition coil current.
