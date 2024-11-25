from unittest import TestCase
import functionsumwithloops

class TestFunctionSumWithLoops(TestCase):
    def test_that_function_sum_with_loops_exists(self):
        functionsumwithloops.sum_lists_with_loops([100, 200, 300, 400, 500])
    
    def test_that_function_sum_with_loops_returns_correct_value(self):
        numbers =[100, 200, 300, 400, 500]
        actual = functionsumwithloops.sum_lists_with_loops([100, 200, 300, 400, 500])
        expected = [1500, 1500]
        self.assertEqual(actual, expected)
