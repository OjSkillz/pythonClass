import unittest
import classWorks.functioncharacterfrequency as cf

class TestFunctionCharacterFrequency(unittest.TestCase):
    def test_that_function_exists(self):
        cf.get_character_frequency("semicolon.africa")

    def test_that_function_returns_correct_value(self):
        sample_string = "semicolon.africa"
        character_frequencies = {'s':1,'e':1,'m':1,'i':2,'c':2,'o':2,'l':1,'n':1,'.':1,'a':2,'f':1,'r':1}

        actual = cf.get_character_frequency(sample_string)

        self.assertEqual(character_frequencies, actual)



if __name__ == '__main__':
    unittest.main()
