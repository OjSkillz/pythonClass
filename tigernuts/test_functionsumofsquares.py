from unittest import TestCase
import functionsumofsquares

class TestFunctionSumOfSquares(TestCase):
    def test_that_function_sum_of_squares_exists(self):
        functionsumofsquares.sum_squares([1,2,3,4])
    
    def test_that_function_sum_of_squares_returns_correct_value(self):
        actual =  functionsumofsquares.sum_squares([1,2,3,4])
        expected = 30
        self.assertEqual(actual, expected)
