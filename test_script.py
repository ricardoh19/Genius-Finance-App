import logging
from yahoo_api import YahooAPI

def test_yahoo_api():
    logging.basicConfig(filename='geniusfinclogs.log', encoding='utf-8', level=logging.DEBUG, force=True)
    #Test 1 create object
    YahooAPIObject = YahooAPI()
    #Test 2 get watchlist info
    # YahooAPIObject.get_watchlist_info(["TSLA", "APPL"])
    #Test 2.1 get watchlist info wrong value
    # YahooAPIObject.get_watchlist_info(["AAAA"])
    #Test 3 get link
    # YahooAPIObject.get_link(stocksymbol="TSLA")
    # YahooAPIObject.get_watchlist_info(["AAAA"])
    #Test 4 get Graph data
    YahooAPIObject.get_stock_graph(stocksymbol="TSLA")


if __name__ == "__main__":
    test_yahoo_api()