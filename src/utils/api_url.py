import pandas as pd

def get_TCBS_API(ticker, timestamp, days):
    sub_domain = 'apipubaws'
    domain = 'tcbs.com.vn'
    api_type = 'stock-insight/v2/stock/bars-long-term'

    param_ticker = ticker
    param_type = 'stock'
    param_resolution = 'D'
    param_to = timestamp
    param_count_back = days

    p1 = 'ticker={}'.format(param_ticker)
    p2 = 'type={}'.format(param_type)
    p3 = 'resolution={}'.format(param_resolution)
    p4 = 'to={}'.format(param_to)
    p5 = 'countBack={}'.format(param_count_back)
    
    api_url = f'https://{sub_domain}.{domain}/{api_type}?{p1}&{p2}&{p3}&{p4}&{p5}'
    raw_df = pd.read_json(api_url)
    return raw_df