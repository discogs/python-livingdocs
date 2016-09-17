from livingdocs.static_site import StaticSite
import unittest
import shutil
import os


class TestStaticSite(unittest.TestCase):

    def test_obj(self):
        """
        Check that the title, description
        and baseurl are correct.
        """
        site = StaticSite(title="MyHub",
                          description="Place for my stuff",
                          baseurl="localhost:1313")
        self.assertIn("MyHub", site.title)
        self.assertIn("Place for my stuff", site.description)
        self.assertIn("localhost:1313", site.baseurl)

    def test_create(self):
        """
        Check that site files and directories
        are created.
        """
        os.makedirs('tmp')
        os.chdir('tmp')
        site = StaticSite()
        site.create()
        self.assertTrue(os.path.isdir('livingdocs/layouts'))
        self.assertTrue(os.path.isdir('livingdocs/static'))
        self.assertTrue(
            os.path.exists(os.path.join(os.getcwd(), 'livingdocs/config.toml')))
        os.chdir(os.pardir)
        shutil.rmtree('tmp', ignore_errors=True)
