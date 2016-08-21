from io import StringIO
from datetime import datetime


class HugoDoc(object):
    """
    A utility for creating hugo/markdown docs.
    """
    def __init__(self, title='', tags=[]):
        self.title = title
        self.meta = {}
        self.buff = StringIO()
        self.meta['tags'] = tags

    def header(self):
        lines = ['title = "%s"' % self.title]
        for key, val in self.meta.items():
            if isinstance(val, list):
                lines.append('%s = %s' % (key, val))
            else:
                lines.append('%s = "%s"' % (key, val))
        # auto date
        self.date = str(datetime.now().isoformat())
        lines.append('date = "%s"' % self.date)
        lines.insert(0, '+++')
        lines.append('+++')
        return '\n'.join(lines)

    def writeline(self, s=u''):
        self.buff.writelines(s)
        self.buff.writelines(u'\n')

    def getcontents(self):
        return self.header() + '\n\n' + self.buff.getvalue()
