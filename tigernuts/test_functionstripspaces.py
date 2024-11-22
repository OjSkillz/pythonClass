from unittest import TestCase
import functionstripspaces

class TestFunctionStripSpaces(TestCase):
    def test_that_function_strip_spaces_exists(self):
        functionstripspaces.strip_spaces("hello, world")
    
    def test_that_function_strip_spaces_returns_correct_value(self):
        self.assertEqual(functionstripspaces.strip_spaces("hello   world"), "helloworld")
