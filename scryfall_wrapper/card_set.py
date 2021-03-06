"""
Class for Set objects representing a group
of related magic cards
"""

from . import utils
from . import card

class Card_Set():
    """
    A class used to represent a set of related cards in
    Magic the Gathering

    ...

    Attributes
    ----------
    A full list of attributes can be found at https://scryfall.com/docs/api/sets.

    Methods
    -------
    cards()
        Return a list of Card objects for cards in the set. 
    """

    object = "Card_Set"

    def __init__(self, set_code: str):
        """
        Constructor for a Card_Set object.

        Arguments
        ---------
            set_code (str) = 3-letter string representing desired set
        
        Returns
        -------
            None
        """
        set_code = set_code.lower()

        data = utils.get_request("/sets/" + set_code, None)

        if data is None:
            raise ValueError
        
        # Assign core fields from data
        self.id = data["id"]
        self.code = data["code"]
        self.mtgo_code = data.get("mtgo_code")
        self.arena_code = data.get("arena_code")
        self.tcgplayer_id = data.get("tcgplayer_id")
        self.name = data["name"]
        self.set_type = data["set_type"]
        self.released_at = data.get("released_at")
        self.block_code = data.get("block_code")
        self.block = data.get("block")
        self.parent_set_code = data.get("parent_set_code")
        self.card_count = data["card_count"]
        self.printed_size = data.get("printed_size")
        self.digital = data["digital"]
        self.foil_only = data["foil_only"]
        self.nonfoil_only = data["nonfoil_only"]
        self.scryfall_uri = data["scryfall_uri"]
        self.uri = data["uri"]
        self.icon_svg_uri = data["icon_svg_uri"]
        self.search_uri = data["search_uri"]

    def cards(self):
        """
        Return a list of Card objects for cards in the set. 

        Returns
        -------
        cards : list
            List of card objects representing cards in the set
        """
        
        has_more = True
        method = self.search_uri.split("https://api.scryfall.com/")[1]
        data_list = []

        # Continue filling data_list until all pages of data have been parsed
        while has_more:
            page = utils.get_request(method, None)
            has_more = page["has_more"]
            next_page = page.get("next_page")
            data = page["data"]
            data_list.extend(data)
            if next_page:
                method = next_page.split("https://api.scryfall.com/")[1]

        cards = []

        # Create and append card objects to cards
        for data in data_list:
            cards.append(card.Card(None, None, None, data))

        return cards

    def __str__(self):
        return self.name + " (" + self.code.upper() + ")"

    def __repr__(self):
        return "Card_Set Object (" + self.code.upper() + ")"

