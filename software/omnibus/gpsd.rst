GPSD
====

.. warning::
    This sink is deprecated and will be removed in the future. Interamap is the recommended sink instead.

GPSD is a sink that parses geographic data from the ZMQ network (Source). 


Usage
~~~~~
The GPSD sink runs with no arguments and outputs to stdout. The sink can be started with the following command:

.. code-block:: bash

    python sinks/gpsd/main.py


The GPSD sink can be stopped by pressing ``Ctrl + C``.

Format
~~~~~~

.. list-table:: **GPSD Output Format**
    :header-rows: 1

    * - HEADER
      - TIMESTAMP
      - LATITUDE
      - LATITUDE_DIRECTION
      - LONGITUDE
      - LONGITUDE_DIRECTION
      - QUALITY
      - NUMBER_OF_SATELLITES
      - _
      - ALTITUDE
      - DALTITUDE
      - CHECKSUM
    * - ``$GPGGA``
      - ``183038.00``
      - ``4757.9313``
      - ``N``
      - ``8152.4151``
      - ``W``
      - ``1``
      - ``06``
      - ``1.0``
      - ``436.90 M``
      - ``0 M``
      - ``*74``
    * - ``$GPGGA``
      - ``183038.00``
      - ``8152.50``
      - ``N``
      - ``4757.19``
      - ``W``
      - ``1``
      - ``06``
      - ``1.0``
      - ``378.28 M``
      - ``0 M``
      - ``*7e``
    * - ``$GPGGA``
      - ``183039.00``
      - ``8152.50``
      - ``N``
      - ``4757.19``
      - ``W``
      - ``6``
      - ``16``
      - ``1.0``
      - ``378.28 M``
      - ``0 M``
      - ``*79``


Known Issues and Limitations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1. TIMESTAMP is not the actual time the data was received; the package timestamp is delayed.
2. Unable to determine the data source board.
3. Direction is hardcoded to N and W.
4. There is no way to exit the gpsd sink gracefully.