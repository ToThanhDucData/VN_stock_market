import utils.web_api_caller as tcbs
import numpy as np
import pandas as pd
import re
import os
from time import time, sleep, localtime, strftime
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def main():
    #---------------------------------------------------------------
    PROCESSING_PATH = os.getenv('PROCESSING_PATH')
    PROCESSING_DATA = os.path.join(PROCESSING_PATH, os.getenv('PROCESSING_DATA_FILE'))
    PROCESSING_INDEX = os.path.join(PROCESSING_PATH, os.getenv('PROCESSING_INDEX_FILE'))
    #---------------------------------------------------------------

    #---------------------------------------------------------------
    DATA_PATH = os.getenv('DATA_PATH')
    ALL_STOCKS = os.path.join(DATA_PATH, os.getenv('ALL_STOCKS_FILE'))
    STOCK_HISTORICAL_PRICE = os.path.join(DATA_PATH, os.getenv('STOCK_HISTORICAL_PRICE_FILE'))
    #---------------------------------------------------------------

    stocks = pd.read_csv(ALL_STOCKS)
    stocks_list = stocks['ticker'].to_list()
    
    print(f"Calling API...")
    latest_df = tcbs.get_all_price_history(stocks_list, PROCESSING_INDEX, PROCESSING_DATA)

    print("Formatting to tabular...")
    latest_extracted = tcbs.extract_information(raw_json=latest_df)

    print("Removing duplicates...")
    extracted_df = latest_extracted.copy().drop_duplicates()
    
    print("Updating 'stock_price_history.parquet'...")
    extracted_df.to_parquet(STOCK_HISTORICAL_PRICE)
    print("'stock_price_history.parquet' was updated")

if __name__ == '__main__':
    #---------------------------------------------------------------
    ERROR_PATH = os.getenv('ERROR_PATH')
    ERROR = os.path.join(ERROR_PATH, os.getenv('ERROR_FILE'))
    #---------------------------------------------------------------

    try:
        main()
    except Exception as e:
        curr_time = strftime("%Y:%m:%d %H:%M:%S", localtime())
        with open(ERROR, 'a') as f:
            f.write(f'[{curr_time}] --- {e} \n')