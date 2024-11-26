from unittest import TestCase
import functionispalindrome

class TestFunctionIsPalindrome(TestCase):
    def test_that_function_is_palindrome_exists(self):
        functionispalindrome.is_palindrome(54145)
    
    def test_that_function_is_palindrome_returns_correct_value(self):
        actual = functionispalindrome.is_palindrome(54145)
        expected = True
        self.assertEqual(actual, expected)
        actual = functionispalindrome.is_palindrome(54146)
        expected = False
        self.assertEqual(actual, expected)
    

