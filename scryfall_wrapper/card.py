from . import utils
import requests

class Card:
    """
    A class used to represent a card in Magic the Gathering

    ...

    Attributes
    ----------
    name : str
        the name of the card

    Methods
    -------

    """

    def __init__(self, query):
        """
        Constructor for a card object 

        Arguments
        ---------
            query (string): full-text string search query (similar to what you'd search in the scryfall search bar)
        """
        data = utils.get_request("cards/search", {"q": query})
        #Check if response is empty
        if data is None:
            raise ValueError
        else:
            data = data["data"][0]

            #Assigning attributes from response content
            self.name = data["name"]
            self.image_uris = data["image_uris"]
            self.land = data["lang"]
            self.cmc = data["cmc"]
            self.color_identity = data["color_identity"]
            self.mana_cost = data.get("mana_cost")
            self.release_date = data["released_at"]
            self.type_line = data["type_line"]
            self.oracle_text = data.get("oracle_text")
            self.power = data.get("power")
            self.toughness = data.get("toughness")
            self.artist = data.get("artist")
            self.legality = data["legalities"]
            self.set_name = data["set_name"]
            self.set = data["set"]
            self.collector_number = data["collector_number"]
            self.prices = data["prices"]
        
    def image(self, option="normal"):
        """
        Return a reference to an encoded image
        at the desired size.
        
        Attributes
        ----------
            option (str): Options for returned image [small, normal, large, png]
        Returns
        -------
            encoded_img (bytes): encoded image data
        """
        response = requests.get(self.image_uris[option])
        return response.content
    




