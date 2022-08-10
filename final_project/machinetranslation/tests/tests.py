
#final linted version of tests.py

""" Testing translator module """
import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    """ Test the translator code """

    def test_english_to_french_bad(self):
        """ test english to french translation with blank text """
        self.assertEqual(english_to_french(""), "Blank text - Code: 400")

    def test_english_to_french(self):
        """ test english to french translation with non-blank text """
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english_bad(self):
        """ test the french to english translation with blank text"""
        self.assertEqual(french_to_english(""), "Blank text - Code: 400")

    def test_french_to_english(self):
        """ test the french to english translation with non-blank text"""
        self.assertEqual(french_to_english("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()
