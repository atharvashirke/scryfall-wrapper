import unittest
from scryfall_wrapper.card import Card

class CardTestCase(unittest.TestCase):

    def setUp(self):
        self.a_card = Card("Imoti, Celebrant of Bounty")
        
    
    def test_card(self):
        """
        Test if a card object can be made.
        """
        self.assertIsInstance(self.a_card, Card)

    def test_none_card(self):
        """
        Test if None is returned when requesting
        a card that does not exist.
        """
        self.assertRaises(ValueError, Card, "jdsfahjsdhfasjdh")

    def test_price(self):
        """
        Test if price method returns expected type
        """
        self.assertIsInstance(self.a_card.price(), float)

if __name__ == "__main__":
    unittest.main()