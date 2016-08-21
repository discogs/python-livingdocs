from livingdocs.hugo_doc import HugoDoc
import unittest

class TestHugoDoc(unittest.TestCase):

    def test_header(self):
        """
        Check that the title, tags and
        date are correct.
        """
        doc = HugoDoc(title="PageOne")
        header_partial = '+++\ntitle = "PageOne"\n'
        doc_header = doc.header()
        self.assertIn(header_partial, doc_header)
        empty_tags = 'tags = []'
        self.assertIn(empty_tags, doc_header)
        datestr = str(doc.date)
        self.assertIn(datestr, doc_header)

    def test_meta_data(self):
        """
        Check that metadata can be
        added to header.
        """
        doc = HugoDoc(title="PageTwo")
        doc.meta['foo'] = 'bar'
        header_str = 'foo = "bar"\n'
        self.assertIn(header_str, doc.header())

    def test_writeline(self):
        """
        Check that writeline adds
        content to buffer.
        """
        doc = HugoDoc(title="PageThree")
        line = u'All original junglist massive'
        doc.writeline(line)
        self.assertIn(line, doc.getcontents())

