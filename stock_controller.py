
class StockController():
    def __init__(self, StockSymbol, 
                 user_object, DashboardController, popup_GUI_object, yahoo_api_object):
        #Passed in objects:
        self.yahoo_api_object = yahoo_api_object
        self.user_object = user_object
        self.StockSymbol=StockSymbol
        self.DashboardController = DashboardController
        self.popup_GUI_object = popup_GUI_object

        self.StockName=StockName
        self.StockData = StockData
        self.StockGraph = StockGraph
        self.newslink = self.get_newslink_Yahoo_API()
        
        self.StockGUIObject = StockGUIObject
        
    
    def HandleSearchBarEvent(self, stocksymbol):
        #check if stock exists
        if self.yahoo_api_object.check_stock_exists(stocksymbol):
            #stock exists hence create stock_controller
            self.create_stock_controller(stocksymbol)
        else:
            #could not find stocksymbol
            message = "Could not find stock entered in search bar."
            self.create_popup_GUI(message)
        pass
    def GetStockGraphAPI():
        pass
    def GetStockDataAPI():
        pass
    def get_newslink_Yahoo_API(self):
        """Returns newslink retreieved from Yahoo API Object"""
        return self.yahoo_api_object.get_link(self.StockSymbol)
        
    def OpenDashboard():
        pass
    def create_stock_GUI(self):
        pass
    def AddStockInUserClass():
        pass
    def CreatePopUpGUI():
        pass
    