from unittest import TestCase
import functioncheckanagram

class TestFunctionAnagramChecker(TestCase):
    def test_that_function_check_anagram_exists(self):
        functioncheckanagram.check_anagram_status("listen", "silent")
    
    def test_that_function_check_anagram_returns_expected_value(self):
        actual =  functioncheckanagram.check_anagram_status("listen", "silent")
        self.assertEqual(actual, True)
        actual =  functioncheckanagram.check_anagram_status("listeno", "silent")
        self.assertEqual(actual, False)
