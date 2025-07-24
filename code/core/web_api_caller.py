import re
import numpy as np
import pandas as pd

def get_API(ticker, timestamp, days):
    sub_domain = 'apipubaws'
    domain = 'tcbs.com.vn'
    api_type = 'stock-insight/v2/stock/bars-long-term'

    param_ticker = ticker
    param_type = 'stock'
    param_resolution = 'D'
    param_to = timestamp
    param_count_back = days

    p1 = 'ticker={}'.format(param_ticker)
    p2 = 'type={}'.format(param_type)
    p3 = 'resolution={}'.format(param_resolution)
    p4 = 'to={}'.format(param_to)
    p5 = 'countBack={}'.format(param_count_back)
    
    api_url = f'https://{sub_domain}.{domain}/{api_type}?{p1}&{p2}&{p3}&{p4}&{p5}'
    return api_url

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

    to_number = ['open', 'high', 'low', 'close', 'volume']
    for col in to_number:
        print("\tChanging data type for column {}..".format(col.upper()))
        raw_json[col] = raw_json[col].astype(float)

    print("\tChanging data type for column DATE")
    raw_json['date'] = pd.to_datetime(raw_json['date'].apply(lambda x: x.split("T")[0].replace("'", "")))
    print('\t-----------------------------------------------------')

    return raw_json[['ticker','open', 'high', 'low', 'close', 'volume', 'date']]