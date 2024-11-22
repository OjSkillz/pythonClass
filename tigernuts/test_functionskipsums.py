from unittest import TestCase
import functionskipsums

class TestFunctionSkipSum(TestCase):
    def test_that_function_skip_sum_exists(self):
        functionskipsums.get_total_sum([1,2,3,4])
        
    def test_that_function_skip_sum_returns_correct_value(self):
        self.assertEqual(functionskipsums.get_total_sum([1,2,3,4]), 30)
        self.assertEqual(functionskipsums.get_total_sum([1,2,3,4,5,6]), 105)
