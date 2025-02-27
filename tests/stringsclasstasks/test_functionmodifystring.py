import unittest
import classWorks.stringsclasstasks.functionmodifystring as modify_string

class TestFunctionModifyString(unittest.TestCase):
    def test_that_function_exists(self):
        modify_string.modify_string("helloo", "ce")

    def test_that_function_returns_modifier_in_middle_of_string_when_string_can_be_divided_equally(self):
        string = "helloo"
        modifier = "ce"
        expected = "helceloo"
        actual = modify_string.modify_string(string, modifier)

        self.assertEqual(actual,expected)

    def test_that_function_returns_modifier_at_the_end_of_string_when_string_can_not_be_divided_equally(self):
        string = "joy"
        modifier = "ce"
        expected = "joyce"
        actual = modify_string.modify_string(string, modifier)
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()
