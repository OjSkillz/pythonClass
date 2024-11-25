from unittest import TestCase
import functionmergeinputsalternatingly

class TestFunctionMergeInputs(TestCase):
    def test_that_function_merge_inputs_exists(self):
        functionmergeinputsalternatingly.merge_inputs_alternatingly(["a","b","c"],["1","2","3"])
    
    def test_that_function_merge_inputs_returns_correct_value(self):
        self.assertEqual(functionmergeinputsalternatingly.merge_inputs_alternatingly(["a","b","c"],["1","2","3"]), ["a","1","b","2","c","3"])
