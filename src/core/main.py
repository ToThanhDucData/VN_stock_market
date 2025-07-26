import utils.web_api_caller as tcbs
import pandas as pd
import os
from time import localtime, strftime
from dotenv import load_dotenv

load_dotenv()

def main():
    #---------------------------------------------------------------
    PROCESSING_PATH = os.getenv('PROCESSING_PATH')
    PROCESSING_DATA = os.path.join(PROCESSING_PATH, os.getenv('PROCESSING_DATA_FILE'))
    #---------------------------------------------------------------

    #---------------------------------------------------------------
    INCREMENTAL_INDEX_PATH = os.getenv('INCREMENTAL_INDEX_PATH')
    INCREMENTAL_INDEX = os.path.join(INCREMENTAL_INDEX_PATH, os.getenv('INCREMENTAL_INDEX_FILE'))
    #---------------------------------------------------------------

    #---------------------------------------------------------------
    INPUT_PATH = os.getenv('INPUT_PATH')
    ALL_STOCKS = os.path.join(INPUT_PATH, os.getenv('ALL_STOCKS_FILE'))

    OUTPUT_PATH = os.getenv('OUTPUT_PATH')
    STOCK_HISTORICAL_PRICE = os.path.join(OUTPUT_PATH, os.getenv('STOCK_HISTORICAL_PRICE_FILE'))
    #---------------------------------------------------------------

    stocks = pd.read_excel(ALL_STOCKS)
    stocks_list = stocks['ticker_id'].to_list()
    
    print("Calling API...")
    latest_df = tcbs.get_all_stocks_historical_price(stocks_list, INCREMENTAL_INDEX, PROCESSING_DATA)

    print("Formatting to tabular...")
    latest_extracted = tcbs.extract_information(latest_df)

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