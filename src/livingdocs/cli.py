"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -mlivingdocs` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``livingdocs.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``livingdocs.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
import click
from static_site import StaticSite


@click.command()
@click.option('--title', prompt='Your site\'s title',
              help='The name of your site.')
@click.option('--description', prompt='Your site\'s description',
              help='A short description of your site.')
@click.option('--baseurl', default='http://localhost:1313',
              help='The base url of your site.')
def cli(title, description, baseurl):
    click.echo('Building Living Docs Site')
    site = StaticSite(title=title, description=description, baseurl=baseurl)
    site.create()
