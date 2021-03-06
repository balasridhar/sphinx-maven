.. _`Sphinx commandline documentation`: http://sphinx.pocoo.org/man/sphinx-build.html?highlight=command%20line
.. _`Sphinx tag documentation`: http://sphinx.pocoo.org/markup/misc.html#tags
.. _`Jython`: http://www.jython.org/
.. _`rst2pdf manual`: http://lateral.netmanagers.com.ar/static/manual.pdf
.. _`GraphViz`: http://www.graphviz.org

Configuration
=============

The ``sphinx-maven`` plugin has these configuration options:

======================== ================================================================================================= ========================================
Parameter                Description                                                                                       Default value
======================== ================================================================================================= ========================================
``sourceDirectory``      The directory containing the documentation source.                                                ``${basedir}/src/site/sphinx``
``outputDirectory``      The directory where the generated output will be placed.                                          ``${project.reporting.outputDirectory}``
``outputName``           The base name used to create the report's output file(s).                                         ``Python-Sphinx``
``name``                 The name of the report.                                                                           ``Sphinx-Docs``
``description``          The description of the report.                                                                    ``Documentation via sphinx``
``builder``              The builder to use. See the `Sphinx commandline documentation`_ for a list of possible builders.  ``html``
``verbose``              Whether Sphinx should generate verbose output.                                                    ``true``
``warningsAsErrors``     Whether warnings should be treated as errors.                                                     ``false``
``force``                Whether Sphinx should generate output for all files instead of only the changed ones.             ``false``
``tags``                 Additional tags to pass to Sphinx. See the `Sphinx tag documentation`_ for more information.
``javaSphinxIncludeDir`` The directory containing the Java Source files.
``javaSphinxOutputDir``  The directory where the generated output will be placed.                                          ``${sourceDirectory}/javadocs/``
``javaSphinxVerbose``    Whether JavaSphinx should generate verbose output.                                                ``true``
``javaSphinxForce``      Whether JavaSphinx should generate output for all files instead of only the changed ones.         ``false``
======================== ================================================================================================= ========================================

Building PDFs
=============

The ``sphinx-maven`` plugin has experimental support for PDF generation. You'll turn it on
by using the pdf builder, e.g.::

    <plugin>
      <groupId>org.caltesting.maven</groupId>
      <artifactId>sphinx-maven-plugin</artifactId>
      <version>3.1.0</version>
      <configuration>
        <builder>pdf</builder>
        <outputDirectory>${project.reporting.outputDirectory}/pdf</outputDirectory>
      </configuration>
    </plugin>

You'll likely also have to add some additional configuration options to your ``conf.py``
file (usually in ``src/site/sphinx``) to tell the pdf builder what to do. At a minimum
you'll probably need to point it to the index page by adding this to the end::

    # -- Options for PDF output ---------------------------------------------------
    pdf_documents = [
        ('index', u'<file name>', u'<document name>', u'<author>'),
    ]

For additional options see the Sphinx section of the `rst2pdf manual`_.

Please note that alpha channels in the images (i.e. PNGs) are not supported, and will be replaced with
black pixels. This is most likely not what you want, so please don't use alpha channels in the images.

Building JavaDocs
==================

The ``sphinx-maven`` plugin has support for JavaDocs generation. You can turn it on by passing the necessary
arguments to the plugin configuration. e.g::

    <plugin>
      <groupId>org.caltesting.maven</groupId>
      <artifactId>sphinx-maven-plugin</artifactId>
      <version>3.1.0</version>
      <configuration>
          <javaSphinxVerbose>true</javaSphinxVerbose>
          <javaSphinxIncludeDir>
              <entry>${basedir}/src/main/java/</entry>
          </javaSphinxIncludeDir>
          <javaSphinxOutputDir>${basedir}/src/site/sphinx/javadoc/</javaSphinxOutputDir>
      </configuration>
    </plugin>

You will need to add some additional configuration options to your ``conf.py`` file
(usually in ``src/site/sphinx``) to tell Sphinx how to interpret the JavaSphinx generated *.rst* files.
You will have to add 'javasphinx' as an extension within the extension's list defined within ``conf.py``.

Please note that the output directory for *javasphinx* generated documentation should be within the *sourceDirectory*
folder structure specified for *Sphinx* configuration. So that *Sphinx* knows to also include these files as well when
generating the html/pdf output.

Using PlantUML
===============

The ``sphinx-maven`` plugin has support for converting uml described using *PlantUML* text format within a *.rst* file
to an image. It automatically references the image as part of the documentation in the appropriate place where the UML
was defined in the reStructured Text source file. As mentioned before, PlantUML requires **GraphViz** to be installed 
on the local machine. 

GraphViz
--------

GraphViz is a software package of opensource tools for drawing graphs described in DOT language scripts. More information
regarding `GraphViz`_ can be found in their website. Windows installer can be downloaded from the website and the package
is available as part of package management provided by the individual operating system vendor.

Remember this is required only for building html pages containing GraphViz generated images. You don't need this library 
for hosting the generated documentation.

PlantUML Config
-----------------

.. uml::

    @startuml
    state pluginBuildProcess {
        [*] -> buildJavaDocs
        buildJavaDocs: Using JavaSphinx
        buildJavaDocs -> buildSphinxDocs
        buildSphinxDocs: Using Sphinx and other extensions as needed.
        buildSphinxDocs -> [*]
    }
    @enduml

You will need to add some additional configuration options to your ``conf.py`` file (usually in ``src/site/sphinx``)
to tell Sphinx how to work with *.. uml::* directives. The steps involved are

* You will need to add 'sphinxcontrib-plantuml' as an extension within the extension's list defined within ``conf.py``
* You will also have to import an environment variable's value within ``conf.py``.::

    import os
    plantuml = os.getenv('plantuml')

Please note that it is absolutely necessary that the environment variable's value is assigned to the variable *plantuml*,
so that the extension works as expected.

A note on memory usage
======================

Sphinx is run via `Jython`_ which will generate lots of small classes for various Python constructs. This means that
the plugin will use a fair amount of memory, especially PermGen space (a moderate plugin run will likely use about 80mb
of PermGen space). Therefore we suggest to either run maven with at least 256mb of heap and 128mb of PermGen space, e.g.

    MAVEN_OPTS="-Xmx256m -XX:MaxPermSize=128m" mvn site


Sample Documentation Config
=============================

Sphinx looks at `conf.py` in the documentation source directory for building the final HTML or PDF file. This file contains 
some basic settings for getting the desired output. The configuration used for generating the plugin documentation is given
below:

.. code-block:: python

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
