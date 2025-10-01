# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Waterloo Rocketry Documentation'
copyright = '2024, Waterloo Rocketry'
author = 'Waterloo Rocketry'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_copy_source =  False
html_show_sphinx = False
html_show_copyright = False

html_logo = 'logo.png'

html_theme_options = {
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_context = {
  'display_github': True,
  'github_user': 'waterloo-rocketry',
  'github_repo': 'docs',
  'github_version': 'main/',
}

# Latex Configuration
latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

extensions = [
    'sphinx.ext.graphviz',
    'breathe'
    # other extensions
]

breathe_projects_source = {
    "canlib" : ( "firmware-library/canlib/canlib", ["can.h", "message_types.h", "message/msg_actuator.h", "message/msg_common.h", "message/msg_general.h", "message/msg_gps.h", "message/msg_recovery.h", "message/msg_sensor.h", "message/msg_state_est.h", "mcp2515/mcp_2515.h", "pic18f26k83/pic18f26k83_can.h", "stm32h7/stm32h7_can.h", "util/can_rcv_buffer.h", "util/can_tx_buffer.h", "util/safe_ring_buffer.h", "util/timing_util.h"] )
}
