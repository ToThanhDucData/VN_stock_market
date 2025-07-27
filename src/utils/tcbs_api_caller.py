import pandas as pd
from utils.incremental import incremental_index
from utils.api_url import get_TCBS_API
from time import time, sleep
from datetime import datetime

def get_stock_historical_price(ticker_name, current_timestamp, count_back=None):
    raw = pd.DataFrame()
    if count_back == None:
        while True:
            date_to_get = str(datetime.fromtimestamp(current_timestamp))[:10]
            print(f'Getting 1 year of historical prices of ticker {ticker_name} before {date_to_get}')
            
            raw_df = get_TCBS_API(ticker = ticker_name, timestamp = current_timestamp, days = 365)
            raw = pd.concat([raw, raw_df])
            
            if raw_df.shape[0] == 0:
                break

            current_timestamp -= 365*24*60*60
            sleep(0.5)
    else:
        while raw.shape[0] < count_back:
            date_to_get = str(datetime.fromtimestamp(current_timestamp))[:10]
            print(f'Getting 1 year of historical prices of ticker {ticker_name} before {date_to_get}')
            
            raw_df = get_TCBS_API(ticker = ticker_name, timestamp = current_timestamp, days = 365)
            raw = pd.concat([raw, raw_df])

            current_timestamp -= 365*24*60*60
            sleep(0.5)
        raw['date'] = raw['data'].apply(lambda x: pd.to_datetime(x['tradingDate']))
        raw = raw.sort_values(by = 'date', ascending = False).head(count_back)
    return raw

def get_all_stocks_historical_price(stocks_list, incremental_index_file, processing_df):
    print("Reading from INCREMENTAL INDEX file..")
    __stock_epoch = incremental_index(saved_file = incremental_index_file)

    #---------------------------------------------------------------
    if __stock_epoch == 0:
        with open(processing_df, 'w') as raw_f:
            raw_f.write("ticker,data,last_updated\n")
    #---------------------------------------------------------------

    #---------------------------------------------------------------
    __all_stocks_number = len(stocks_list)
    for stock in stocks_list[__stock_epoch:]:
        print('')
        print(f'Updating all historical prices for ticker {stock}...')
        print('=====================================================')
        
        current_timestamp = int(time())
        _raw = get_stock_historical_price(ticker_name = stock, current_timestamp = current_timestamp)
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