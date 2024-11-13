from unittest import TestCase
import functiondiscount

class TestDiscountFunction(TestCase):
    def test_that_discount_function_exists(self):
        functiondiscount.get_discount(5, 15)
    
    def test_that_discount_function_returns_correct_value(self):
        actual = functiondiscount.get_discount(150, 15)
        expected = 127.5
        self.assertEqual(actual, expected)
    
    def test_that_discount_function_rounds_float_results_to_two_decimal_places(self):
        actual = functiondiscount.get_discount(150.25, 15.5)
        expected = 126.96
        self.assertEqual(actual, expected)
        actual = functiondiscount.get_discount(100.5, 16.5)
        expected = 83.92
        self.assertEqual(actual, expected)
    
    def test_that_discount_function_returns_an_error_message_when_any_input_is_zero(self):
        functiondiscount.get_discount(0, 0) 
        self.assertRaises(TypeError, functiondiscount.get_discount(0, 0))
    

    
