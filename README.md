Overview  
========
[![Build Status](https://travis-ci.org/discogs/python-livingdocs.svg?branch=master)](https://travis-ci.org/discogs/python-livingdocs) [![Coverage Status](https://coveralls.io/repos/github/discogs/python-livingdocs/badge.svg?branch=master)](https://coveralls.io/github/discogs/python-livingdocs?branch=master) [![codecov](https://codecov.io/gh/discogs/python-livingdocs/branch/master/graph/badge.svg)](https://codecov.io/gh/discogs/python-livingdocs) [![PyPI](https://img.shields.io/pypi/v/livingdocs.svg?maxAge=2592000)](https://pypi.python.org/pypi/livingdocs) [![PyPI](https://img.shields.io/pypi/wheel/livingdocs.svg?maxAge=2592000)](https://pypi.python.org/pypi/livingdocs)

Using a Python BDD test runner like [behave], create living documentation from your BDD feature files. This library will create documents that contain up-to-date information about your BDD specs and helps generate a static site for your living documentation.

Current supported document types:

-   \*.mmark files (to be used by [Hugo])

Installation
------------

    pip install livingdocs

You should also install the Hugo binaries in order to generate your static site: https://gohugo.io/overview/installing/

Quick Start
-----------
Use the CLI command `livingdocs` to configure your Hugo site:
```
$ livingdocs
  Your site's title: <enter title>
  Your site's description: <enter description>
  ....
```
This will create a `livingdocs` folder in your root directory which will have a Hugo skeleton to create a static site.

Using a test runner like [behave], you can generate documents for each feature, scenario and step. In **environment.py**, you can use the DocsMaker to capture this information:

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


After you have successfully ran your tests, each test step will create its own documentation (and corresponding screenshot if you are using Selenium WebDriver). These new files will be placed in livingdocs/content/features. Once you have generated these files, we can build our static Hugo site with the following commands:

    $ cd livingdocs
    $ hugo

You will now have a static living docs site in the livingdocs/public directory.


Development
-----------

First create a virtual env, then to run the tests use:

    tox -e py27

License
-------

* BSD License

  [behave]: http://pythonhosted.org/behave/
  [Hugo]: https://gohugo.io/
