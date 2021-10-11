import logging
from yahoo_api import YahooAPI
from main import set_env_variables

import unittest # use unittest

def test_yahoo_api():
    try:
        logging.basicConfig(filename='geniusfinclogs.log', encoding='utf-8', level=logging.DEBUG, force=True)
    except:
        logging.error("Please check if you are using python 3.9")
    set_env_variables()
    #Test 1 create object
    YahooAPIObject = YahooAPI()
    #Test 2 get watchlist info
    YahooAPIObject.get_watchlist_info(["TSLA", "AMRN"])
    #Test 2.1 get watchlist info wrong value
    YahooAPIObject.get_watchlist_info(["AAAA"])
    #Test 3 get link
    YahooAPIObject.get_link(stocksymbol="TSLA")
    YahooAPIObject.get_watchlist_info(["AAAA"])
    #Test 4 get Graph data
    YahooAPIObject.get_stock_graph(stocksymbol="TSLA")
    YahooAPIObject.get_stock_graph(stocksymbol="AAAA")
    #Test 5 check stock exists
    YahooAPIObject.check_stock_exists("TSLA")
    YahooAPIObject.check_stock_exists("AAAA")



if __name__ == "__main__":
    test_yahoo_api()