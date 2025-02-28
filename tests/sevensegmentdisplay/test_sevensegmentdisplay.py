import unittest

from sevensegmentdisplay.sevensegmentdisplay import display_output_for

class TestSevenSegmentDisplay(unittest.TestCase):
    def test_that_function_exists(self):
        display_code = "10111011"
        display_output_for(display_code)

    def test_that_function_returns_appropriate_value(self):
        display_code = "11111111"
        expected = '''
#####
#   #
#   #
#####
#   #
#   #
#####
'''
        actual = display_output_for(display_code)
        self.assertEqual(expected, actual)

    def test_that_display_code_must_be_eight_digits_long(self):
        display_code = "111"
        self.assertRaises(ValueError, display_output_for, display_code)

        display_code = "111111111"
        self.assertRaises(ValueError, display_output_for, display_code)

    def test_that_nothing_displays_when_last_digit_of_display_code_is_0(self):
        display_code = "11111110"
        expected = '''
     
     
     
     
     
     
     
'''
        self.assertEqual(expected, display_output_for(display_code))

    def test_that_display_code_can_only_contain_digits(self):
        display_code = "11a11111"
        self.assertRaises(TypeError, display_output_for, display_code)

        display_code = "1@1111.1"
        self.assertRaises(TypeError, display_output_for, display_code)

    def test_that_display_code_can_only_contain_0s_and_1s(self):
        display_code = "11211111"
        self.assertRaises(ValueError, display_output_for, display_code)


if __name__ == '__main__':
    unittest.main()
