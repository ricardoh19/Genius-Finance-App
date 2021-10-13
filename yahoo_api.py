import http.client
import json
import os
import sys 
import logging

class YahooAPI():
    """This class gets information from an API endpoint.
    Connection to Yahoo finc is established using http.client
    >> https://docs.python.org/3/library/http.client.html
    This class retrieves a graph for stockprice over the past 24 h for a given stock.
    It retrieves the newslink to a story about a company given the stocksymbol.
    It verifies wether a stocksymbol exists.
    It gets information on a stock current_ratio, trailing_EPS, trailing_PE, 
    debt_to_equity_ratio, stockprice given the stocksymbol.
    """
    def __init__(self):
        """Initialize stockprice graph_stock and newslink"""
        self.stockprice = 0 #int float current stockprice
        self.graph_stock = [[], []] #2D list list1: 40 float x values and list2: 40 float y values #x values are float timestamps and y values are float stockprices"
        self.newslink = "" #string holding newslink

    def get_news_uuid(self, stocksymbol):
        """This function is helper function of get_link(self, stocksymbol="TSLA")
        It posts stocksymbol to Yahoo API endpoint to retrieve uuid of a newsstory.
        UUID is used in get_details_of_uuid() 
        to get the newslink of that story associated with the uuid that we find in this function."""
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.
        except Exception as e:
            logging.error("Check that API key and host is provided in the bash script run-main.sh.")
            logging.error("Oops!", sys.exc_info()[0], "occurred.")
            logging.error("Exception: ", e)
            sys.exit(1) #crash
        #establish connection to API host
        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

        payload = ""
        # header contains authentication and host
        headers = {
            'content-type': "text/plain",
            'x-rapidapi-host': api_host,
            'x-rapidapi-key': api_key
            }
        #post request with parameter stocksymbol to the API endpoint
        conn.request("POST", f"/news/v2/list?region=US&snippetCount=1&s={stocksymbol}", payload, headers)
        #get response
        res = conn.getresponse()
        #get status code of the response
        status = res.status # 200 for is found #302 not found
        logging.info(status)
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            logging.warning(f"Stock {stocksymbol} not found. Status code: {status}")
            #TO-DO: pop up GUI?
            return 0

        data = res.read()
        result_json = json.loads( data.decode("utf-8")) #dump it in json # convert result to json/dict#dump it in json # convert result to json/dict
        uuid = result_json["data"]["main"]["stream"][0]["id"] #get uuid from result
        logging.info(f"uuid: {uuid}")
        return uuid

    def get_details_of_uuid(self, uuid):
        """This function is helper function of get_link(self, stocksymbol="TSLA")
        It passes uuid of a newsstory to Yahoo API endpoint to retrieve the newslink associated with it."""
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            logging.error("Check that API key and host is provided in the bash script run-main.sh.")
            logging.error("Oops!", sys.exc_info()[0], "occurred.")
            logging.error("Exception: ", e)
            sys.exit(1) #crash

        #establish connection to API host
        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

        # header contains authentication and host
        headers = {
        'X-RapidAPI-Host': api_host,
        'X-RapidAPI-Key': api_key
        }
        #post request with parameter uuid to the API endpoint
        conn.request("GET", f"/news/v2/get-details?uuid={uuid}&region=US", headers=headers)
        res = conn.getresponse()
        #get status code of the response
        status = res.status # 200 for is found #302 not found
        logging.info(status)
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            logging.warning(f"Status code: {status}")
            #TO-DO: pop up GUI?
            return 0

        data = res.read()
        result_json = json.loads( data.decode("utf-8")) #dump it in json # convert result to json/dict#dump it in json
        self.newslink = result_json["data"]["contents"][0]["content"]["clickThroughUrl"]["url"]
        logging.info(self.newslink)

    def get_stock_summary(self, stocksymbol):
        """Function gets information all stock info including stock current_ratio, trailing_EPS, trailing_PE, 
        debt_to_equity_ratio, stockprice given the stocksymbol from API endpoint. Returns API complete stock summary"""
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            logging.error("Check that API key and host is provided in the bash script run-main.sh.")
            logging.error("Oops!", sys.exc_info()[0], "occurred.")
            logging.error("Exception: ", e)
            sys.exit(1) #crash

        #establish connection to API host
        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")
        payload = ''
        # header contains authentication and host
        headers = {
        'X-RapidAPI-Host': api_host,
        'X-RapidAPI-Key': api_key
        }
        #post request with parameter stocksymbol to the API endpoint
        conn.request("GET", f"/stock/v2/get-summary?symbol={stocksymbol}&region=US", payload, headers)
        res = conn.getresponse()
        #get status code of the response
        status = res.status # 200 for is found #302 not found
        logging.info(status)
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            logging.warning(f"Stock {stocksymbol} not found. Status code: {status}")
            #TO-DO: pop up GUI?
            return 0
        
        # print(res) #<http.client.HTTPResponse object at 0x102d00a60>
        data = res.read()
        # print(data)
        # logging.debug(data.decode("utf-8"))
        result_json = json.loads( data.decode("utf-8"))
        # logging.debug(result_json)
        return result_json

    def get_stocks_info(self, stocksymbollist=[]):
        """Function gets information on each stock's current_ratio, trailing_EPS, trailing_PE, 
        debt_to_equity_ratio, stockprice given the stocksymbol from get_stock_summary function"""
        stockinfo ={} #remove old data
        for stocksymbol in stocksymbollist:
            stock_summary = self.get_stock_summary(stocksymbol)
            if stock_summary!=0:
                #extract stock's current_ratio, trailing_EPS, trailing_PE, debt_to_equity_ratio, stockprice from json response
                stockprice = stock_summary["financialData"]["currentPrice"]["raw"]
                logging.debug(f"stockprice {stockprice}")
                current_ratio = stock_summary["financialData"]["currentRatio"]["raw"]
                logging.debug(f"current ratio: {current_ratio}")
                debt_to_equity_ratio = stock_summary["financialData"]["debtToEquity"]["raw"]
                logging.debug(f"D2E {debt_to_equity_ratio}")
                #Trailing EPS typically refers to a company's earnings per share as a rolling total over the previous four quarters
                trailing_EPS = stock_summary["defaultKeyStatistics"]["trailingEps"]["raw"]
                logging.debug(f"Trailing EPS {trailing_EPS}")
                trailing_PE = stock_summary["summaryDetail"]["trailingPE"]["raw"]
                logging.debug(f"trailing PE: {trailing_PE}")
                ["trailingPE"]
                #put extracted data in dictionary
                stockinfo[stocksymbol] = {
                    "currentRatio": current_ratio,
                    "trailingEPS": trailing_EPS,
                    "PERatio":trailing_PE,
                    "DebtToEquityRatio": debt_to_equity_ratio,
                    "stockPrice": stockprice
                }
                logging.debug(stockinfo[stocksymbol])
        logging.debug(stockinfo)
        return stockinfo # return dict with stocksymbol as keys and data as value stored in dict
    
    def get_chart(self, stocksymbol):
        """This function retrieves a graph for stockprice over the past 24 h for a given stock from API endpoint.
        x values are float timestamps and y values are float stockprices"""
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            logging.error("Check that API key and host is provided in the bash script run-main.sh.")
            logging.error("Oops!", sys.exc_info()[0], "occurred.")
            logging.error("Exception: ", e)
            sys.exit(1) #crash

        #establish connection to API host
        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

        # header contains authentication and host
        headers = {
        'X-RapidAPI-Host': api_host,
        'X-RapidAPI-Key': api_key
        }
        #post request with parameter stocksymbol to the API endpoint
        conn.request("GET", f"/stock/v2/get-chart?interval=15m&symbol={stocksymbol}&range=1d&region=US", headers=headers)
        res = conn.getresponse()
        #get status code of the response
        status = res.status # 200 for is found #302 not found
        logging.info(status)
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            logging.warning(f"Status code: {status}")
            #TO-DO: pop up GUI?
            return 0
        
        data = res.read() 
        result_json = json.loads( data.decode("utf-8")) #dump it in json # convert result to json/dict#dump it in json
        #x-values:
        timestamp = result_json["chart"]["result"][0]["timestamp"]#returns 40 timestamps as list in format [1633515300, 1633517100, 1633518900, ...]
        logging.info(f"timestamp {timestamp}")
        # y-values:
        open_stockprice = result_json["chart"]["result"][0]["indicators"]["quote"][0]["open"] #extract past 24 h stockprice values 
        logging.info(f"stockprice {open_stockprice}")
        self.graph_stock[0] = timestamp #list of float
        self.graph_stock[1] = open_stockprice #list of float

    def get_link(self, stocksymbol="TSLA"):
        """Gets newslink associated with a given stock. 
        Gets uuid by searching API for specific stock.
        Use that uuid of an article on that stock to ge the link in the get_detail call."""
        if not self.check_stock_exists(stocksymbol):
            logging.warning("Stocksymbol doesn't exist")
            return 0
        uuid = self.get_news_uuid(stocksymbol)
        self.get_details_of_uuid(uuid)
        return self.newslink

    def get_watchlist_info(self, stocksymbollist= ["TSLA", "APPL"]):
        """This function takes a list with stocksymbols,
        it returns a dictionary with stocksymbol as keys and all ratios and info as values."""
        return self.get_stocks_info(stocksymbollist)

    def get_specific_stock_info(self, stocksymbol="APPL"):
        """This function takes a stocksymbol,
        it returns a dictionary with stocksymbol as key and all ratios and info as values."""
        return self.get_stocks_info([stocksymbol])

    def get_stock_graph(self, stocksymbol = "TESLA"):
        """This function gets stockprice over the last 24 hours.
        Returns a list of 2 list length 40.
        first list is timestamp and stockprice for the second"""
        if not self.check_stock_exists(stocksymbol):
            logging.warning("Stocksymbol doesn't exist")
            return 0
        self.get_chart(stocksymbol)
        return self.graph_stock #2D list with 2 dict timestamp and stockprice

    def check_stock_exists(self, stocksymbol):
        """Checks against API if stock exists"""
        stockinfo = self.get_stock_summary(stocksymbol)
        if stockinfo == 0:
            return False
        else:
            return True
