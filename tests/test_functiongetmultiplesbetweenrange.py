import unittest
from getmultiplesbetweenrange import functiongetmultiplesbetweenrange

class TestFunctionGetMultiplesBetweenRange(unittest.TestCase):
    def test_that_function_returns_correct_values(self):
        a = 1
        b = 10
        c = 2

        self.assertEqual([2,4,6,8,10], functiongetmultiplesbetweenrange.get_multiples_between(a,b,c))  # add assertion here

    def test_that_range_values_cannot_be_negative(self):
        a = -1
        b = 10
        c = 2

        self.assertRaises(ValueError, functiongetmultiplesbetweenrange.get_multiples_between, a, b, c)

        a = 1
        b = 10
        c = -2

        self.assertRaises(ValueError, functiongetmultiplesbetweenrange.get_multiples_between, a, b, c)

    def test_that_factor_cannot_be_zero(self):
        a = 1
        b = 10
        c = 0
        self.assertRaises(ValueError, functiongetmultiplesbetweenrange.get_multiples_between, a, b, c)

    def test_that_function_returns_correct_values_with_different_range(self):
        a = 3
        b = 15
        c = 3
        self.assertEqual([3,6,9,12,15], functiongetmultiplesbetweenrange.get_multiples_between(a,b,c))

    def test_that_lower_range_value_cannot_be_greater_than_higher_range_value(self):
        a = 10
        b = 5
        c = 2
        self.assertRaises(ValueError, functiongetmultiplesbetweenrange.get_multiples_between, a, b, c)

    def test_that_range_cannot_be_zero(self):
        a = 10
        b = 10
        c = 2
        self.assertRaises(ValueError, functiongetmultiplesbetweenrange.get_multiples_between, a, b, c)

if __name__ == '__main__':
    unittest.main()
