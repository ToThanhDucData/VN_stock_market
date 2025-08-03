from utils.get_all_tickers_history import get_all, get_daily
from utils.error_handling import errors_log

def main():
    test = True
    feature_selection = 1
    if feature_selection == 1:
        get_all(test)
    elif feature_selection == 2:
        get_daily(test)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        errors_log(e)