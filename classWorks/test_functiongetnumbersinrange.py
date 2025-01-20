from unittest import TestCase
import functiongetnumbersinrange

class TestFunctionGetNumbersInRange(TestCase):
    def test_that_function_exists(self):
        functiongetnumbersinrange.get_numbers_in_range([12,15,19,21,50,70])
    
    def test_that_function_returns_correct_value(self):
        actual = functiongetnumbersinrange.get_numbers_in_range([12,15,19,21,50,70])
        expected = [21, 50]
        self.assertEqual(actual, expected)
