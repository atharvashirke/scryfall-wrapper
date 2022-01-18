import unittest
import requests
import imghdr
from scryfall_wrapper.card_face import Card_Face
from scryfall_wrapper.utils import write_timestamped_file

class Card_FaceTestCase(unittest.TestCase):

    def setUp(self):
        response = requests.get("https://api.scryfall.com/cards/search", {"q": "Agadeem's Awakening"}).json()
        self.ag = Card_Face(response["data"][0]["card_faces"][0])
        
    def test_card(self):
        """
        Test if a Card_Face object can be made.
        """
        self.assertIsInstance(self.ag, Card_Face)

    def test_image(self):
        """
        Test if image method returns valid image file
        """
        image = write_timestamped_file("dev/", self.ag.image(), ".jpg")
        self.assertEquals(imghdr.what(image), "jpeg")

if __name__ == "__main__":
    unittest.main()