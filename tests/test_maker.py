from mock import Mock
from livingdocs.maker import DocsMaker
import unittest
import shutil
import os

class TestDocsMaker(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        path = 'tmp'
        os.makedirs(path)
        os.chdir(path)

    @classmethod
    def tearDownClass(cls):
        os.chdir(os.pardir)
        shutil.rmtree('tmp', ignore_errors=True)

    @classmethod
    def setUp(cls):
        cls.section = 'feature'
        cls.maker = DocsMaker(cls.section)

    @classmethod
    def tearDown(cls):
        shutil.rmtree('livingdocs/content/feature', ignore_errors=True)

    def test_init(self):
        self.assertEqual(self.maker.section, self.section)
        self.assertIn(self.section, self.maker.output_dir)

    def test_fix_filename(self):
        filename = 'foo/bar.md'
        result = self.maker.fix_filename(filename)
        self.assertEquals(result, 'feature/bar')

    def test_start_feature(self):
        feature = Mock()
        feature.filename = 'foo/bar.md'
        feature.description = u'This is an example.'
        feature.tags = []
        context = Mock()
        self.maker.start_feature(context,feature)
        self.assertIn('This is an example.',self.maker.doc.getcontents())
        dir_name = self.maker.output_dir + '/' + self.maker.doc.path
        assert os.path.isdir(dir_name)

    def test_end_feature(self):
        feature = Mock()
        feature.filename = 'foo/bar.md'
        feature.description = u'This is an example.'
        feature.tags = []
        feature.scenarios = []
        scenario = Mock()
        scenario.name = 'Scenario 1'
        scenario.status = 'passed'
        feature.scenarios.append(scenario)
        context = Mock()
        self.maker.start_feature(context,feature)
        self.maker.end_feature(context, feature)
        num_scenarios = 'num_scenarios = "1"'
        num_scenarios_passing = 'num_scenarios_passing = "1"'
        self.assertIn(num_scenarios, self.maker.doc.header())
        self.assertIn(num_scenarios_passing, self.maker.doc.header())

    def test_start_scenario(self):
        feature = Mock()
        feature.filename = 'foo/bar.md'
        feature.description = u'This is an example.'
        feature.tags = []
        feature.scenarios = []
        scenario = Mock()
        scenario.name = 'Scenario 1'
        scenario.status = 'passed'
        feature.scenarios.append(scenario)
        context = Mock()
        self.maker.start_feature(context,feature)
        self.maker.start_scenario(context,scenario)
        scenario_line = '### %s' % scenario.name
        self.assertIn(scenario_line, self.maker.doc.getcontents())

    def test_end_step(self):
        feature = Mock()
        feature.filename = 'foo/bar.md'
        feature.description = u'This is an example.'
        feature.tags = []
        feature.scenarios = []
        scenario = Mock()
        scenario.name = 'Scenario 1'
        scenario.status = 'passed'
        feature.scenarios.append(scenario)
        context = Mock()

        def side_effect(arg):
            raise Exception('No browser')

        context.browser.driver.get_screenshot_as_file = side_effect

        self.maker.start_feature(context,feature)
        self.maker.start_scenario(context,scenario)
        step = Mock()
        step.keyword = u'foo'
        step.name = u'bar'
        step.status = u'passed'
        step.duration = 1.01
        self.maker.end_step(context, step)
        step_line = 'foo bar | passed | 1.01 | error capturing'
        self.assertIn(step_line, self.maker.doc.getcontents())

