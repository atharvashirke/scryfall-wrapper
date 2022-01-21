"""
Misc. functions 
"""

import requests
import time
import json
from datetime import datetime

def get_request(method: str, params):
    """
    Function for making get requests to scryfall API. Manages
    rate limits for good citizenship. Returns contents of JSON response
    as a dict.

    Parameters
    ----------
    method : str
        Method to be added to scryfall endpoint (https://api.scryfall.com/METHOD)
    params : dict
        A dictionary with parameters for API call. If none, no parameters are added
        to the request.
    Returns
    -------
    content : dict 
        Dictionary with content of response
    """

    if params:
        response = requests.get("https://api.scryfall.com/" + method, params=params)
    else:
        response = requests.get("https://api.scryfall.com/" + method)

    # Space requests by 1/10 seconds
    time.sleep(0.10)

    output = response.json()

    # If response results in error, return None
    if output["object"] == "error":
        return None
    
    return response.json()

def str_to_date(date_string: str, date_format="%Y-%m-%d"):
    """
    Given a string representation of a date, return
    a datetime object of that date. 

    Parameters
    ----------
    date_string : str 
        A string representing a date
    date_format : str, optional
        A string representing the format of a date 
        (default is "%Y-%m-%d")
    Returns
    -------
    date : datetime
        A date object representation of given date_string
    """

    date = datetime.strptime(date_string, date_format)
    return date

def write_timestamped_file(dir_path_str, content, ftype=".json"):
    """
    Writes a timestamped file to the given directory.

    Parameters
    ----------
    dir_path_str : str
        A string path of directory for file to be written in.
    content : str
        A string representing content to write to file
    ftype : str, optional
        A string representing file type to be written as. 
        (default is ".json")
    Returns
    -------
    path : str
        String path of written file
    """

    mode_ref = {".jpg": "wb", ".png": "wb", ".json": "w"}
    timestr = time.strftime("%Y%m%d-%H%M%S")
    path = dir_path_str + timestr + ftype
    with open(path, mode_ref.get(ftype, "w")) as bdf:
        if ftype == ".json":
            json.dump(content, bdf)
        else:
            bdf.write(content)
    return path

def get_exchange_rate(from_currency, to_currency):
    """
    Given two currencies, returns a float representing
    the exchange rate. 

    Parameters
    ----------
    from_currency : str
        3-letter abbreviated currency to exchange [ex:"USD"]
    to_currency : str 
        3-letter abbreviated currency after conversion [ex: "EUR"]
    Returns
    -------
    exchange_rate : float 
        Rate of exchange for from_currency:to_currency
    """

    try:
        response = requests.get("https://v6.exchangerate-api.com/v6/0e164fc6317a50745338c53e/latest/" + from_currency)
    except requests.exceptions.HTTPError as err:
        SystemExit(err)

    exchange_rate = float(response.json()["conversion_rates"][to_currency])
    return exchange_rate