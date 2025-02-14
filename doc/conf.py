import sys, os
import nestedtext

# General

project = u'NestedText'
copyright = u'2020-21, Ken and Kale Kundert'
release = '3.2.3'
version = '.'.join(release.split('.'))

master_doc = 'index'
source_suffix = '.rst'
templates_path = ['.templates']
exclude_patterns = ['.build']

# Extensions

extensions = '''\
    sphinx.ext.autodoc
    sphinx.ext.autosummary
    sphinx.ext.coverage
    sphinx.ext.doctest
    sphinx.ext.napoleon
    sphinx.ext.viewcode
    sphinx_rtd_theme
    sphinx_toolbox.collapse
'''.split()

autosummary_generate = True
html_theme = 'sphinx_rtd_theme'
pygments_style = 'sphinx'
html_static_path = ['.static']

def setup(app):
    import os
    if os.path.exists('.static/css/custom.css'):
        app.add_css_file('css/custom.css')

