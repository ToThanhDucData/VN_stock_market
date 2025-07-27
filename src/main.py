import os
from utils.get_all_tickers_history import get_all_tickers_history
from utils.error_log import errors_log


def main():
    get_all_tickers_history()

if __name__ == '__main__':
    #---------------------------------------------------------------
    ERROR_PATH = os.getenv('ERROR_PATH')
    ERROR = os.path.join(ERROR_PATH, os.getenv('ERROR_FILE'))
    #---------------------------------------------------------------

    try:
        main()
    except Exception as e:
        errors_log(ERROR, e)