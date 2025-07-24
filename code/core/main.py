import utils.web_api_caller as tcbs
import time

tickers_list = ['vic']
current_timestamp = int(time.time())
days = 365

api_url = tcbs.get_API(ticker = tickers_list[0]
                       ,timestamp = current_timestamp
                       ,days = days
                       )
print(api_url)