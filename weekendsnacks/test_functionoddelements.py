from unittest import TestCase
import functionoddelements

class TestFunctionOddElements(TestCase):
    def test_that_function_odd_elements_exits(self):
        functionoddelements.print_odd_elements([1,3,5,6,8,10])
    
    def test_that_function_odd_elements_returns_correct_value(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        actual =  functionoddelements.print_odd_elements(numbers)
        expected = [1,3,5,7,9]
        self.assertEqual(actual, expected)
