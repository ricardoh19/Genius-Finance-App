import http.client
import json
import os
import sys 
import logging

class YahooAPI():
    def __init__(self):
        self.stockprice = ""
        self.graph_stock = [[], []] #2D list x and y values
        self.newslink = ""

    def get_news_uuid(self, stocksymbol):
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.
        except Exception as e:
            logging.error("Check that API key and host is provided in the bash script run-main.sh.")
            logging.error("Oops!", sys.exc_info()[0], "occurred.")
            logging.error("Exception: ", e)
            sys.exit(1) #crash
        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

        payload = ""

        headers = {
            'content-type': "text/plain",
            'x-rapidapi-host': "yh-finance.p.rapidapi.com",
            'x-rapidapi-key': "9928c7260amshad0766390e03e89p1f4683jsn18824f37a5dc"
            }

        conn.request("POST", f"/news/v2/list?region=US&snippetCount=1&s={stocksymbol}", payload, headers)

        res = conn.getresponse()

        status = res.status # 200 for is found #302 not found
        logging.info(status)
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            logging.warning(f"Stock {stocksymbol} not found. Status code: {status}")
            #TO-DO: pop up GUI?
            return 0

        data = res.read()
        result_json = json.loads( data.decode("utf-8")) #dump it in json
        uuid = result_json["data"]["main"]["stream"][0]["id"]
        logging.info(f"uuid: {uuid}")
        return uuid

    def get_details_of_uuid(self, uuid):
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            logging.error("Check that API key and host is provided in the bash script run-main.sh.")
            logging.error("Oops!", sys.exc_info()[0], "occurred.")
            logging.error("Exception: ", e)
            sys.exit(1) #crash

        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

        headers = {
        'X-RapidAPI-Host': api_host,
        'X-RapidAPI-Key': api_key
        }
        conn.request("GET", f"/news/v2/get-details?uuid={uuid}&region=US", headers=headers)
        res = conn.getresponse()
        status = res.status # 200 for is found #302 not found
        logging.info(status)
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            logging.warning(f"Status code: {status}")
            #TO-DO: pop up GUI?
            return 0

        data = res.read()
        result_json = json.loads( data.decode("utf-8")) #dump it in json
        self.newslink = result_json["data"]["contents"][0]["content"]["clickThroughUrl"]["url"]
        logging.info(self.newslink)

    def get_stock_summary(self, stocksymbol):
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            logging.error("Check that API key and host is provided in the bash script run-main.sh.")
            logging.error("Oops!", sys.exc_info()[0], "occurred.")
            logging.error("Exception: ", e)
            sys.exit(1) #crash

        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")
        payload = ''
        headers = {
        'X-RapidAPI-Host': api_host,
        'X-RapidAPI-Key': api_key
        }
        conn.request("GET", f"/stock/v2/get-summary?symbol={stocksymbol}&region=US", payload, headers)
        res = conn.getresponse()
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
        stockinfo ={} #remove old data
        for stocksymbol in stocksymbollist:
            stock_summary = self.get_stock_summary(stocksymbol)
            if stock_summary!=0:
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
                stockinfo[stocksymbol] = {
                    "currentRatio": current_ratio,
                    "trailingEPS": trailing_EPS,
                    "PERatio":trailing_PE,
                    "DebtToEquityRatio": debt_to_equity_ratio,
                    "stockPrice": stockprice
                }
                logging.debug(stockinfo[stocksymbol])
        logging.debug(stockinfo)
        return stockinfo
    
    def get_chart(self, stocksymbol):
        try:
            api_host = str(os.getenv('X_RapidAPI_Host'))
            api_key = str(os.getenv('X_RapidAPI_Key')) #This key is limited to 500 calls.

        except Exception as e:
            logging.error("Check that API key and host is provided in the bash script run-main.sh.")
            logging.error("Oops!", sys.exc_info()[0], "occurred.")
            logging.error("Exception: ", e)
            sys.exit(1) #crash

        conn = http.client.HTTPSConnection("yh-finance.p.rapidapi.com")

        headers = {
        'X-RapidAPI-Host': api_host,
        'X-RapidAPI-Key': api_key
        }
        conn.request("GET", f"/stock/v2/get-chart?interval=15m&symbol={stocksymbol}&range=1d&region=US", headers=headers)
        res = conn.getresponse()
        status = res.status # 200 for is found #302 not found
        logging.info(status)
        if status != 200:
            # TO-DO:
            # add check for different errors and throw exceptions
            logging.warning(f"Status code: {status}")
            #TO-DO: pop up GUI?
            return 0
        
        data = res.read() 
        result_json = json.loads( data.decode("utf-8")) #dump it in json
        timestamp = result_json["chart"]["result"][0]["timestamp"]#returns 40 timestamps as dict in format 0:1633515300 1:1633517100 2:1633518900
        logging.info(f"timestamp {timestamp}")
        open_stockprice = result_json["chart"]["result"][0]["indicators"]["quote"][0]["open"]
        logging.info(f"stockprice {open_stockprice}")
        self.graph_stock[0] = timestamp
        self.graph_stock[1] = open_stockprice

    def get_link(self, stocksymbol="TSLA"):
        """Gets uuid by searching API for specific stock.
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
