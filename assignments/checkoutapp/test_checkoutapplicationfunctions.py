from unittest import TestCase
import checkoutapplicationfunctions
from datetime import datetime

class TestCheckOutApplicationFunctions(TestCase):
    def test_that_function_display_breaker_one_exists(self):
        checkoutapplicationfunctions.display_breaker_one()
    def test_that_function_display_breaker_two_exists(self):
        checkoutapplicationfunctions.display_breaker_two()
    
    def test_that_function_update_checkout_header_exists(self):
        checkoutapplicationfunctions.update_checkout_header("cashier_name", "customer_name")
    def test_that_function_update_checkout_header_returns_correct_value(self):
        self.assertEqual(checkoutapplicationfunctions.update_checkout_header("cashier's name", "customer's name"),  {
    "LOCATION": "312, HERBERT MACAULAY WAY, SABO, YABA, LAGOS.", "TEL 📞" : "032938287870", "Date" : datetime.now(), "Cashier" : "Cashier's Name", "Customer" : "Customer's Name"}) 
    
    
