import shutil
import os


class StaticSite(object):

    def __init__(self, title='', description='', baseurl=''):
        self.title = title
        self.description = description
        self.baseurl = baseurl

    def create(self, path="livingdocs"):
        """
        Scaffolds a simple Hugo static site build.
        """
        os.makedirs(path)
        dirs = ['layouts', 'static']
        for d in dirs:
            template = u'site_files/%s' % d
            directory = os.path.join(os.path.dirname(__file__), template)
            self.copy(directory,
                      u'livingdocs/%s' % d)
            print(u'added %s' % d)
        self.make_config()

    def make_config(self):
        """
        Creates config.toml
        """
        with open(u"livingdocs/config.toml", "a") as cfg:
            cfg.write(u"baseurl = '%s'\n" % self.baseurl)
            cfg.write(u"title = '%s'\n" % self.title)
            cfg.write(u"description = '%s'\n" % self.description)
            cfg.write(u"languageCode = 'en-us'\n")
            cfg.write(u"SectionPagesMenu = 'main'\n")
            cfg.write(u"\n")
            cfg.write(u"[taxonomies]\n")
            cfg.write(u"tag = \"tags\"\n")

    def copy(self, src, dest):
        """
        Copies both directories and files to a
        given destination.
        """
        shutil.copytree(src, dest)
