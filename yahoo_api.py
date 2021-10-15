import http.client
import json
import os
import sys 

class YahooAPI():
    """This class gets information from an API endpoint.
    Connection to Yahoo finc is established using http.client
    >> https://docs.python.org/3/library/http.client.html
    This class retrieves a graph for stockprice over the past 24 h for a given stock.
    It retrieves the newslink to a story about a company given the stock_symbol.
    It verifies wether a stock_symbol exists.
    It gets information on a stock current_ratio, trailing_EPS, trailing_PE, 
    debt_to_equity_ratio, stockprice given the stock_symbol.

    Note:
    API call functions are first.
    Methods called from outside are below, they use the API call functions as helper functions.
    """
    def __init__(self):
        """Initialize stockprice graph_stock and newslink"""
        self.stockprice = 0 #int float current stockprice
        self.graph_stock = [[], []] #2D list list1: 40 float x values and list2: 40 float y values #x values are float timestamps and y values are float stockprices"
        self.newslink = "" #string holding newslink

    def get_news_uuid(self, stock_symbol):
        """This function is helper function of get_link(self, stock_symbol="TSLA")
        It posts stock_symbol to Yahoo API endpoint to retrieve uuid of a newsstory.
        UUID is used in get_details_of_uuid() 
        to get the newslink of that story associated with the uuid that we find in this function."""
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.
        except Exception as e:
            print("Check that API key and host is provided in the bash script run-main.sh.")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
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
        #post request with parameter stock_symbol to the API endpoint
        conn.request("POST", f"/news/v2/list?region=US&snippetCount=1&s={stock_symbol}", payload, headers)
        #get response
        res = conn.getresponse()
        #get status code of the response
        status = res.status # 200 for is found #302 not found
        print(f"status: {status}")
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            print(f"Stock {stock_symbol} not found. Status code: {status}")
            #TO-DO: pop up GUI?
            return 0

        data = res.read()
        result_json = json.loads( data.decode("utf-8")) #dump it in json # convert result to json/dict#dump it in json # convert result to json/dict
        uuid = result_json["data"]["main"]["stream"][0]["id"] #get uuid from result
        # print(f"uuid: {uuid}")
        return uuid

    def get_details_of_uuid(self, uuid):
        """This function is helper function of get_link(self, stock_symbol="TSLA")
        It passes uuid of a newsstory to Yahoo API endpoint to retrieve the newslink associated with it."""
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            print("Check that API key and host is provided in the bash script run-main.sh.")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
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
        print(f"status: {status}")
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            print(f"Status code: {status}")
            #TO-DO: pop up GUI?
            return 0

        data = res.read()
        result_json = json.loads( data.decode("utf-8")) #dump it in json # convert result to json/dict#dump it in json
        try:
            self.newslink = result_json["data"]["contents"][0]["content"]["clickThroughUrl"]["url"]
        except Exception as e:
            print("Error could not retrieve a newslink.")
            self.newslink = "Error could not retrieve a newslink."

    def get_stock_summary(self, stock_symbol):
        """Function gets information all stock info including stock current_ratio, trailing_EPS, trailing_PE, 
        debt_to_equity_ratio, stockprice given the stock_symbol from API endpoint. Returns API complete stock summary"""
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            print("Check that API key and host is provided in the bash script run-main.sh.")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
            sys.exit(1) #crash

        #establish connection to API host
        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")
        payload = ''
        # header contains authentication and host
        headers = {
        'X-RapidAPI-Host': api_host,
        'X-RapidAPI-Key': api_key
        }
        #post request with parameter stock_symbol to the API endpoint
        conn.request("GET", f"/stock/v2/get-summary?symbol={stock_symbol}&region=US", payload, headers)
        res = conn.getresponse()
        #get status code of the response
        status = res.status # 200 for is found #302 not found
        print(f"status: {status}")
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            print(f"Stock {stock_symbol} not found. Status code: {status}")
            #TO-DO: pop up GUI?
            return 0
        
        # print(res) #<http.client.HTTPResponse object at 0x102d00a60>
        data = res.read()
        # print(data)
        # print(data.decode("utf-8"))
        result_json = json.loads( data.decode("utf-8"))
        # print(result_json)
        return result_json

    def get_stocks_info(self, stock_symbollist=[]):
        """Function gets information on each stock's current_ratio, trailing_EPS, trailing_PE, 
        debt_to_equity_ratio, stockprice given the stock_symbol from get_stock_summary function"""
        stockinfo ={} #remove old data
        for stock_symbol in stock_symbollist:
            stock_summary = self.get_stock_summary(stock_symbol)
            if stock_summary!=0:
                #extract stock's current_ratio, trailing_EPS, trailing_PE, debt_to_equity_ratio, stockprice from json response
                stockprice = stock_summary["financialData"]["currentPrice"]["raw"]
                # print(f"stockprice {stockprice}")
                current_ratio = stock_summary["financialData"]["currentRatio"]["raw"]
                # print(f"current ratio: {current_ratio}")
                debt_to_equity_ratio = stock_summary["financialData"]["debtToEquity"]["raw"]
                # print(f"D2E {debt_to_equity_ratio}")
                #Trailing EPS typically refers to a company's earnings per share as a rolling total over the previous four quarters
                trailing_EPS = stock_summary["defaultKeyStatistics"]["trailingEps"]["raw"]
                # print(f"Trailing EPS {trailing_EPS}")
                trailing_PE = stock_summary["summaryDetail"]["trailingPE"]["raw"]
                # print(f"trailing PE: {trailing_PE}")
                #put extracted data in dictionary
                stockinfo[stock_symbol] = {
                    "currentRatio": current_ratio,
                    "trailingEPS": trailing_EPS,
                    "PERatio":trailing_PE,
                    "DebtToEquityRatio": debt_to_equity_ratio,
                    "stockPrice": stockprice
                }
                # print(stockinfo[stock_symbol])
        # print(stockinfo)
        return stockinfo # return dict with stock_symbol as keys and data as value stored in dict
    
    def get_chart(self, stock_symbol):
        """This function retrieves a graph for stockprice over the past 24 h for a given stock from API endpoint.
        x values are float timestamps and y values are float stockprices"""
        #get keys from environment
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            print("Check that API key and host is provided in the bash script run-main.sh.")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
            sys.exit(1) #crash

        #establish connection to API host
        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

        # header contains authentication and host
        headers = {
        'X-RapidAPI-Host': api_host,
        'X-RapidAPI-Key': api_key
        }
        #post request with parameter stock_symbol to the API endpoint
        conn.request("GET", f"/stock/v2/get-chart?interval=15m&symbol={stock_symbol}&range=1d&region=US", headers=headers)
        res = conn.getresponse()
        #get status code of the response
        status = res.status # 200 for is found #302 not found
        print(f"status: {status}")
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            print(f"Something went wrong status code: {status}")
            print("Note: Yahoo API function is returning 0.")
            #TO-DO: pop up GUI?
            return 0
        
        data = res.read() 
        result_json = json.loads( data.decode("utf-8")) #dump it in json # convert result to json/dict#dump it in json
        #x-values:
        timestamp = result_json["chart"]["result"][0]["timestamp"]#returns 40 timestamps as list in format [1633515300, 1633517100, 1633518900, ...]
        print(f"timestamp {timestamp}")
        # y-values:
        open_stockprice = result_json["chart"]["result"][0]["indicators"]["quote"][0]["open"] #extract past 24 h stockprice values 
        print(f"stockprice {open_stockprice}\n")
        self.graph_stock[0] = timestamp #list of float
        self.graph_stock[1] = open_stockprice #list of float

    def get_link(self, stock_symbol="TSLA"):
        """Gets newslink associated with a given stock. 
        Gets uuid by searching API for specific stock.
        Use that uuid of an article on that stock to ge the link in the get_detail call."""
        if not self.check_stock_exists(stock_symbol):
            return 0
        print(f"Getting uuid which is news id refering to {stock_symbol}")
        uuid = self.get_news_uuid(stock_symbol)
        print(f"uuid: {uuid}")
        self.get_details_of_uuid(uuid)
        print(f"newslink: {self.newslink}\n")
        return self.newslink

    def get_watchlist_info(self, stock_symbollist= ["TSLA", "APPL"]):
        """This function takes a list with stock_symbols,
        it returns a dictionary with stock_symbol as keys and all ratios and info as values."""
        print("Retrieving all data needed for watchlist:")
        stocks_data = self.get_stocks_info(stock_symbollist)
        print(f"Data for Watchlist: {stocks_data}\n")
        return stocks_data 

    def get_specific_stock_info(self, stock_symbol="APPL"):
        """This function takes a stock_symbol,
        it returns a dictionary with stock_symbol as key and all ratios and info as values."""
        print(f"Getting stock infos on {stock_symbol}")
        info = self.get_stocks_info([stock_symbol])
        print(f"Stock info: {info}\n")
        return info

    def get_stock_graph_values(self, stock_symbol = "TESLA"):
        """This function gets stockprice over the last 24 hours.
        Returns a list of 2 list length 40.
        first list is timestamp and stockprice for the second"""
        print("Getting stock price over past 24h for graphing purposes.")
        if not self.check_stock_exists(stock_symbol):
            return 0
        self.get_chart(stock_symbol)
        print(f"Graphing data of {stock_symbol}:")
        print(f">>> timeseries {self.graph_stock[0]}\n")
        print(f">>> stockprice {self.graph_stock[1]}\n")
        return self.graph_stock #2D list with 2 dict timestamp and stockprice

    def check_stock_exists(self, stock_symbol):
        """Checks against API if stock exists"""
        print(f"Checking wether {stock_symbol} exists")
        stockinfo = self.get_stock_summary(stock_symbol)

        if stockinfo == 0:
            print(f"Error: Stocksymbol {stock_symbol} does not exist.\n")
            return False
        else:
            print(f"Stocksymbol {stock_symbol} exists.\n")
            return True
