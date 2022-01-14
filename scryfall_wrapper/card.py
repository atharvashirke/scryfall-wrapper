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
            self.card_back_id = data["card_back_id"]
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
        
    def image(self, option="normal"):
        """
        Return a reference to an encoded image
        at the desired size.
        
        Attributes
        ----------
            option (str): Options for returned image [small, normal, large, art_crop, border_crop, png]
        Returns
        -------
            encoded_img (bytes): encoded image data
        """
        response = requests.get(self.image_uris[option])
        return response.content
