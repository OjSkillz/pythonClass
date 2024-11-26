from unittest import TestCase
import functionfactorof

class TestFunctionFactorOf(TestCase):
    def test_that_function_factor_of_exists(self):
        functionfactorof.factor_of(10)
    
    def test_that_function_factor_of_returns_correct_value(self):
        actual = functionfactorof.factor_of(10)
        expected = 4
        self.assertEqual(actual, expected)
