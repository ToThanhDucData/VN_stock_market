This project is in progress.

Step 1. Create .env file under project folder:
```
# .env
# Processing paths
PROCESSING_PATH=add/your/path
PROCESSING_DATA_FILE=choose_your_name.csv

# Data paths
INPUT_PATH=add/your/path
ALL_STOCKS_FILE=choose_your_tickers_list_name.xlsx

OUTPUT_PATH=add/your/path
STOCK_HISTORICAL_PRICE_FILE=choose_your_name.parquet

# Incremental index paths
INCREMENTAL_INDEX_PATH = add/your/path
INCREMENTAL_INDEX_FILE=choose_your_name.txt

# Error paths
ERROR_PATH=add/your/path
ERROR_FILE=choose_your_name.txt
```

Step 2. Run main.py