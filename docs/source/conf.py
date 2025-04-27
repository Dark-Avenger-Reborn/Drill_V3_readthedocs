
# Configuration file for the Sphinx documentation builder.

project = 'DRILL V3'
copyright = '2025'
author = 'Oz Abramovich'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
