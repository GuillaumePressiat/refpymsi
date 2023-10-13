


import gzip
import json
import pprint

from refpymsi.utils import get_data_path


def get_liste(nom_liste, plrs = True):
    with open(get_data_path() + "/listes/" + nom_liste + ".json") as json_file: 
                   data = json.load(json_file)
    
    return(data)

