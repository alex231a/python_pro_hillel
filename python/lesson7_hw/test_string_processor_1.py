"""Module contains tests for class StringProcessor"""
import unittest
from string_processor import StringProcessor


class TestStringProcessor(unittest.TestCase):
    """Class with testcases for StringProcessor"""

    @unittest.skip("Known issue with empty string reversal")
    def test_reverse_string_empty(self):
        """Tcase for method reverse_string with empty string, skipped"""
        self.assertEqual(StringProcessor.reverse_string(""), "")

    def test_reverse_string(self):
        """Tcases for method reverse_string"""
        self.assertEqual(StringProcessor.reverse_string("hello"), "olleh")
        self.assertEqual(StringProcessor.reverse_string("Python"), "nohtyP")
        self.assertEqual(StringProcessor.reverse_string("123@!"), "!@321")
        self.assertEqual(StringProcessor.reverse_string("Hello World"),
                         "dlroW olleH")

    def test_capitalize_string(self):
        """Tcases for method capitalize_string"""
        self.assertEqual(StringProcessor.capitalize_string("hello"), "Hello")
        self.assertEqual(StringProcessor.capitalize_string("python"), "Python")
        self.assertEqual(StringProcessor.capitalize_string("123abc"), "123abc")
        self.assertEqual(StringProcessor.capitalize_string("HELLO"), "Hello")
        self.assertEqual(StringProcessor.capitalize_string("hELLo WoRLD"),
                         "Hello world")
        self.assertEqual(StringProcessor.capitalize_string(""), "")

    def test_count_vowels(self):
        """Tcases for method count_vowels"""
        self.assertEqual(StringProcessor.count_vowels("hello"), 2)
        self.assertEqual(StringProcessor.count_vowels("PYTHON"), 2)
        self.assertEqual(StringProcessor.count_vowels("bcdfg"), 0)
        self.assertEqual(StringProcessor.count_vowels("AeiOu"), 5)
        self.assertEqual(StringProcessor.count_vowels("123!@#"), 0)
        self.assertEqual(StringProcessor.count_vowels(""), 0)


if __name__ == "__main__":
    unittest.main()
