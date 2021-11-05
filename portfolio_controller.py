from watchlist_controller import WatchlistController
from portfolio_GUI import PortfolioGUI
from stock_controller import StockController

class PortfolioController():
    def __init__(self, user_object,DashboardControllerObject,
                 YahooAPIObject, StockController, PopUpGUIObject):
        #passed in objects
        self.user_object = user_object
        self.DashboardControllerObject = DashboardControllerObject
        self.YahooAPIObject = YahooAPIObject
        self.StockController=StockController
        self.PopUpGUIObject = PopUpGUIObject
        #to be created objects
        self.WatchlistControllerObject = None
        self.portfolioGUI = None
        #stock price dictionary 
        self.stocksymbol_price_change_dict = {} 
        #ex: {"Stocksymbol":{"stockprice":"0.34", "percentage_change":23}, "OtherStocksymbol":{"stockprice":"0.22", "percentage_change":-44}}

        self.portfolio_value = 0 #int sum of each stock's stockprice*stockowned

    def calculate_portfolio_value(self):
        """Needs to be run after get_stock_price_yahoo_api_object.
        Gets the stock amount owned from user object and takes that times the current stock price."""
        self.portfolio_value = 0 
        for stocksymbol in self.stocksymbol_price_change_dict.keys():
            stockprice = self.stocksymbol_price_change_dict[stocksymbol]["stockprice"]
            stockowned = self.user_object.get_stockowned(stocksymbol)
            self.portfolio_value += (stockprice*stockowned)

    def calculate_percentage_change(self, stocksymbol):
        """I messed up and forgot to pull the percentage change from api. 
        But we can use get_chart method to pull stock value over the past 24 h to compute the percentage change."""
        stockchart = self.YahooAPIObject.get_stock_graph_values(stocksymbol) #2D list list1: 40 float x values and list2: 40 float y values #x values are float timestamps and y values are float stockprices"
        currentstock_price = float(stockchart[1][0]) # get first entry of stockprices
        stock_price_24h_ago = float(stockchart[1][39]) #get last entry of stockprices
        stock_price_change =  (currentstock_price-stock_price_24h_ago)/stock_price_24h_ago
        return stock_price_change*100 #percentage change of stock price over past 24 h

    def call_user_object_to_remove_stock(self, stocksymbol):
        """Removes stock from user object. Therefore it is removed from Portfolio"""
        successful = self.user_object.delete_stock(stocksymbol)
        if not successful: #if we programmed right this should never be exceuted
            self.create_popup_GUI("Oh no your stock could not be deleted.")
            
    def Create_stock_controller_object(self, stocksymbol):
        """Creates Stock Controller Object based on given stocksymbol"""
        self.StockController = StockController((stocksymbol,self.user_object, self.DashboardControllerObject, self.PopUpGUIObject, self.YahooAPIObject))

    def get_stock_price_yahoo_api_object(self):
        """Get stockinfo dict from Yahoo API. key = stocksymbol, value = current stock price"""
        #retrieve list of all users stocksymbols that will be put in the portfolio
        stock_symbol_list = self.user_object.return_users_stock_symbols()
        #get the stockinfo on each symbol >> here we need price
        stockinfo = self.YahooAPIObject.get_stock_price_yahoo_api_object(stock_symbol_list)
        #extract just the stockprice associated with the stock and get percentage change on stock over past 24h
        for key in stockinfo:
            percentage_change = self.calculate_percentage_change(stockinfo[key]) #retrieves percentage change over past 24h
            stockprice = stockinfo[key]["stockPrice"]
            self.stocksymbol_price_change_dict[key] = \
                {"stockprice":stockprice, "percentage_change": percentage_change} #updates self.StockPriceDict
        
    def create_portfolio_GUI_object(self):
        """Creates Portfolio GUI with """
        #get updated stockprice for each stock that will be displayed in GUI
        self.get_stock_price_yahoo_api_object()
        self.portfolioGUI = PortfolioGUI(self, self.stocksymbol_price_change_dict, self.portfolio_value)


    def CreateWatchListController(self):
        """Creates Watchlist Controlller Object"""
        self.WatchlistControllerObject = WatchlistController(self.user_object, self.YahooAPIObject,
                 self.popup_GUI_object,self.DashboardControllerObject)

    def create_popup_GUI(self, message):
        """creates a pop-up GUI with given error message."""
        self.popup_GUI_object.create_pop_up(message)
