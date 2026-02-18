Health Checks
=============

Each module implements ``health_result_t module_health_check(void)``.

::

  typedef enum {
    HEALTH_OK = 0,
    HEALTH_WARN,   // Log; set CAN bit
    HEALTH_ERROR,  // Log; set CAN bit; notify flight phase
    HEALTH_FATAL   // Log; set CAN bit; notify flight phase
  } health_severity_t;

  typedef struct {
    health_severity_t     severity;
    module_id_t           module_id;   // Which module
    module_error_code_t   error_code;  // Module-specific
    uint32_t              debug_data;  // Optional diagnostic
  } health_result_t;

Notes
-----
- Overcurrent is reported by the Power Handler (not by generic health checks).
