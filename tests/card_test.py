import unittest
from scryfall_wrapper.card import Card
from scryfall_wrapper.utils import write_timestamped_file
from scryfall_wrapper.card_set import Card_Set
import imghdr

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
        b_card = Card("Mox Sapphire") # No foil mox sapphire
        self.assertIsNone(b_card.price(foil=True))

    def test_conv_price(self):
        """
        Test if price method returns a converted price
        """
        eur = self.a_card.price(conv_to="EUR")
        self.assertEqual(eur != self.a_card.price(), True)

    def test_reprints(self):
        """
        Test if reprints method returns a list of 
        card objects with proper length
        """
        b_card = Card("Mox Sapphire")
        reprints = b_card.reprints()
        self.assertEqual(len(reprints), 10)

    def test_legality(self):
        """
        Test if legality method returns expected
        output
        """
        self.assertEqual(self.a_card.legality(), "False")

    def card_set_test(self):
        """
        Test if card_set method returns output of
        expected type and attributes
        """
        cmr = self.a_card.card_set()
        self.assertIsInstance(cmr, Card_Set)
        self.assertEqual(cmr.name, "Commander Legends")

    
    def test_image(self):
        """
        Test if image method returns valid image file
        """
        image = write_timestamped_file("dev/", self.a_card.image(), ".jpg")
        self.assertEquals(imghdr.what(image), "jpeg")

    def test_str(self):
        """
        Test Card str method returns desired output
        """
        self.assertEqual(str(self.a_card), "Imoti, Celebrant of Bounty (CMR)")
        
    def test_repr(self):
        """
        Test Card reor method returns desired output
        """
        self.assertEqual(self.a_card.__repr__(), "Imoti, Celebrant of Bounty (CMR)" + " [ID:8afceb13-877a-4256-9ba6-851b6924ffd9]")

if __name__ == "__main__":
    unittest.main()