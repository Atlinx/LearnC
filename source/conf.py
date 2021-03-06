# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Learn C'
copyright = '2022, Atlinx'
author = 'Atlinx'

# The full version, including alpha/beta/rc tags
release = '1.0.0'
html_title = "Learn C 🌱"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'notfound.extension',
	'sphinx_toolbox.collapse',
	'sphinx.ext.autosectionlabel',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css']

html_favicon = '_static/favicon.ico'

on_rtd = os.environ.get("READTHEDOCS", None) == "True"
on_gh_pages = "GITHUB_REPOSITORY" in os.environ

html_js_files = ['custom.js']


# -- Furo --------------------------------------------------------------------

html_theme_options = {
	"light_css_variables": {
		"admonition-font-size": "qem",
	},
	"dark_css_variables": {
		"admonition-font-size": "1em",
	}
}


# -- Autosection Label -------------------------------------------------------

autosectionlabel_prefix_document = True;
autosectionlabel_maxdepth = 10;


# -- Not Found Page ----------------------------------------------------------

if on_gh_pages:
	notfound_urls_prefix = "/LearnC/"
elif not on_rtd:
	notfound_urls_prefix = ''


# -- Sphinx Toolbox ----------------------------------------------------------

github_username = "Atlinx"
github_repository = "github.com/atlinx/LearnC"