from unittest import TestCase
import functionevenelements

class TestFunctionOddElements(TestCase):
    def test_that_function_odd_elements_exits(self):
        functionevenelements.print_even_elements([1,3,5,6,8,10])
    
    def test_that_function_odd_elements_returns_correct_value(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        actual =  functionevenelements.print_even_elements(numbers)
        expected = [2,4,6,8]
        self.assertEqual(actual, expected)
