Overview
========

Using a Python BDD test runner like [behave], create living documentation from your BDD feature files. This library will create documents that contain up-to-date information about your BDD specs.

Current supported document types:

-   \*.mmark files (to be used by [Hugo])

Installation
------------

    pip install livingdocs

Quick Start
-----------

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

Development
-----------

First create a virtual env, then to run the tests use:

    tox -e py27

License
-------

* BSD License

  [behave]: http://pythonhosted.org/behave/
  [Hugo]: https://gohugo.io/
