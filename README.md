This project is in progress.<br>
main.py can work now.<br>

Get all historical data will take more than 4 hours to process. However, you can pause it.<br>

### Instruction:
Step 1. Create .env file under project folder:
```
# .env
# Processing paths
PROCESSING_PATH=add/your/path
PROCESSING_DATA_FILE=choose_your_name.csv

# Data paths
INPUT_PATH=add/your/path
ALL_STOCKS_TEST_FILE=choose_your_small_tickers_list_name.xlsx
ALL_STOCKS_FILE=choose_your_complete_tickers_list_name.xlsx

OUTPUT_PATH=add/your/path
STOCK_HISTORICAL_PRICE_FILE=choose_your_name.parquet

# Incremental index paths
INCREMENTAL_INDEX_PATH = add/your/path
ALL_HIST_INCREMENTAL_INDEX_FILE=choose_your_name.txt

# Error paths
ERROR_PATH=add/your/path
ERROR_FILE=choose_your_name.txt
```

Step 2. Run main.py