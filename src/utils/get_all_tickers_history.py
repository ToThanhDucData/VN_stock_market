import pandas as pd
import os
from dotenv import load_dotenv
from utils.json_to_df import extract_information
from utils.tcbs_api_caller import get_all_stocks_historical_price

load_dotenv()

def get_all_tickers_history():
    #---------------------------------------------------------------
    PROCESSING_PATH = os.getenv('PROCESSING_PATH')
    PROCESSING_DATA = os.path.join(PROCESSING_PATH, os.getenv('PROCESSING_DATA_FILE'))
    #---------------------------------------------------------------

    #---------------------------------------------------------------
    INCREMENTAL_INDEX_PATH = os.getenv('INCREMENTAL_INDEX_PATH')
    ALL_HIST_INCREMENTAL_INDEX = os.path.join(INCREMENTAL_INDEX_PATH, os.getenv('ALL_HIST_INCREMENTAL_INDEX_FILE'))
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
    latest_df = get_all_stocks_historical_price(stocks_list, ALL_HIST_INCREMENTAL_INDEX, PROCESSING_DATA)

    print("Formatting to tabular...")
    latest_extracted = extract_information(latest_df)

    print("Removing duplicates...")
    extracted_df = latest_extracted.copy().drop_duplicates()
    
    print("Updating 'stock_price_history.parquet'...")
    extracted_df.to_parquet(STOCK_HISTORICAL_PRICE)
    print("'stock_price_history.parquet' was updated")