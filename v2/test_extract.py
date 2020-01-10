import unittest,extract

class ExtractTestCase(unittest.TestCase):

    def test_extract_with_by_key(self):
        self.assertEquals(extract.extract('root/section/item2', '{"root": {"section": {"item1": "value1", "item2": "value2"}}}'), 'value2')
        self.assertEquals(extract.extract('a/b/c','{"a":{"b":{"c":"d"}}}'), 'd')
