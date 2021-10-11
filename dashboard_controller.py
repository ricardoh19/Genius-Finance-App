from stock_controller import StockController
from yahoo_api import YahooAPI
class DashboardControllers():
    def __init__(self, LoginLogoutController, WatchlistObject, 
                 PortfolioObject, DashboardGUIObject, PopUpGUIObject):
        self.LoginLogoutController = LoginLogoutController
        self.WatchlistObject = WatchlistObject
        self.StockObject= None #replaced by stock object
        self.PortfolioObject = PortfolioObject
        self.DashboardGUIObject = DashboardGUIObject
        self.PopUpGUIObject = PopUpGUIObject
        self.yahoo_api_object = self.create_yahoo_api()
    
    def handle_logout_event(self):
        self.LoginLogoutController

        pass
    def create_stock_controller(stocksymbol):
        class StockController():
    # def __init__(self, StockSymbol, 
    #              UserObject, DashboardController, PopUpGUIObject):
        stock_controller_object = StockController(stocksymbol, self)


    def CreatePortfolioController():
        pass
    def CreateDashboardGUI():
        pass
    def create_yahoo_api(self):
        yahoo_api_object = YahooAPI()
        return yahoo_api_object

    def HandleSearchBarEvent(self, stocksymbol):
        if self.yahoo_api_object:
            self.create_stock_controller(stocksymbol)
        else:
            message = "Could not find stock entered in search bar."
            self.create_popup_GUI(message)


    def create_popup_GUI(self, message):
        pass
      