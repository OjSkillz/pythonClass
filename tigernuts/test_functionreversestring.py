from unittest import TestCase
import functionreversestring

class TestFunctionReverseString(TestCase):
    def test_that_function_reverse_string_exists(self):
        functionreversestring.reverse_string("hello")
    
    def test_that_function_reverse_string_returns_correct_value(self):
        self.assertEqual(functionreversestring.reverse_string("hello"), "olleh")
        self.assertEqual(functionreversestring.reverse_string("cognate"), "etangoc")
