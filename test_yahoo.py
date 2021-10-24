import logging
from yahoo_api import YahooAPI
from main import set_env_variables
from user import User

def test_yahoo_api():
    #Test py version 3.9
    try:
        logging.basicConfig(filename='geniusfinclogs.log', encoding='utf-8', level="DEBUG", force=True)
    except:
        print("Please check if you are using python 3.9")
    #Test Yahoo API
    test_suite_yahoo_api("TSLA") #run without keys
    set_env_variables() #now with keys
    test_suite_yahoo_api("AAAA")  #incorrect stocksymbol  
    test_suite_yahoo_api("AMRN") #correct stocksymbol
    
def test_suite_yahoo_api(stocksymbol1= "TSLA"):
    #Test 1 create object
    YahooAPIObject = YahooAPI()
    print(YahooAPIObject)
    #Test 2 get watchlist info
    watchlist = YahooAPIObject.get_watchlist_info([stocksymbol1, "AMRN"])
    print(watchlist)    
    #Test 3 get link
    print(YahooAPIObject.get_link(stock_symbol=stocksymbol1))
    #Test 4 get Graph data
    print(YahooAPIObject.get_stock_graph_values(stock_symbol=stocksymbol1))
    #Test 5 check stock existscre
    print(YahooAPIObject.check_stock_exists(stocksymbol1))
    #Test 6 Get specific stock info
    print(YahooAPIObject.get_specific_stock_info(stocksymbol1))


if __name__ == "__main__":
    test_yahoo_api()
