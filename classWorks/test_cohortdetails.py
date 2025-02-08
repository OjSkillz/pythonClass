from unittest import TestCase
import cohortdetails

class TestFunction (TestCase):
	def test_that_function_exists(self):
	    cohortdetails.zip_details(["C24" , "C23" , "C22", "C21", "C20"], ["4 months", "5 months", "6 months", "7 months", "8 months"])
	
	def test_that_function_returns_correct_value(self):
	    actual = cohortdetails.zip_details(["C24" , "C23" , "C22", "C21", "C20"], ["4 months", "5 months", "6 months", "7 months", "8 months"])
	    expected = {"C24" : "4 months", "C23" : "5 months", "C22" : "6 months", "C21" : "7 months", "C20" : "8 months"}
	    self.assertEqual(actual, expected)
		
	
