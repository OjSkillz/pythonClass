from unittest import TestCase
import functionduplicateelement

class TestFunctionDuplicateElement(TestCase):
    def test_that_function_duplicate_element_exists(self):
        functionduplicateelement.check_duplicate([1,2,3,4,5,2])
        
    def test_that_function_duplicate_element_returns_correct_value(self):
        self.assertEqual(functionduplicateelement.check_duplicate([1,2,3,4,5,3]), True)
