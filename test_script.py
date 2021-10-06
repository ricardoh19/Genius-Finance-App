import logging
from yahoo_api import YahooAPI

def test_yahoo_api():
    logging.basicConfig(filename='geniusfinclogs.log', encoding='utf-8', level=logging.DEBUG, force=True)
    YahooAPIObject = YahooAPI()
    YahooAPIObject.get_watchlist_stock_info()

if __name__ == "__main__":
    test_yahoo_api()