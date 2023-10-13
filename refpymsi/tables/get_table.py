

import gzip
import json
import pandas
import polars as pl
import pprint

from refpymsi.utils import get_data_path

def get_table(nom_table, plrs = True):
    with gzip.GzipFile(get_data_path() + "/tables/" + nom_table + ".json.gz", 'r') as json_file:
                   data = json.loads(json_file.read().decode('utf-8'))
    
    d =  pandas.DataFrame(data)

    if plrs:
        return(pl.from_pandas(d))

    return(d)


