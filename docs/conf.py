# -*- coding: utf-8 -*-
"""Sphinx build configuration file."""

from __future__ import unicode_literals

import os

from sphinx.ext import apidoc

from docutils import nodes
from docutils import transforms


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '2.0.1'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_markdown_tables',
    'recommonmark'
]

autodoc_mock_imports = []

# General information about the project.
# pylint: disable=redefined-builtin
project = 'Open Source DFIR tools'
copyright = 'Open Source DFIR tools authors'
version = '20200920'
release = '20200920'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The master toctree document.
master_doc = 'index'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Output file base name for HTML help builder.
htmlhelp_basename = 'opensourcedfirdoc'


# -- Options linkcheck ----------------------------------------------------

linkcheck_ignore = [
]


# -- Code to rewrite links for readthedocs --------------------------------

class MarkdownLinkFixer(transforms.Transform):
  """Transform definition to parse .md references to internal pages."""

  default_priority = 1000

  _URI_PREFIXES = []

  def _FixLinks(self, node):
    """Corrects links to .md files not part of the documentation.

    Args:
      node (docutils.nodes.Node): docutils node.

    Returns:
      docutils.nodes.Node: docutils node, with correct URIs outside
          of Markdown pages outside the documentation.
    """
    if isinstance(node, nodes.reference) and 'refuri' in node:
      reference_uri = node['refuri']
      for uri_prefix in self._URI_PREFIXES:
        if (reference_uri.startswith(uri_prefix) and
            not reference_uri.endswith('.asciidoc')):
          node['refuri'] = reference_uri + '.md'
          break

    return node

  def _Traverse(self, node):
    """Traverses the document tree rooted at node.

    Args:
      node (docutils.nodes.Node): docutils node.
    """
    self._FixLinks(node)

    for child_node in node.children:
      self._Traverse(child_node)

  # pylint: disable=arguments-differ
  def apply(self):
    """Applies this transform on document tree."""
    self._Traverse(self.document)


# pylint: invalid-name
def setup(app):
  """Called at Sphinx initialization.

  Args:
    app (sphinx.application.Sphinx): Sphinx application.
  """
  # Triggers sphinx-apidoc to generate API documentation.
  app.add_config_value(
      'recommonmark_config', {'enable_auto_toc_tree': True}, True)
  app.add_transform(MarkdownLinkFixer)
