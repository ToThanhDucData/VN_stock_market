import re
import numpy as np
import pandas as pd

def extract_information(raw_json):
    print("\tFormatting data from JSON..")
    raw_json['data'] = raw_json['data'].apply(lambda x: re.sub("[{ }]", "", x).split(","))
    print('\t-----------------------------------------------------')

    to_extract = ['open', 'high', 'low', 'close', 'volume', 'date']
    col_index = 0
    for col in to_extract:
        print("\tExtracting column {}..".format(col.upper()))
        raw_json[col] = raw_json['data'].apply(lambda x: x[col_index].split(":")[1]).replace("None", np.nan)
        col_index += 1
    print('\t-----------------------------------------------------')

    to_number = ['open', 'high', 'low', 'close', 'volume', 'last_updated']
    for col in to_number:
        print("\tChanging data type for column {}..".format(col.upper()))
        raw_json[col] = raw_json[col].astype(float)

    print("\tChanging data type for column DATE")
    raw_json['date'] = pd.to_datetime(raw_json['date'].apply(lambda x: x.split("T")[0].replace("'", "")))
    print('\t-----------------------------------------------------')

    return raw_json[['ticker','open', 'high', 'low', 'close', 'volume', 'date', 'last_updated']]