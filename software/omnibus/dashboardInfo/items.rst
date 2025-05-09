Dashboard item module
=====================

This module defines the ``DashboardItem`` class, which serves as the abstract base class
(template) for all dashboard widgets. Subclasses should extend ``DashboardItem`` and
implement or override specific methods to define their behavior, parameters, and appearance.

.. module:: dashboard_item
.. currentmodule:: dashboard_item

Classes
-------

DashboardItem
^^^^^^^^^^^^^

Abstract superclass for all dashboard items. Manages common UI behavior (resizing,
parameter trees, mouse interactions) and defines the interface subclasses must implement.

.. class:: DashboardItem(dashboard, params=None)

    :param dashboard: The parent ``Dashboard`` instance to which this item belongs.
    :param params: Optional JSON string of serialized parameters to restore state.

    **Methods**

    .. method:: __init__(dashboard, params=None)

        Initialize the widget:
        - Store the ``dashboard`` reference.
        - Enable mouse tracking for resize handles.
        - Initialize corner-grab state (size, index, flags).
        - Create a ``pyqtgraph.Parameter`` group with ``"width"`` and ``"height"`` children.
        - Call ``add_parameters()`` to insert widget-specific parameters.
        - Wrap parameters in a custom ``ParameterTree`` for display.
        - Restore state from ``params`` if provided and set up resize callbacks.

    .. method:: resizeEvent(event)

        Called when the widget is resized. Updates the ``"width"`` and ``"height"`` parameters
        to match the new size and invokes the dashboard’s resize callback.

    .. method:: add_parameters() -> list[Parameter]

        Return a list of ``pyqtgraph.Parameter`` objects defining this widget’s custom
        properties (aside from size). Called once when the item is added.

    .. method:: get_name() -> str

        **Abstract/static method.** Return a human-friendly name for this item type.
        Must be overridden by subclasses (default raises ``NotImplementedError``).

    .. method:: get_parameters() -> Parameter

        Return the root ``pyqtgraph.Parameter`` group containing all parameters
        (size + custom) for this widget. Used to build the property panel.

    .. method:: get_serialized_parameters() -> str

        Serialize the current parameter state to a JSON string suitable for saving
        to a dashboard configuration file.

    .. method:: on_delete()

        Called when this widget is removed from the dashboard. Subclasses may override
        to clean up subscriptions or resources (default is a no-op).

    .. method:: dynamic_corner_size() -> int | float

        Compute and return the size of the corner “grabber” handle based on the widget’s
        dimensions and the dashboard’s ``mouse_resize`` setting (0 if resizing is disabled).

    .. method:: mousePressEvent(event)

        If the click occurs within a corner “grabber” region (and resizing is enabled),
        begin resizing mode; otherwise, defer to the base ``QWidget`` handler.

    .. method:: mouseMoveEvent(event)

        Change the mouse cursor to indicate resize readiness when hovering over a
        corner handle; reset the cursor otherwise.

    .. method:: mouseReleaseEvent(event)

        End resizing mode on mouse release, reset grab state, and recompute corner handle size;
        otherwise, pass the event to the base handler.

    .. method:: corner_hit(pos) -> bool

        Check whether the given point (a ``QPoint`` in widget coordinates) lies within any
        of the four resize handles. If so, update ``corner_index`` and return ``True``.

    .. method:: paintEvent(event)

        Override the paint event to draw the corner grab handles when the mouse is
        hovering over them.

    .. method:: draw_corner(painter)

        Draw the four invisible corner rectangles and, if active, fill the current
        corner grabber to indicate it can be dragged.
