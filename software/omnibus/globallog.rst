GlobalLog
==========

GlobalLog is a logger sink that logs all messages from ZMQ network to a file.

Usage
~~~~~
The GlobalLog sink runs with no arguments and outputs to a file. The sink can be started with the following command:

.. code-block:: bash

    python sinks/globallog/main.py

The GlobalLog sink can be stopped by pressing ``Ctrl + C``.

.. note::
    The output file is stored in the format ``<timestamp>.log`` in your current working directory.


