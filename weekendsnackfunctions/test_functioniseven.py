from unittest import TestCase
import functioniseven

class TestFunctionIsEven(TestCase):
    def test_that_function_is_even_exists(self):
        functioniseven.is_even(4)
    
    def test_that_function_is_even_returns_correct_value_with_even_input(self):
        self.assertEqual(functioniseven.is_even(4), True)
    
    def test_that_function_is_even_returns_correct_value_with_odd_input(self):
        self.assertEqual(functioniseven.is_even(5), False)
        
