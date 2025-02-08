from unittest import TestCase
import countsigns

class TestFunctionCountSigns(TestCase) :
    def test_that_function_count_signs_exists(self):
        countsigns.count_signs([15,34,-1,24,-7,9])
    
    def test_that_function_count_signs_returns_correct_value(self) :
        actual = countsigns.count_signs([15,34,-1,24,-7,9])
        expected = f"Positive : 4 \nNegative : 2"
        self.assertEqual(actual, expected)
