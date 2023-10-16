


import gzip
import json
import pprint
import pandas
import polars as pl

from refpymsi.utils import get_data_path


def get_liste(nom_liste, plrs = True):
    with open(get_data_path() + "/listes/" + nom_liste + ".json") as json_file: 
                   data = json.load(json_file)
    
    return(data)


def get_dictionnaire_listes(plrs = True):
    with open(get_data_path() + "/dictionnaire.json") as json_file: 
                   data = json.load(json_file)
    
    d =  pandas.DataFrame(data)

    if plrs:
        return(pl.from_pandas(d))

    return(data)

