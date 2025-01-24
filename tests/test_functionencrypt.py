import unittest
from encryption import functionencrypt

class TestFunctionEncrypt(unittest.TestCase):
    def test_that_function_encrypt_exists(self):
        functionencrypt.encrypt_text("Hello, World!")

    def test_that_function_encrypt_returns_correct_value(self):
        actual = functionencrypt.encrypt_text("Hello, World!")
        expected = "Uryyb, Jbeyq!"
        self.assertEqual(actual, expected)

        actual = functionencrypt.encrypt_text("Welcome, 123")
        expected = "Jrypbzr, 123"
        self.assertEqual(actual, expected)

    def test_that_function_encrypt_raises_exception_with_integer_input(self):
        actual = functionencrypt.encrypt_text(1)
        self.assertRaises(TypeError, actual)

    if __name__ == '__main__':
        unittest.main()
