from . import utils
from .card_face import Card_Face
from .ruling import Ruling
from .card_set import Card_Set
import requests

class Card(Card_Face):
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
    object = "Card"

    def __init__(self, query, method="search", params="q"):
        """
        Constructor for a card object. 

        Arguments
        ---------
            query (string): a search query. If default "method" argument is used, this string is
                treated identically to a search on the scryfall search bar
            method (string) [default: "search"]: type of method to use for lookup
            params (string) [default: "q"]: parameter query is packaged in when method is called
        """
        if params is None and query is None:
            data = utils.get_request("cards/" + method, None)
        else:
            data = utils.get_request("cards/" + method, {params: query})
        #Check if response is empty
        if data is None:
            raise ValueError
        else:
            if data["object"] == "list":
                data = data["data"][0]

            #Assigning core card field attributes
            # Cannot be declared dynamically due to risk
            self.arena_id = data.get("arena_id")
            self.id = data["id"]
            self.lang = data["lang"]
            self.mtgo_id = data.get("mtgo_id")
            self.mtgo_foil_id = data.get("mtgo_foil_id")
            self.multiverse_ids = data.get("multiverse_ids")
            self.tcgplayer_id = data.get("tcgplayer_id")
            self.tcgplayer_etched_id = data.get("tcgplayer_etched_id")
            self.cardmarket_id = data.get("cardmarket_id")
            self.oracle_id = data["oracle_id"]
            self.prints_search_uri = data["prints_search_uri"]
            self.rulings_uri = data["rulings_uri"]
            self.scryfall_uri = data["scryfall_uri"]
            self.uri = data["uri"]


            #Gameplay Fields
            self.all_parts = data.get("all_parts")

            self.card_faces = data.get("card_faces")
            if self.card_faces:
                card_faces = []
                for face in self.card_faces:
                    card_faces.append(Card_Face(face)) 
                self.card_faces = card_faces

            self.cmc = data["cmc"]
            self.color_identity = data["color_identity"]
            self.color_indicator = data.get("color_indicator")
            self.colors = data.get("colors")
            self.edhrec_rank = data.get("edhrec_rank")
            self.hand_modifier = data.get("hand_modifier")
            self.keywords = data["keywords"]
            self.layout = data["layout"]
            self.legalities = data["legalities"]
            self.life_modifier = data.get("life_modifier")
            self.loyalty = data.get("loyalty")
            self.mana_cost = data.get("mana_cost")
            self.name = data["name"]
            self.oracle_text = data.get("oracle_text")
            self.oversized = data["oversized"]
            self.power = data.get("power")
            self.produced_mana = data.get("produced_mana")
            self.reserved = data["reserved"]
            self.toughness = data.get("toughness")
            self.type_line = data["type_line"]

            #Print fields
            self.artist = data.get("artist")
            self.booster = data["booster"]
            self.border_color = data["border_color"]
            self.collector_number = data["collector_number"]
            self.content_warning = data.get("content_warning")
            self.digital = data["digital"]
            self.finishes = data["finishes"]
            self.flavor_name = data.get("flavor_name")
            self.flavor_text = data.get("flavor_text")
            self.frame_effects = data.get("frame effects")
            self.frame = data["frame"]
            self.full_art = data["full_art"]
            self.games = data["games"]
            self.highres_image = data["highres_image"]
            self.illustration_id = data.get("illustration_id")
            self.image_status = data["image_status"]
            self.image_uris = data.get("image_uris")
            self.prices = data.get("prices")
            self.printed_name = data.get("printed_name")
            self.printed_text = data.get("printed_text")
            self.printed_type_line = data.get("printed_type_line")
            self.promo = data["promo"]
            self.promo_types = data.get("promo_types")
            self.purchase_uris = data["purchase_uris"]
            self.rarity = data["rarity"]
            self.related_uris = data["related_uris"]
            self.released_at = data["released_at"]
            self.reprint = data["reprint"]
            self.scryfall_set_uri = data["scryfall_set_uri"]
            self.set_name = data["set_name"]
            self.set_search_uri = data["set_search_uri"]
            self.set_type = data["set_type"]
            self.set_uri = data["set_uri"]
            self.set = data["set"]
            self.set_id = data["set_id"]
            self.story_spotlight = data["story_spotlight"]
            self.textless = data["textless"]
            self.variation = data["variation"]
            self.variation_of = data.get("variation_of")
            self.security_stamp = data.get("security_stamp")
            self.watermark = data.get("watermark")
            self.previewed_at = data.get("preview.previewed_at")
            self.preview_source_uri = data.get("preview.source_uri")
            self.preview_source = data.get("preview.source")

    def reprints(self):
        """
        Return a list of card objects that 
        are reprints

        Returns
        -------
            reprints (list): list of card objects
        """
        method = self.prints_search_uri.split("https://api.scryfall.com/")[1]
        data_list = utils.get_request(method, None)["data"]
        reprints = []
        for reprint in data_list:
            reprints.append(Card(None, reprint["id"], None))
        return reprints

    def price(self, currency="USD", foil=False, conv=False, conv_to=None):
        """
        Returns the price of a card in the given currency and card type.
        
        Arguments
        ---------
            currency (string) [default: "USD"]: Returns price in given currency
                WARNING: Only supports "USD" and "EUR"
            foil (boolean) [default: False]: Returns price if foil or not
            conv (boolean) [default: False]: If true, converts price to 'conv_to' currency
            conv_to (string) [default: "USD"]: If conv is true, converts to given currency
        
        Returns
        -------
            price (float): price of card in given market and currency (May return None if no price found)
        """
        if conv and conv_to:
            exchange_rate = utils.get_exchange_rate(currency, conv_to)
        elif conv or conv_to:
            raise ValueError
        else:
            exchange_rate = None

        currency = currency.lower()
        foil_str = "_foil" if foil else ""
        price = self.prices[currency + foil_str]

        if price:
            price = float(price) * (exchange_rate if exchange_rate else 1)

        return price 

    def legality(self, game_format="standard"):
        """
        Returns a string representing legality of card in given format.

        Arguments
        ---------
            format (string)[default: "standard"]: string name of format to check legality in
        
        Returns
        -------
            is_legal (string): returns string representing legality in format
        """
        game_format = game_format.lower()
        if self.legalities.get(game_format) is None:
            return ValueError
        if self.legalities.get(game_format) == "not_legal":
            return "False"
        elif self.legalities.get(game_format) == "restricted":
            return "Restricted"
        else:
            return "True"

    def rulings(self):
        """
        Returns a list of Ruling objects constructed
        with rulings data of the card.
        
        Arguments
        ---------
            None

        Returns
        -------
            rulings_list (list): list of Ruling objects
        """
        method = self.rulings_uri.split("https://api.scryfall.com/")[1]
        data_list = utils.get_request(method, None)["data"]
        
        if len(data_list) == 0:
            return []

        rulings_list = []

        for data in data_list:
            ruling = Ruling(data)
            rulings_list.append(ruling)
        
        return rulings_list

    def card_set(self):
        """
        Returns a Set object the card belongs to 

        Arguments
        ---------
            None

        Returns
        -------
            set (Card_Set): set card belongs to
        """
        return Card_Set(self.set)




    def __str__(self):
        return self.name + " (" + self.set + ")"

    def __repr__(self):
        return str(self) + " [ID:" + self.id + "]"