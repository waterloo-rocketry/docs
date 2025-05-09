Publisher module
================

Defines the :class:`Publisher`, the central data bus for the dashboard.  
Enables creation and management of named data streams, allowing consumers to subscribe to value updates or periodic “clock” ticks.

.. module:: publisher
.. currentmodule:: publisher

Classes
-------

Publisher
^^^^^^^^^

Manages data streams and subscriptions.

.. class:: Publisher()

    Core data bus for the dashboard.

    Holds named streams. Consumers subscribe to streams for data updates or periodic ticks.

    **Methods**

    .. method:: __init__()

        Initializes:

        - `streams`: dict mapping stream names to subscriber lists  
        - `stream_update_callbacks`: callbacks for new streams  
        - `ticks`: tick counter  
        - `clock_callbacks`: periodic tick callbacks

    .. method:: register_stream_callback(cb)

        Register a callback for stream set changes.  
        Callback receives a sorted list of stream names.

    .. method:: get_all_streams()

        Return a sorted list of all stream names.

    .. method:: subscribe(stream, callback)

        Subscribe `callback` to updates on `stream`.  
        On `update(stream, payload)`, calls `callback(stream, payload)`.

    .. method:: unsubscribe_from_all(callback)

        Unsubscribe `callback` from all streams and clock subscriptions.

    .. method:: update(stream, payload)

        Publish `payload` to `stream`.  
        Ensures stream exists, then notifies all subscribers.

    .. method:: subscribe_clock(interval, callback)

        Subscribe `callback` to periodic ticks.  
        Calls `callback(ticks)` every `interval` calls to `update_clock()`.

    .. method:: update_clock()

        Increment tick counter and invoke matching clock callbacks.

    .. method:: ensure_exists(stream)

        Ensure `stream` is registered.  
        If new, creates it and notifies all stream update callbacks.

Module-level variables
----------------------

- **publisher**: Default :class:`Publisher` instance.
