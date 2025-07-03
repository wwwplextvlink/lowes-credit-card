# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'How to Pay Your Lowe’s Credit Card Bill Online'
copyright = '2025, Lowe’s Credit Card Help'
author = 'Lowe’s Credit Card Help'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Pay Your Lowe’s Credit Card Bill Online – Step-by-Step Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Pay Lowe’s Credit Card Online"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (uncomment to enable)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source" link
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

raw_enabled = True

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you have static assets

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
