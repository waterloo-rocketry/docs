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
    # other extensions
]
