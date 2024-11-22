from unittest import TestCase
import functioncapitalize

class TestFunctionCapitalize(TestCase):
    def test_that_function_capitalize_exists(self):
        functioncapitalize.capitalize_first_letter(["apple", "banana", "cherry"])
    
    def test_that_function_capitalize_returns_correct_value(self):
        self.assertEqual(functioncapitalize.capitalize_first_letter(["apple", "banana", "cherry"]), ["Apple", "Banana", "Cherry"])
        self.assertEqual(functioncapitalize.capitalize_first_letter(["come", "go", "remain"]), ["Come", "Go", "Remain"])

