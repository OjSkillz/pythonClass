from unittest import TestCase
import functiongetevennumbers

class TestFunctionGetEvenNumbers(TestCase) :
    def test_that_function_get_even_numbers_exist(self):
        functiongetevennumbers.get_even_numbers("73H2AdSdf439dm")
        
    def test_that_function_returns_correct_value(self):
        actual = functiongetevennumbers.get_even_numbers("73H2AdSdf439dm")
        expected = [2,4]
        self.assertEqual(actual, expected)
