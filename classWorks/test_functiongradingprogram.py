from unittest import TestCase
import functiongradingprogram

class TestFunctionGradingProgram(TestCase):
    def test_that_function_exists(self):
        functiongradingprogram.grade_students(student_scores = {
'Gloria': 88,
'Divine': 78,
'Esther': 65,
'Mercy': 75,
'Uzo': 71})

    def test_that_function_returns_correct_value(self):
        actual = functiongradingprogram.grade_students(student_scores = {
'Gloria': 88,
'Divine': 78,
'Esther': 65,
'Mercy': 75,
'Uzo': 71})
        expected =  {
'Gloria': "Exceeds Expectations",
'Divine': "Acceptable",
'Esther': "Fail",
'Mercy': "Acceptable",
'Uzo': "Acceptable"}
        self.assertEqual(actual, expected)
