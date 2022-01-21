import unittest
import requests
from scryfall_wrapper.card_set import Card_Set

class Card_Set_TestCase(unittest.TestCase):

    def setUp(self):
        self.a_set = Card_Set("ELD")

    def test_card_set(self):
        """
        Test if a Card_Set object can be made.
        """
        self.assertIsInstance(self.a_set, Card_Set)

    def cards_test(self):
        """
        Test if cards method returns the correct number
        of cards in the set
        """
        self.assertEqual(len(self.a_set.cards()), 397)

    def str_test(self):
        """
        Test if str method returns expected output
        """
        self.assertEqual(str(self.a_set), "Throne of Eldraine (ELD)")

    def repr_test(self):
        """
        Test if repr method returns expected output
        """
        self.assertEqual(self.a_set.__repr__(), "Card_Set Object (ELD)")

if __name__ == "__main__":
    unittest.main()