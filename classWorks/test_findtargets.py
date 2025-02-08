from unittest import TestCase
import findtarget

class TestFindTargets(TestCase) : 
    def test_that_function_find_target_exists(self) :
        findtarget.find_target([12, 17, 24, 32, 14], 24)
    
    def test_that_function_find_target_returns_correct_value(self) :
        actual = findtarget.find_target([12, 17, 24, 32, 14], 32)
        expected = 3
        self.assertEqual(actual, expected)
    
    def test_that_function_find_target_returns_correct_value_for_non_existent_target(self):
        actual = findtarget.find_target([12, 17, 24, 32, 14], 54)
        expected = "not found"
        self.assertEqual(actual, expected)
