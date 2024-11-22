from unittest import TestCase
import functioncountvowels

class TestFunctionCountVowels(TestCase):
    def test_that_function_count_vowels_exists(self):
        functioncountvowels.get_vowel_count("Hello")
        
    def test_that_function_count_vowels_returns_correct_value(self):
        actual = functioncountvowels.get_vowel_count("Hello")
        self.assertEqual(actual, 2)
        actual = functioncountvowels.get_vowel_count("Python is sweet")
        self.assertEqual(actual, 4)
