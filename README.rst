========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - tests
      - |travis| |coveralls| |codecov|
    * - package
      - |version| |wheel| |supported-versions|

.. |travis| image:: https://travis-ci.org/dicogs/python-livingdocs.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/discogs/python-livingdocs

.. |coveralls| image:: https://coveralls.io/repos/discogs/python-livingdocs/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/discogs/python-livingdocs

.. |codecov| image:: https://codecov.io/github/discogs/python-livingdocs/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/discogs/python-livingdocs

.. |version| image:: https://img.shields.io/pypi/v/livingdocs.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/livingdocs


.. |wheel| image:: https://img.shields.io/pypi/wheel/livingdocs.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/livingdocs

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/livingdocs.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/livingdocs



.. end-badges

Using a Python BDD test runner like `behave`_, create living
documentation from your BDD feature files. This library will create
documents that contain up-to-date information about your BDD specs and
helps generate a static site for your living documentation.

Current supported document types:

-  \*.mmark files (to be used by `Hugo`_)

Installation
------------

::

    pip install livingdocs

You should also install the Hugo binaries in order to generate your
static site: https://gohugo.io/overview/installing/

Quick Start
-----------

Use the CLI command ``livingdocs`` to configure your Hugo site:

::

    $ livingdocs
      Your site's title: <enter title>
      Your site's description: <enter description>
      ....

This will create a ``livingdocs`` folder in your root directory which
will have a Hugo skeleton to create a static site.

Using a test runner like `behave`_, you can generate documents for each
feature, scenario and step. In **environment.py**, you can use the
DocsMaker to capture this information:

::

    from livingdocs.maker import DocsMaker

    def before_all(context):
        context.docs = DocsMaker('feature')

    def before_scenario(context, scenario):
        context.docs.start_scenario(context, scenario)

    def after_scenario(context, scenario):
        context.docs.end_scenario(context, scenario)

    def before_feature(context, feature):
        context.docs.start_feature(context, feature)

    def after_feature(context, feature):
        context.docs.end_feature(context, feature)

    def before_step(context, step):
        context.docs.start_step(context, step)

    def after_step(context, step):
        """
        if context.browser is an instance
        of Selenium Webdriver, then it will
        take a snapshot of this step.
        """
        context.docs.end_step(context, step)
        

Development
-----------

First create a virtual env, then to run the tests use:

::

    tox -e py27

License
-------

-  BSD License

.. _behave: http://pythonhosted.org/behave/
.. _Hugo: https://gohugo.io/
