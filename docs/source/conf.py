# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

project = 'TestsRefactoringMiner'
copyright = '2023, Luana Martins'
author = 'Luana Martins'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  'sphinx.ext.autosectionlabel',
  'sphinx.ext.autodoc',
  'sphinx.ext.intersphinx',
]

templates_path = ['_templates']


source_suffix = ['.rst']
master_doc = 'index'
language = 'en'

exclude_patterns = []

pygments_style = 'sphinx'
html_theme = 'sphinx_rtd_theme'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
     