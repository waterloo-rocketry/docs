Parsers module
==============

This module defines the message parsing framework. It provides a
:class:`Register` decorator for associating parsing functions to message
channel prefixes, a :func:`parse` function to dispatch messages to
appropriate parsers, and several built-in parsers.

.. module:: parsers
.. currentmodule:: parsers

Classes
-------

Register
^^^^^^^^

Decorator to register parser functions under specific message channel prefixes.

.. class:: Register(msg_channels)

    **Class Attributes**

    .. attribute:: func_map
        :type: dict

        Maps message channel prefixes to lists of registered parser functions.

    **Constructor**

    .. method:: __init__(msg_channels)
        Initialize the decorator with one or more channel prefixes.

        :param msg_channels: A string or list of strings representing channel prefixes.

    **Call**

    .. method:: __call__(func)
        Register the decorated function under the configured channel prefixes.

        :param func: The parser function to register.
        :returns: The original function.

Functions
---------

parse
^^^^^

.. function:: parse(msg_channel, msg_payload)

    Dispatch the incoming message to all parser functions whose registered
    channel prefix matches the start of ``msg_channel``. Each parser yields
    tuples of ``(stream_name, timestamp, parsed_message)``, which are forwarded
    to the global ``publisher`` instance.

    :param msg_channel: The channel name of the incoming message.
    :param msg_payload: The payload data for the message.

daq_parser
^^^^^^^^^^

.. function:: daq_parser(msg_data)

    Parser for "DAQ" messages. Computes the average of each sensor's data list
    and yields ``(sensor, timestamp, average_value)`` tuples.

    :param msg_data: Dict with keys ``"timestamp"`` and ``"data"`` mapping sensor names to lists of values.

can_parser
^^^^^^^^^^

.. function:: can_parser(payload)

    Parser for CAN bus messages. Splits messages based on their type-specific
    fields, handles timestamp rollovers, and emits one stream per data field
    plus optional error/reset streams.

    :param payload: Dict representing a CAN message with keys
        ``"board_type_id"``, ``"board_inst_id"``, ``"msg_type"``, and ``"data"``.
    :returns: List of ``(stream_name, timestamp, value)`` tuples.

rlcs_parser
^^^^^^^^^^^

.. function:: rlcs_parser(payload)

    Parser for RLCS messages. Emits one stream per key in the payload.

    :param payload: Dict of RLCS data fields.

parsley_health
^^^^^^^^^^^^^^

.. function:: parsley_health(payload)

    Health check parser for the Parsley subsystem. Yields a single stream with
    the healthy status.

    :param payload: Dict with keys ``"id"`` and ``"healthy"``.

state_est_parser
^^^^^^^^^^^^^^^^

.. function:: state_est_parser(payload)

    Parser for StateEstimation messages. Emits orientation and position streams.

    :param payload: Dict with keys ``"timestamp"`` and ``"data"`` containing ``orientation`` and ``position``.

all_parser
^^^^^^^^^^

.. function:: all_parser(_)

    Catch-all parser that emits a single "ALL" stream for any message.

    :param _: Unused payload.

Module-level Variables
----------------------

.. data:: splits

    Dict mapping message types to the field used to split data into separate streams.

.. data:: last_timestamp

    Dict tracking the last timestamp seen for each board-and-message key to detect rollovers.

.. data:: offset_timestamp

    Dict tracking cumulative offsets to correct for timestamp rollovers.
