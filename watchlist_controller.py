import watchlist_GUI
import yahoo_api
import popupGUI
import dashboard_controller
from tkinter import *

# this class controls the controller of the watchlist controller. Its methods include 
# get_stock_info_yahoo_api_object, calculate_stocks_percentage_change,
# calculate_percentage_change, , calculate_watchlist_stock_trend, create_watchlist_GUI.

class WatchlistController():
    def __init__(self, user_object):
        #passed in objects
        self.user_object = user_object
        self.YahooAPIObject = yahoo_api.YahooAPI()
        
        self.dashboardControllerObject = dashboard_controller.DashboardController(self.user_object)

        #to be calculated by calling methods in the class: 
        self.stockinfo = self.get_stock_info_yahoo_api_object() #get all stockinfo from Yahoo API    
        #self.StockPercentageChange = self.calculate_percentage_change()
        self.best_stocks = []
        self.worst_stocks = []  
        #self.calculate_watchlist_stock_trend()      
        #string: description
        self.description = "description"
        


    def get_stock_info_yahoo_api_object(self):
        """Get stockinfo dict from Yahoo API. key = stocksymbol, value = current stock price"""
        # Returns this:
        #   stockinfo[stock_symbol] = {
                #     "currentRatio": current_ratio,
                #     "trailingEPS": trailing_EPS,
                #     "PERatio":trailing_PE,
                #     "DebtToEquityRatio": debt_to_equity_ratio,
                #     "stockPrice": stockprice
                # } 
        #retrieve list of all users stocksymbols that will be put in the portfolio
        stock_symbol_list = self.user_object.return_users_stock_symbols()      
        #get the stockinfo on each symbol >> here we need price
        self.stockinfo = self.YahooAPIObject.get_stocks_info(stock_symbol_list)
        return self.stockinfo
        
  
    
    def calculate_stocks_percentage_change(self, stocksymbol):
        """I messed up and forgot to pull the percentage change from api. 
        But we can use get_chart method to pull stock value over the past 24 h to compute the percentage change."""
        stockchart = self.YahooAPIObject.get_stock_graph_values(stocksymbol) #2D list list1: 40 float x values and list2: 40 float y values #x values are float timestamps and y values are float stockprices"
        currentstock_price = float(stockchart[1][0]) # get first entry of stockprices
        stock_price_24h_ago = float(stockchart[1][-1]) #get last entry of stockprices
        stock_price_change =  (currentstock_price-stock_price_24h_ago)/stock_price_24h_ago
        return stock_price_change*100 #percentage change of stock price over past 24 h
        
    def calculate_percentage_change(self):
        '''calculates percentage change of each stock symbol in user object'''
        self.stockinfo = self.get_stock_info_yahoo_api_object()
        for stocksymbol in list(self.stockinfo):
            percentage_change = self.calculate_stocks_percentage_change(stocksymbol)
            self.stockinfo[stocksymbol]['PercentageChange'] = percentage_change
        return self.stockinfo

    def calculate_watchlist_stock_trend(self, stockinfo):
        """This function sorts the stocks according the percentage change.
        The best 3 stocks are added to best 3 stocks, the worst three in the worst 3 stocks.
        If there are less than 6 stocks they are divided into best and worst in the middle.
        If there are no stocks in the portfolio displays an error message in pop up gui."""
        self.best_stocks = []
        self.worst_stocks = []
        all_stocks = []
        #get a 2D list with stocksymbol and percentage change
        
        for stocksymbol in stockinfo.keys():
            all_stocks.append([stocksymbol, stockinfo[stocksymbol]['PercentageChange']])
        #sort stocks according to percentage change
        all_stocks = sorted(all_stocks, key=lambda x: x[1])
        print(all_stocks)
        #divide stocks into best and worst stocks.
        if len(all_stocks)> 0:
            self.best_stocks = [x[0] for x in all_stocks if x[1] >=0]    
            self.worst_stocks = [x[0] for x in all_stocks if x[1] <=0]  
            print(self.best_stocks)
            print(self.worst_stocks)
            
            
        #     self.best_stocks = [x[0] for x in all_stocks[0:3]]
        #     self.worst_stocks = [x[0] for x in all_stocks[-3:]]
        # elif len(all_stocks) > 0:
        #     middle = int(len(all_stocks)/2)
        #     self.best_stocks = [x[0] for x in all_stocks[0:middle]]
        #     self.worst_stocks = [x[0] for x in all_stocks[middle:]]            
        else: # if there are no stocks in portfolio error message
           print("Error no stocks in Portfolio.")
           self.popup_GUI_object = popupGUI.PopUpGUI("Error no stocks in Portfolio.")
           self.popup_GUI_object.createPopUp()

        return self.best_stocks, self.worst_stocks

    def create_watchlist_GUI(self):
        '''creates the watchlist GUI'''
        stockInfo = self.calculate_percentage_change()
        stocksTrendingUp,stocksTrendingDown = self.calculate_watchlist_stock_trend(stockInfo)
        
        description = None
        print(f"stocks trending up: {stocksTrendingUp}")
        print(f"stocks trending up: {stocksTrendingDown}")
        print(f"Stock info: {stockInfo}")

        
        

        root = Tk()
        root.geometry("750x600")
        self.portfolioGUI = watchlist_GUI.WatchlistGUI(root, self.user_object,stocksTrendingUp, 
        stocksTrendingDown, description, stockInfo )
        root.mainloop()
    

