"""
Class for objects representing rulings for
particular cards
"""

class Ruling():
    """
    Object representing Oracle, WOTC, and Scryfall rulings

    ...

    Attributes
    ----------
    source : str 
        String representing org that produced ruling
    published_at : str
        String representing date ruling was published 
        (YYYY-MM-DD)
    comment : str
        Ruling text
    """

    def __init__(self, data):
        """
        Constructor for Ruling object
        
        Parameters
        ----------
        data : dict
            A dictionary of data for Ruling object construction
        """
        
        self.source = data["source"]
        self.published_at = data["published_at"]
        self.oracle_id = data["oracle_id"]
        self.comment = data["comment"]

    def __str__(self):
        return self.comment + " (" + self.published_at + ")"
    
    def __repr__(self):
        return "Ruling Object Dated: " + self.published_at

    
    

    