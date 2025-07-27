import os
from time import localtime, strftime
from utils.get_all_tickers_history import get_all_tickers_history


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
        curr_time = strftime("%Y:%m:%d %H:%M:%S", localtime())
        with open(ERROR, 'a') as f:
            f.write(f'[{curr_time}] --- {e} \n')