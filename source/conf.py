# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ameba AIoT Documentation Homepage'
copyright = '2025 Realtek Semiconductor Corp. All rights reserved'
author = 'REALTEK SG SD3'
release = 'v1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx_markdown_tables',
    'sphinx.ext.intersphinx',
    'sphinx_tabs.tabs'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_context = {
    "display_github": True,
    "github_user": "Ameba-AIoT",
    "github_repo": "ameba-docs",
    "github_version": "main",
    "conf_py_path": "/source/",
}

html_logo = '_static/Realtek_logo.png'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]
numfig = True
