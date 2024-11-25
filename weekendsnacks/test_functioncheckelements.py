from unittest import TestCase
import functioncheckelements

class TestFunctionCheckElements(TestCase):
    def test_that_function_check_elements_exists(self):
        functioncheckelements.check_elements([1,3,4,5,6], 2)
    
    def test_that_function_sum_with_loops_returns_correct_value(self):
        actual = functioncheckelements.check_elements([1,3,4,5,6], 2)
        expected = False
        self.assertEqual(actual, expected)
