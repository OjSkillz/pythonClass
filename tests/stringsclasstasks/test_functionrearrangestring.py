import unittest
import classWorks.stringsclasstasks.functionrearrangestring as frs

class TestFunctionRearrangeString(unittest.TestCase):
    def test_that_function_returns_word_arranged_with_uppercase_letters_first(self):
        sample = "sEmIColOn"
        output = "EICOsmoln"

        actual = frs.rearrange(sample)
        self.assertEqual(output, actual)

        sample = "aBcDeFg"
        output = "BDFaceg"

        actual = frs.rearrange(sample)
        self.assertEqual(output, actual)

if __name__ == '__main__':
    unittest.main()
