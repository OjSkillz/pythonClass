from unittest import TestCase
import functionmergeinputs

class TestFunctionMergeInputs(TestCase):
    def test_that_function_merge_inputs_exists(self):
        functionmergeinputs.merge_inputs([3,4,9,10],[1,5,7,8])
    
    def test_that_function_merge_inputs_returns_correct_value(self):
        self.assertEqual(functionmergeinputs.merge_inputs([3,4,9,10,90],[1,5,7,8,12]), [1,3,4,5,7,8,9,10,12,90])
