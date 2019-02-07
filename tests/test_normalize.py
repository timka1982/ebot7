# https://docs.python.org/3/library/unittest.html
import unittest
from .context import refactor

class TestNormalizeFunction(unittest.TestCase):

    def test_remove_punctuation(self):
        self.assertEqual(refactor.normalize('a.b.'), 'ab')

    def test_lower_case(self):
        self.assertEqual(refactor.normalize('AbBa'), 'abba')

    def test_lower_replace_numbers_english(self):
        self.assertEqual(refactor.normalize('123', 'en'), 'one two three')
if __name__ == '__main__':
    unittest.main()
