from unittest import TestCase
import functionaverage

class TestFunctionAverage(TestCase):
    def test_that_function_average_exists(self):
        functionaverage.get_average([10,20,30,40])
    
    def test_that_function_average_returns_correct_value(self):
        self.assertEqual(functionaverage.get_average([10,20,30,40]), 25.0)
        self.assertEqual(functionaverage.get_average([1,2,3]), 2.0)
