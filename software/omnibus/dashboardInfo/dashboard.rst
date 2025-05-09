Dashboard module
================

This module defines the ``Dashboard`` class, which provides the main GUI window
and integrates with the data bus for a real-time dashboard.
It also includes ``QGraphicsViewWrapper`` for enhanced view interactions
and the ``dashboard_driver`` function to launch the application.

.. module:: dashboard
.. currentmodule:: dashboard

Classes
-------

QGraphicsViewWrapper
^^^^^^^^^^^^^^^^^^^^

Wrapper around ``QGraphicsView`` to intercept wheel events for custom zooming
and horizontal/vertical scrolling.

.. class:: QGraphicsViewWrapper(scene, dashboard)

    :param scene: Instance of ``QGraphicsScene`` to display.
    :param dashboard: The parent ``Dashboard`` instance.

    **Methods**

    .. method:: __init__(scene, dashboard)
        :noindex:

        Initialize the view wrapper with default zoom level,
        scroll sensitivity, and a reference to the dashboard.

    .. method:: wheelEvent(event)
        :noindex:

        Handle wheel events:

        - Zoom in/out if Ctrl/Cmd is held.
        - Scroll horizontally if Shift is held.
        - Scroll vertically otherwise.

Dashboard
^^^^^^^^^

Main widget for the dashboard application, managing items,
menus, interactions, and timed updates.

.. class:: Dashboard(callback)

    :param callback: Function invoked for outgoing message callbacks (e.g., sending CAN messages).

    **Class Attributes**

    .. attribute:: build_info
        :type: BuildInfoManager

        Holds application name and build number metadata.

    **Methods**

    .. method:: __init__(callback)
        :noindex:

        Set up the application window, subscribe to the data bus on ``"ALL"``,
        and initialize menus, scene, view, and registry triggers.

    .. method:: contextMenuEvent(event)
        :noindex:

        Display a context menu at the cursor for item actions
        (duplicate, remove, lock, z-order operations).

    .. method:: select_instance(instance)
        :noindex:

        Change the current Parsley data source instance and reload items.

    .. method:: check_for_changes()
        :noindex:

        Detect external configuration changes via ``EventTracker`` and prompt to reload.

    .. method:: change_detector()
        :noindex:

        Periodically poll for backend data updates and mark for refresh.

    .. method:: every_second(stream, payload)
        :noindex:

        Handler for the special ``"ALL"`` stream; used for timed callbacks.

    .. method:: send_can_message()
        :noindex:

        Send a CAN bus message using the configured ``omnibus_sender``.

    .. method:: open_property_panel()
        :noindex:

        Show the property panel for the currently selected dashboard item.

    .. method:: on_selection_changed()
        :noindex:

        React to selection changes in the scene and update the property panel.

    .. method:: close_property_tree()
        :noindex:

        Close and remove the property panel widget.

    .. method:: on_duplicate()
        :noindex:

        Duplicate the currently selected dashboard items.

    .. method:: on_item_resize()
        :noindex:

        Update item parameters in response to user-initiated resizing.

    .. method:: remove()
        :noindex:

        Remove the currently selected dashboard item.

    .. method:: remove_all()
        :noindex:

        Prompt for confirmation and remove all dashboard items.

    .. method:: remove_selected()
        :noindex:

        Remove all currently selected dashboard items.

    .. method:: load()
        :noindex:

        Load a dashboard layout from a JSON configuration file.

    .. method:: save()
        :noindex:

        Save the current layout to the last opened file.

    .. method:: save_as()
        :noindex:

        Prompt for a file path and save the layout under a new name.

    .. method:: open()
        :noindex:

        Open a file dialog and load a dashboard configuration file.

    .. method:: show_save_popup()
        :noindex:

        Display a dialog prompting the user to save unsaved changes.

    .. method:: show_save_as_prompt()
        :noindex:

        Prompt the user for a new save location via dialog.

    .. method:: lock_selected()
        :noindex:

        Mark all selected widgets as locked against movement and resizing.

    .. method:: lock_widget(widget)
        :noindex:

        Lock a specific widget, disabling its movement/resizing.

    .. method:: unlock()
        :noindex:

        Unlock the specified widget(s), restoring movement and resizing.

    .. method:: toggle_lock()
        :noindex:

        Toggle the lock/unlock state of all dashboard items.

    .. method:: toggle_mouse()
        :noindex:

        Toggle mouse-powered item resizing mode.

    .. method:: reset_zoom()
        :noindex:

        Reset the view’s zoom level to its default scale.

    .. method:: get_data()
        :noindex:

        Retrieve data or parameters from the selected dashboard item.

    .. method:: help()
        :noindex:

        Show the application’s help or about dialog.

    .. method:: update()
        :noindex:

        Timer-driven refresh method; called at ~60 FPS to refresh the dashboard.

    .. method:: send_forward()
        :noindex:

        Move selected item(s) one layer forward in the z-order.

    .. method:: send_backward()
        :noindex:

        Move selected item(s) one layer backward in the z-order.

    .. method:: send_to_front()
        :noindex:

        Bring selected item(s) to the front of the view stack.

    .. method:: send_to_back()
        :noindex:

        Send selected item(s) to the back of the view stack.

Functions
---------

dashboard_driver
^^^^^^^^^^^^^^^^

.. function:: dashboard_driver(callback)

    Launch the Qt application and start the main event loop
    with a ``Dashboard`` instance and a periodic update timer.

    :param callback: Function for message callbacks from the UI.
