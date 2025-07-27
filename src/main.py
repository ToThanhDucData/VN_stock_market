from utils.get_all_tickers_history import get_all_tickers_history
from utils.error_log import errors_log


def main():
    test = True
    get_all_tickers_history(test)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        errors_log(e)