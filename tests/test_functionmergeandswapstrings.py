import unittest
import classWorks.functionmergeandswapstrings as fms

class TestFunctionMergeAndSwapStrings(unittest.TestCase):
    def test_that_function_exists(self):
        fms.merge_and_swap("abc", "xyz")

    def test_that_function_returns_correct_value(self):
        actual = fms.merge_and_swap("abc", "xyz")
        expected = "xyc abz"
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
