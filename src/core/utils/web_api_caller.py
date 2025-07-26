import re
import numpy as np
import pandas as pd
import utils.incremental as incremental
from time import time, sleep, localtime, strftime
from datetime import datetime

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
    raw_df = pd.read_json(api_url)
    return raw_df

def get_stock_historical_price(ticker_name, current_timestamp, count_back):
    raw = pd.DataFrame()
    while True:
        date_to_get = str(datetime.fromtimestamp(current_timestamp))[:10]
        print(f'All {count_back} days historical prices of ticker {ticker_name} before {date_to_get}')
        
        raw_df = get_API(ticker = ticker_name, timestamp = current_timestamp, days = count_back)
        raw = pd.concat([raw, raw_df])
        
        if raw_df.shape[0] == 0:
            break

        current_timestamp -= 365*24*60*60
        sleep(0.5)
    return raw

def get_all_stocks_historical_price(stocks_list, incremental_index_file, processing_df):
    print("Reading from INCREMENTAL INDEX file..")
    __stock_epoch = incremental.incremental_index(saved_file = incremental_index_file)

    #---------------------------------------------------------------
    if __stock_epoch == 0:
        with open(processing_df, 'a') as raw_f:
            raw_f.write("ticker,data,last_updated\n")
    #---------------------------------------------------------------

    #---------------------------------------------------------------
    __all_stocks_number = len(stocks_list)
    for stock in stocks_list[__stock_epoch:]:
        print('')
        print(f'Updating all historical prices for ticker {stock}...')
        print('=====================================================')
        
        current_timestamp = int(time())
        _raw = get_stock_historical_price(ticker_name = stock, current_timestamp = current_timestamp, count_back = 365)
        #_raw.fillna('', inplace = True)

        print('-----------------------------------------------------')
        print("Updating PROCESSING DATA..")
        with open(processing_df, 'a') as raw_f:
            for _, row in _raw.iterrows():
                raw_f.write(row.ticker + ",\"" + str(row.data) + "\"," + str(time()) + '\n')
        print("---PROCESSING DATA UPDATED.---")
        print('-----------------------------------------------------')
        __stock_epoch += 1
        print(f'{stock} Completed.')
        print('{:,}/{:,}'.format(__stock_epoch, __all_stocks_number))

        print('-----------------------------------------------------')
        print("Updating INCREMENTAL INDEX..")
        with open (incremental_index_file, 'a') as index_f:
            index_f.write(str(__stock_epoch) + '\n')
        print("---INCREMENTAL INDEX UPDATED.---")
        print('-----------------------------------------------------')
        print('=====================================================')
        print('')
    #---------------------------------------------------------------

    return pd.read_csv(processing_df)

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

    return raw_json[['ticker','open', 'high', 'low', 'close', 'volume', 'date', 'last_updated']]