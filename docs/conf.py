# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.append(os.path.abspath('.'))
import metamodel

sys.path.append(os.path.abspath('scripts'))
from filter import filter_id_linked_element_and_back

# For autodoc

# For merge_dicts and other cripts on this level:
sys.path.append(os.path.abspath('..'))

# For test:
sys.path.append(os.path.abspath('../tests'))
import merge_dicts_test

# -- Project information

project = 'ReConf 2023 X-As-Code'
copyright = '2023, PhilipPartsch'
author = 'PhilipPartsch'

release = '0.1'
version = '0.1.0'

# -- General configuration
on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx.ext.doctest',
    'sphinx_needs',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.test_reports',
    'sphinxcontrib.collections',
]

templates_path = ['_templates']

exclude_patterns = ['_tools/*',]

# -- intersphinx

#intersphinx_mapping = {
#    'python': ('https://docs.python.org/3/', None),
#    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
#}
#intersphinx_disabled_domains = ['std']


# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_css_files = ['custom.css']

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Collections
# For debugging it is possible to disable the clean up after sphinx-build
# collections_final_clean = False

collections = {}

# Fetch coverage data from coverage.json.
# Info: we collect the coverage over all test, so only one file has to be read in.
import json
# relative from here: _static/_external_data/coverage.json
test_coverage_file = os.path.join(os.path.dirname(__file__), '_static', '_external_data', 'coverage.json')

if os.path.exists(test_coverage_file):
    f = open(test_coverage_file)
    json_data = json.load(f)
    f.close()
    files = json_data['files']
    test_coverage = []
    for key, value in files.items():
       test_coverage_pro_file = {}
       coverage = value['summary']['percent_covered']
       test_coverage_pro_file['name'] = key.replace('/', '_').replace('\\', '_').replace('.py', '')
       test_coverage_pro_file['file'] = key
       test_coverage_pro_file['coverage'] = coverage
       test_coverage.append(test_coverage_pro_file)

    collections['test_coverage'] = {
                                    'driver': 'jinja',
                                    'source': os.path.join('templates', 'test_coverage.rst.template'),
                                    'target': os.path.join('test_coverage', 'test_coverage_for_{{name|lower}}.rst'),
                                    'data': test_coverage,
                                    'active': True,
                                    'multiple_files': True,
                                    }

# sphinxcontrib.plantuml configuration
local_plantuml_path = os.path.join(os.path.dirname(__file__), "_tools", "plantuml.jar")

if on_rtd:
    plantuml = f"java -Djava.awt.headless=true -jar {local_plantuml_path}"
else:
    plantuml = f"java -jar {local_plantuml_path}"

plantuml_output_format = 'svg'

# sphinx_needs configuration

needs_build_json = True

needs_id_regex = metamodel.needs_id_regex

needs_types = metamodel.needs_types

needs_extra_options = metamodel.needs_extra_options

needs_extra_links = metamodel.needs_extra_links

needs_services = metamodel.needs_services

needs_layouts = metamodel.needs_layouts

needs_functions = metamodel.needs_functions

needs_global_options = metamodel.needs_global_options

needs_warnings = metamodel.needs_warnings

