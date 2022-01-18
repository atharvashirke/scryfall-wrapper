"""
Class for objects representing rulings for
particular cards
"""

class Ruling():
    """
    Object representing Oracle, WOTC, and Scryfall rulings/notes
    about particular cards.
    """

    def __init__(self, data):
        """
        Constructor for Ruling object
        
        Arguments
        ---------
            scryfall_data (dict): dictionary of data for construction

        Returns
        -------
            None
        """
        self.source = data["source"]
        self.published_at = data["published_at"]
        self.oracle_id = data["oracle_id"]
        self.comment = data["comment"]

    def __str__(self):
        return self.comment + " (" + self.published_at + ")"
    
    def __repr__(self):
        return "Ruling Object Dated: " + self.published_at

    
    

    