This project is in progress.<br>
main.py can work now.<br>

Get all historical data will take more than 4 hours to process.<br>
However, you can pause it. <b>Next run, it continue.</b><br>

### Instruction:
Step 1. Create .env file under project folder:
```
# .env
# Data paths
INPUT_PATH                           = add/your/path
ALL_STOCKS_FILE                      = add_your_name.xlsx
ALL_STOCKS_TEST_FILE                 = add_your_name_test.xlsx

# Processing paths
PROCESSING_PATH                      = add/your/path
PROCESSING_DATA_FILE                 = add_your_name.csv
PROCESSING_DATA_TEST_FILE            = add_your_name_test.csv

OUTPUT_PATH                          = add/your/path
STOCK_HISTORICAL_PRICE_FILE          = add_your_name.parquet
STOCK_HISTORICAL_PRICE_TEST_FILE     = add_your_name_test.parquet

# Incremental index paths
INCREMENTAL_INDEX_PATH               = add/your/path
ALL_HIST_INCREMENTAL_INDEX_FILE      = add_your_name.txt
ALL_HIST_INCREMENTAL_INDEX_TEST_FILE = add_your_name_test.txt
DAILY_INCREMENTAL_INDEX_FILE         = add_your_name.txt
DAILY_INCREMENTAL_INDEX_TEST_FILE    = add_your_name.txt

# Error paths
ERROR_PATH                           = add/your/path
ERROR_FILE                           = add_your_name.txt
```

Step 2. Run main.py