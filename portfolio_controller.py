
class PortfolioController():
    def __init__(self, user_object,DashboardControllerObject,
                 YahooAPIObject, StockController):
        #passed in objects
        self.user_object = user_object
        self.DashboardControllerObject = DashboardControllerObject
        self.YahooAPIObject = YahooAPIObject
        self.StockController=StockController
        #stock price dictionary key = stocksymbol value = price
        self.StockPriceDict = {}

    def CallUserToRemoveStock(self):
        pass
    def Createstock_controller_object(self):
        pass
    def get_stock_price_yahoo_api_object(self):
        """Get stockinfo dict from Yahoo API."""
        stocksymbol_list = self.user_object.return_users_stocksymbols()
        stockinfo = self.YahooAPIObject.get_stock_price_yahoo_api_object(stocksymbol_list)
        #extract just the stockprice associated with the stock
        for key in stockinfo:
            self.StockPriceDict[key] = stockinfo[key]["stockPrice"] 

    def create_portfolio_GUI_object(self):
        #get updated stockprice for each stock that will be displayed in GUI
        self.get_stock_price_yahoo_api_object()

    def CreateWatchListController(self):
        pass