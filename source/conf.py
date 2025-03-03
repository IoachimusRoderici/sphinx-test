# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'Doctest'
author = 'Quetin Porta'

version = '0'
release = '0.0'

# -- General configuration ---------------------------------------------------

extensions = ['rst2pdf.pdfbuilder']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
