"""Configuration file for the Sphinx documentation builder.

More info at https://www.sphinx-doc.org/en/master/usage/configuration.html
"""
project = "PipeSerial"
copyright = "2020, Thomas Steen Rasmussen"
author = "Thomas Steen Rasmussen"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_theme",
    "sphinx.ext.napoleon",
    "sphinxarg.ext",
]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
master_doc = "index"
version = "0.1.0"
html_theme = "sphinx_rtd_theme"
html_theme_options = {"display_version": True}
man_pages = [
    (
        "pipeserial",
        "pipeserial",
        "Manpage for PipeSerial",
        ["Thomas Steen Rasmussen"],
        8,
    ),
]
manpages_url = "https://pipeserial.readthedocs.io/en/latest/{page}.html"
napoleon_include_init_with_doc = True
