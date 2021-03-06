# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# -*- coding: utf-8 -*-

import sys, os

needs_sphinx = '1.0'

extensions = ['sphinx.ext.autodoc', 'rst2pdf.pdfbuilder', 'javasphinx', 'sphinxcontrib.plantuml']

# ---------- Options for PlantUML Integration ----------------
plantuml = os.getenv('plantuml')

templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'

project = u'Sphinx-Maven'
copyright = u'2015, Bala Sridhar'

version = '3.1.0'
release = '3.1.0'

exclude_trees = ['.build']

add_function_parentheses = True
pygments_style = 'trac'
master_doc = 'index'

# -- Options for HTML output ------------------

# Bootstrap Theme
#sys.path.append(os.path.abspath('_themes'))
#html_theme_path = ["_themes"]
#html_static_path = ['_static']
#html_theme = 'bootstrap'

html_theme = 'pyramid'
html_short_title = "Sphinx-Maven"
html_use_smartypants = True
html_use_index = True
htmlhelp_basename = 'sphinxmavendoc'

html_sidebars = {
    'index': ['globaltoc.html', 'relations.html', 'sidebarintro.html', 'searchbox.html'],
    '**': ['globaltoc.html', 'relations.html', 'sidebarintro.html', 'searchbox.html']
}

# -- Options for PDF output ---------------------------------------------------
pdf_documents = [
    ('index', u'Sphinx-Maven-Plugin', u'Sphinx-Maven-Plugin', u'Bala Sridhar'),
]

# -------- Options for JavaSphinx -------------------------------
javadoc_url_map = {
    'java': ('http://docs.oracle.com/javase/7/docs/api/', 'javadoc'),
    'javax': ('http://docs.oracle.com/javase/7/docs/api/', 'javadoc'),
    'org.xml': ('http://docs.oracle.com/javase/7/docs/api/', 'javadoc'),
    'org.w3c': ('http://docs.oracle.com/javase/7/docs/api/', 'javadoc'),
    'org.apache.maven.plugin': ('http://maven.apache.org/plugin-tools/maven-plugin-plugin/apidocs/', 'javadoc'),
    'org.apache.maven.reporting': ('https://maven.apache.org/shared/maven-reporting-api/apidocs/', 'javadoc'),
    'org.codehaus.doxia.sink': ('http://maven.apache.org/doxia/doxia/doxia-sink-api/apidocs/', 'javadoc')
}
