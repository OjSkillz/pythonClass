from unittest import TestCase
import populationApp

class TestPopulationApp(TestCase):
    def test_that_app_exists(self):
        populationApp.get_population("USA", "California")
        
    def test_that_function_works(self):
        actual = populationApp.get_population("USA", "California")
        expected = "Los Angeles: 40000000\nSan Francisco: 870000\n"
        self.assertEqual(actual, expected)
        
  
