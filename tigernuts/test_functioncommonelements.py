from unittest import TestCase
import functioncommonelements

class TestFunctionCommon(TestCase):
    def test_that_function_common_elements_exists(self):
        functioncommonelements.check_common([1,2,3],[3,4,5])
    
    def test_that_function_common_returns_correct_value(self):
        actual = functioncommonelements.check_common([1,2,3,4],[3,4,5])
        expected = [3,4]
        self.assertEqual(actual, expected)
