import http.client
import json
import os
import sys 
import logging

class YahooAPI():
    def __init__(self, stocksymbol="AMRN"):
        self.stockprice = ""
        self.graph_stock = [[], []] #2D list x and y values
        self.newslink = ""
        logging.debug("Created Yahoo API Object.")

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
        print(type(status))
        if status != 200:
            logging.warning(f"Stock {stocksymbol} not found. Status code: {status}")
            return 0
        print(status)
        print(res) #<http.client.HTTPResponse object at 0x102d00a60>
        data = res.read()
        # print(data)
        sys.exit(0)
        logging.debug(data.decode("utf-8"))
        result_json = json.loads( data.decode("utf-8"))
        logging.debug(result_json)
        return result_json

    def get_stocks_info(self, stocksymbollist=["AAAA"]):
        stockinfo ={} #remove old data
        for stocksymbol in stocksymbollist:
            stock_summary = self.get_stock_summary(stocksymbol)
            stockprice = stock_summary["price"]["regularMarketOpen"]["raw"] #Nasdaq Real Time Price
            stockprice2 = stock_summary["financialData"]["currentPrice"]["raw"]
            logging.debug(f"stockprice {stockprice}, {stockprice2}")
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
    def get_watchlist_info(self, stocksymbollist= ["AAAA"]):
        """This function takes a list with stocksymbols,
        it returns a dictionary with stocksymbol as keys and all ratios and info as values."""
        return self.get_stocks_info(stocksymbollist)

    def GetStockInfo(self, stocksymbol):
        return self.get_stocks_info([stocksymbol])
        
    def GetStockGraph(self):
        pass
    def GetNewsLink(self):
        pass
    def check_stock_exists(self, stocksymbol):
        """Checks against API if stock exists"""
        stockinfo = self.get_stock_summary()
        if stockinfo == 0:
            return False
        else:
            return True
