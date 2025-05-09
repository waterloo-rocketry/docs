TxtConsole
==========
A command-line console for streaming OmniBus messages.

Synopsis
--------
.. code-block:: bash

    python txtconsole.py [CHANNEL1 CHANNEL2 ...]

Description
-----------
TxtConsole connects to an OmniBus broker and continuously prints incoming message payloads.
By default (no arguments) it listens on all channels. When one or more CHANNEL names are
provided, only messages from those channels are displayed.

Options
-------
CHANNEL1, CHANNEL2, …
     Optional list of channel names to filter incoming messages.

Examples
--------
.. code-block:: bash

    # Listen on all channels
    python txtconsole.py

    # Only show messages from 'sensor' and 'control' channels
    python txtconsole.py sensor control