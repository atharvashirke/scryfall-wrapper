"""
Test file for utils functions 
"""
import unittest
from scryfall_wrapper import utils
from datetime import datetime

class UtilsTestCase(unittest.TestCase):

    def setUp(self):
        self.method = "cards/search"
        self.query = {"q": "Imoti, Celebrant of Bounty"}
        self.data = utils.get_request(self.method, self.query)
    
    def test_basic_request(self):
        """
        Test if a basic get request can be made
        """
        self.assertIsNotNone(self.data)

    def test_response_dict(self):
        """
        Test if dict output is accessible
        """
        self.assertIsInstance(self.data, dict)
    
    def test_date(self):
        """
        Test if date function creates proper date
        """
        date = utils.str_to_date("2021-06-18")
        self.assertEquals(date, datetime(2021, 6, 18))

if __name__ == "__main__":
    unittest.main()