from utils.get_all_tickers_history import get_all_tickers_history
from utils.error_handling import errors_log


def main():
    test = False
    get_all_tickers_history(test)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        errors_log(e)