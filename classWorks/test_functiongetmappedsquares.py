from unittest import TestCase
import functiongetmappedsquares

class TestFunctionGetMappedSquares(TestCase) :
    def test_that_function_exists(self):
        functiongetmappedsquares.get_mapped_squares(4)
    
    def test_that_function_returns_correct_value(self):
     actual = functiongetmappedsquares.get_mapped_squares(5)
     expected = {1:5, 2:25}
     self.assertEqual(actual, expected)
    
