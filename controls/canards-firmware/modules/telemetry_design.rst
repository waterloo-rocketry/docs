Telemetry Design
================

Example types
-------------

::

  typedef enum {
    SCALE_NAV_Q,
    SCALE_NAV_W,
    /* ... */
    SCALE_COUNT
  } can_scaling_t;

  typedef enum {
    TYPE_INT16,
    TYPE_UINT16,
    /* ... */
    TYPE_COUNT
  } can_types_t;

  typedef struct {
    can_types_t type;
    int16_t     scale;
  } can_scale_data_t;

  static const can_scale_data_t can_scale_map[SCALE_COUNT] = {
    [SCALE_NAV_Q] = {.type = TYPE_INT16, .scale = 10000},
    [SCALE_NAV_W] = {.type = TYPE_INT16, .scale = 10},
  };
