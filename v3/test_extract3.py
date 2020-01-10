import unittest,extract3

class ExtractTestCase(unittest.TestCase):

    def test_extract_with_by_key(self):
        self.assertEqual(extract3.extract('root/section/item2', '{"root": {"section": {"item1": "value1", "item2": "value2"}}}'), 'value2')
