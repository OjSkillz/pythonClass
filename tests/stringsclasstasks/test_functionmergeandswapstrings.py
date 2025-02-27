import unittest
import classWorks.stringsclasstasks.functionmergeandswapstrings as fms

class TestFunctionMergeAndSwapStrings(unittest.TestCase):
    def test_that_function_exists(self):
        fms.merge_and_swap("abc", "xyz")

    def test_that_function_returns_correct_value(self):
        actual = fms.merge_and_swap("abc", "xyz")
        expected = "xyc abz"
        self.assertEqual(actual, expected)

        actual = fms.merge_and_swap("123", "456")
        expected = "453 126"
        self.assertEqual(actual, expected)
if __name__ == '__main__':
    unittest.main()
