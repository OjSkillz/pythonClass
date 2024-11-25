from unittest import TestCase
import functionreversestring

class TestFunctionReverseString(TestCase):
    def test_that_function_reverse_string_exists(self):
        functionreversestring.reverse_string("hello")
