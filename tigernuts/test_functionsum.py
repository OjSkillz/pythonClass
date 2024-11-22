from unittest import TestCase
import functionsum

class TestFunctionSum(TestCase):
    def test_that_function_sum_exists(self):
        functionsum.get_sum([2,3,4,5,6])
    
    def test_that_function_sum_returns_correct_value_with_list_input(self):
        actual = functionsum.get_sum([1,2,3,4,5,6])
        expected = 12
        self.assertEqual(actual, expected)
        actual = functionsum.get_sum([10,24,3,4,5,6])
        expected = 44
        self.assertEqual(actual, expected)
