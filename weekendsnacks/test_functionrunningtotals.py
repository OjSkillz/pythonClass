from unittest import TestCase
import functionrunningtotals

class TestFunctionRunningTotals(TestCase):
    def test_that_function_running_totals_exists(self):
        functionrunningtotals.get_running_totals([100, 200, 300, 400, 500])
    
    def test_that_function_running_totals_returns_correct_value(self):
        numbers =[100, 200, 300, 400, 500]
        actual =    functionrunningtotals.get_running_totals(numbers)
        expected = [100, 300, 600, 1000, 1500]
        self.assertEqual(actual, expected)
