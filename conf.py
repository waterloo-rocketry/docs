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
    'titles_only': False,
    'body_max_width': 'none'
}

html_context = {
  'display_github': True,
  'github_user': 'waterloo-rocketry',
  'github_repo': 'docs',
  'github_version': 'main/',
}

html_css_files = [
  'custom.css'
]

# Latex Configuration
latex_elements = {
  'extraclassoptions': 'openany,oneside'
}

extensions = [
    'sphinx.ext.graphviz',
    'breathe',
    'sphinxcontrib.mermaid'
    # other extensions
]

breathe_projects_source = {
    "rocketlib" : ( "firmware-library/rocketlib/rocketlib", [
        "can_buffer/can_rcv_buffer.h",
        "can_buffer/can_tx_buffer.h",
        "can_buffer/safe_ring_buffer.h",
        "can_message/can.h",
        "can_message/msg_actuator.h",
        "can_message/msg_canards.h",
        "can_message/msg_common.h",
        "can_message/msg_general.h",
        "can_message/msg_gps.h",
        "can_message/msg_recovery.h",
        "can_message/msg_sensor.h",
        "can_message/msg_stream.h",
        "can_message/msg_telemetry.h",
        "can_message/packet_format.h",
        "common/common.h",
        "common/crc8.h",
        "common/electrical.h",
        "common/low_pass_filter.h",
        "common/mathops.h",
        "logging/mbr.h",
        "mcp2515/mcp2515.h",
        "pic18f26k83/pic18f26k83_can.h",
        "pic18f26k83/pic18f26k83_can_timing_util.h",
        "pic18f26k83/pic18f26k83_timer.h",
        "stm32h7/stm32h7_can.h"])
}

breathe_show_include = False
