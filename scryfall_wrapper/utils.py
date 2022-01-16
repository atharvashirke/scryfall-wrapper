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

    Arguments
    ---------
        method (str): method to be added to scryfall endpoint (https://api.scryfall.com/METHOD)
        params (dict): dictionary with parameters for API call
    Returns
    -------
        content (dict): content of response
    """
    if params:
        response = requests.get("https://api.scryfall.com/" + method, params=params)
    else:
        response = requests.get("https://api.scryfall.com/" + method)
    time.sleep(0.10)
    output = response.json()
    if output["object"] == "error":
        return None
    return response.json()

def str_to_date(date_string: str, date_format="%Y-%m-%d"):
    """
    Given a string representation of a date, return
    a datetime object of that date. 

    Arguments
    ---------
        date_string (str): string representation of date
    Returns
    -------
        date (datetime): date object representation of date
    """
    date = datetime.strptime(date_string, date_format)
    return date

def write_timestamped_file(dir_path_str, content, ftype=".json"):
    """
    Writes a timestamped file to the given directory.
        Parameters:
            dir_path_str (str): path of directory to be written
            ftype (str): string file suffix
            content (str): content to write to file
        Returns:
            path (str): path of written file
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
        Parameters:
            from_currency (string): abbreviated currency to exchange [ex:"USD"]
            to_currency (string): abbreviated currency after conversion [ex: "EUR"]
        Returns:
            exchange_rate (float): rate of exchange for from_currency:to_currency
    """
    try:
        response = requests.get("https://v6.exchangerate-api.com/v6/0e164fc6317a50745338c53e/latest/" + from_currency)
    except requests.exceptions.HTTPError as err:
        SystemExit(err)

    exchange_rate = float(response.json()["conversion_rates"][to_currency])
    return exchange_rate