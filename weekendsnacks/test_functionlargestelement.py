from unittest import TestCase
import functionlargestelement

class TestFunctionLargest(TestCase):
    def test_that_function_largest_element_exists(self):
        functionlargestelement.get_largest([2,5,7,])
    
    def test_that_function_largest_element_returns_correct_value(self):
        self.assertEqual(functionlargestelement.get_largest([2,5,7,]), 7)
