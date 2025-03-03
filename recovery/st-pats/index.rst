ST PATS
=======
ST PATS stands for System That Points To The Shark, it is a device the shows the location, direction, and distance of the rocket. In the center, there are 3 buttons, 2 LEDs, and 1 screen. On the right, there’s a reset button and a power switch.

.. image:: st-pats.jpg
   :alt: Picture of st-pats

The left, red LED lights up when the board is powered. The right, blue LED lights up when telemetry data is received.

There are two modes of operation: serial and radio. In serial mode, GPS coordinate is received from USB serial; in radio mode, GPS coordinate is received from the radio module.

Calibration
-----------
The on-board compass needs to be calibrated when a firmware is flashed or when using stpats in a new environment. The compass will not work correctly without calibration. To enter calibration mode, press the left button. The min/max value of each axis should appear on the top left of the screen. Rotate the whole device in every direction so the numbers stabilize, the press the left button again to save the calibration.

Radio Telemetry
---------------
The radio and serial mode can be toggled using the right button. In radio mode, it parses the serialized CAN messages sent from the rocket and decodes the GPS locations. The UART of radio is set at 57600 baud.

Serial Telemetry
----------------

As an alternative to radio telemetry, USB serial can also be used to send GPS coordinate to stpats. The serial mode can be switched to using the right button. The GPS message has the format of ``[0-9]+.[0-9]*[NSEWM]``, for example: ``12.34N56.78W90M`` means 12.34 degrees north, 56.78 degrees west, 90m high. The altitude information is not used in the calculations so it’s optional.

aprs2stpats.py
--------------
The stpats repository includes a utils/aprs2stpats.py that can be used to send APRS coordinates to stpats. To use, install aprspy and bitstring using pip, then follow the steps in 

 to setup and run direwolf.

Usage: ::

   aprs2stpats.py [--host HOST | -H HOST] [--port PORT | -p PORT] [--callsign CALLSIGN | -c CALLSIGN] [--output OUTPUT | -o OUTPUT] [--debug]


The ``--host`` and ``--port`` options specifies the KISS TNC server to connect to. By default, they are 127.0.0.1:8001, which connects to a direwolf instance running on localhost.

The ``--callsign`` option filters the message by sender’s callsign, in case there are multiple APRS beacons on the same frequency. Note the callsign includes ssid, for example, VE7OIR-1 instead of just VE7OIR. By default, it forwards all GPS messages.

The ``--output`` option specified the output. By default it is stdout. To send the output to serial, use ``--output \\.\COM1`` (Windows) or ``--output /dev/ttyACM0`` (Linux), change COM1 or ACM0 to the actual serial port stpats is on.

The ``--debug`` options prints additional info to stderr.

Persistent Location
-------------------
Press the middle button in either mode to save the current tracking location in flash so a reset doesn’t lose it. Most useful when one wants to unplug stpats from computer in serial mode, pressing the middle button before disconnecting allows one to move around without worrying losing track in case of accidental reset.

Note: similiar to calibration data, flashing a firmware wipes the flash and so the saved data.
