from unittest import TestCase
import functionpalindrome

class TestFunctionPalindrome(TestCase):
    def test_that_function_palindrome_exists(self):
        functionpalindrome.check_palindrome("madam")
    
    def test_that_function_palindrome_returns_correct_value(self):
        self.assertEqual(functionpalindrome.check_palindrome("madam"), True)
        self.assertEqual(functionpalindrome.check_palindrome("dad"), True)
        self.assertEqual(functionpalindrome.check_palindrome("hello"), False)
