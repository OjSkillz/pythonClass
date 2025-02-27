import unittest
import classWorks.stringsclasstasks.functionremovespecialcharacters as frs

class TestFunctionRemoveSpecialCharacters(unittest.TestCase):
    def test_that_function_works(self):
        self.assertEqual("hello", frs.remove_special_characters("he,ll.o"))  # add assertion here


if __name__ == '__main__':
    unittest.main()
