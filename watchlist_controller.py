from watchlist_GUI import WatchlistGUI

class WatchlistController():
    def __init__(self, user_object, YahooAPIObject,
                 popup_GUI_object,DashboardControllerObject):
        #passed in objects
        self.user_object = user_object
        self.YahooAPIObject = YahooAPIObject
        self.popup_GUI_object = popup_GUI_object
        self.DashboardControllerObject = DashboardControllerObject

        #to be calculated by calling methods in the class: 
        self.get_stock_info_yahoo_api_object() #get all stockinfo from Yahoo API    
        self.StockPercentageChange = self.calculate_percentage_change()
        self.best_stocks = []
        self.worst_stocks = []  
        self.calculate_watchlist_stock_trend()      
        #string: description
        self.description = "description"
        
        self.WatchlistGUIObject= self.create_watchlist_GUI()


    def get_stock_info_yahoo_api_object(self):
        """Get stockinfo dict from Yahoo API. key = stocksymbol, value = current stock price"""
        #retrieve list of all users stocksymbols that will be put in the portfolio
        stock_symbol_list = self.user_object.return_users_stock_symbols()      
        #get the stockinfo on each symbol >> here we need price
        self.stockinfo = self.YahooAPIObject.get_stock_price_yahoo_api_object(stock_symbol_list)
        # Returns this:
        #   stockinfo[stock_symbol] = {
                #     "currentRatio": current_ratio,
                #     "trailingEPS": trailing_EPS,
                #     "PERatio":trailing_PE,
                #     "DebtToEquityRatio": debt_to_equity_ratio,
                #     "stockPrice": stockprice
                # } 
  
    
    def calculate_stocks_percentage_change(self, stocksymbol):
        """I messed up and forgot to pull the percentage change from api. 
        But we can use get_chart method to pull stock value over the past 24 h to compute the percentage change."""
        stockchart = self.YahooAPIObject.get_stock_graph_values(stocksymbol) #2D list list1: 40 float x values and list2: 40 float y values #x values are float timestamps and y values are float stockprices"
        currentstock_price = float(stockchart[1][0]) # get first entry of stockprices
        stock_price_24h_ago = float(stockchart[1][39]) #get last entry of stockprices
        stock_price_change =  (currentstock_price-stock_price_24h_ago)/stock_price_24h_ago
        return stock_price_change*100 #percentage change of stock price over past 24 h
        
    def calculate_percentage_change(self):
        for stocksymbol in self.stockinfo.keys():
            percentage_change = self.calculate_percentage_change(stocksymbol)
            self.stockinfo['PercentageChange'] = percentage_change

    def calculate_watchlist_stock_trend(self):
        """This function sorts the stocks according the percentage change.
        The best 3 stocks are added to best 3 stocks, the worst three in the worst 3 stocks.
        If there are less than 6 stocks they are divided into best and worst in the middle.
        If there are no stocks in the portfolio displays an error message in pop up gui."""
        self.best_stocks = []
        self.worst_stocks = []
        all_stocks = []
        #get a 2D list with stocksymbol and percentage change
        for stocksymbol in self.stockinfo.keys():
            all_stocks.append([stocksymbol, self.stockinfo[stocksymbol]['PercentageChange']])
        #sort stocks according to percentage change
        all_stocks = sorted(all_stocks, key=lambda x: x[1])
        print(all_stocks)
        #divide stocks into best and worst stocks.
        if len(all_stocks)> 6: 
            self.best_stocks = [x[0] for x in all_stocks[0:3]]
            self.worst_stocks = [x[0] for x in all_stocks[-3:]]
        elif len(all_stocks) > 0:
            middle = int(len(all_stocks)/2)
            self.best_stocks = [x[0] for x in all_stocks[0:middle]]
            self.worst_stocks = [x[0] for x in all_stocks[middle:]]            
        else: # if there are no stocks in portfolio error message
           print("Error no stocks in Portfolio.")
           self.create_popup_GUI("Error no stocks in Portfolio.")
                 
    def create_watchlist_GUI(self):
        return WatchlistGUI(self, self.popup_GUI_object, self.StockTrendingUp,
                 self.StocksTrendingDown, self.description, self.StockPercentageChange)
    
    def create_popup_GUI(self, message):
        """creates a pop-up GUI with given error message."""
        self.popup_GUI_object.create_pop_up(message)

