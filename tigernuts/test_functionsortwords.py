from unittest import TestCase
import functionsortwords

class TestFunctionSortWords(TestCase):
    def test_that_function_sort_words_exists(self):
        functionsortwords.sort_words(["apple", "cashews", "cherry"])
    
    def test_that_function_sort_words_returns_correct_value(self):
        self.assertEqual(functionsortwords.sort_words(["apple", "cashews", "pineapple",  "cherry"]), ["apple", "cherry", "cashews", "pineapple"])
