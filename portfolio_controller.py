
class PortfolioController():
    def __init__(self, user_object,DashboardControllerObject,
                 YahooAPIObject, StockController):
        #passed in objects
        self.user_object = user_object
        self.DashboardControllerObject = DashboardControllerObject
        self.YahooAPIObject = YahooAPIObject
        self.StockController=StockController
        #stock price dictionary key = stock_symbol value = price
        self.StockPriceDict = {}

    def call_user_object_to_remove_stock(self):
        pass
    def Createstock_controller_object(self):
        pass
    def get_stock_price_yahoo_api_object(self):
        """Get stockinfo dict from Yahoo API."""
        stock_symbol_list = self.user_object.return_users_stock_symbols()
        stockinfo = self.YahooAPIObject.get_stock_price_yahoo_api_object(stock_symbol_list)
        #extract just the stockprice associated with the stock
        for key in stockinfo:
            self.StockPriceDict[key] = stockinfo[key]["stockPrice"] 

    def create_portfolio_GUI_object(self):
        #get updated stockprice for each stock that will be displayed in GUI
        self.get_stock_price_yahoo_api_object()

    def CreateWatchListController(self):
        pass

    def create_popup_GUI(self, message):
        """creates a pop-up GUI with given error message."""
        self.popup_GUI_object.create_pop_up(message)