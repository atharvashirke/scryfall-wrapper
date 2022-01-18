"""
Class file representing the face of a card.
"""
import requests

class Card_Face():

    object = 'Card_Face'

    def __init__(self, data: dict):
        """
        Constructor for a Card_Face object.

        Arguments
        ---------
            data (dict): dictionary of values from scryfall API used to construct card_face object

        Returns
        -------
            None
        """
        self.artist = data.get("artist")
        self.cmc = data.get("cmc")
        self.color_indicator = data.get("color_indicator")
        self.colors = data.get("colors")
        self.flavor_text = data.get("flavor_text")
        self.illustration_id = data.get("illustration_id")
        self.image_uris = data.get("image_uris")
        self.layout = data.get("layout")
        self.loyalty = data.get("loyalty")
        self.mana_cost = data["mana_cost"]
        self.name = data["name"]
        self.oracle_id = data.get("oracle_id")
        self.power = data.get("power")
        self.printed_name = data.get("printed_name")
        self.printed_text = data.get("printed_text")
        self.printed_type_line = data.get("printed_type_line")
        self.toughness = data.get("toughness")
        self.type_line = data.get("type_line")
        self.watermark = data.get("watermark")

    def image(self, option="normal"):
        """
        Return a reference to an encoded image
        at the desired size.
        
        Arguments
        ----------
            option (str): Options for returned image [small, normal, large, art_crop, border_crop, png]
        Returns
        -------
            encoded_img (bytes): encoded image data
        """
        if option not in self.image_uris.keys():
            raise ValueError

        response = requests.get(self.image_uris[option])
        return response.content

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Card_Face Object: " + self.name 
