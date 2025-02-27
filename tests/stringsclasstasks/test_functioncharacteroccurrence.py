import unittest
import classWorks.stringsclasstasks.functioncharacteroccurrence as fco

class TestFunctionCharacterOccurrence(unittest.TestCase):
    def test_that_function_returns_correct_value(self):
        self.assertEqual(("o", 2), fco.get_character_occurrence("semicolon", "o"))
        self.assertEqual(("s", 1), fco.get_character_occurrence("semicolon","s"))

if __name__ == '__main__':
    unittest.main()
