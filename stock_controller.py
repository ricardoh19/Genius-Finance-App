
class StockController():
    def __init__(self, StockName, StockSymbol, StockData, StockGraph,
                 UserObject, StockGUIObject, DashboardController,PopUpGUIObject):
        self.StockName=StockName
        self.StockSymbol=StockSymbol
        self.StockData = StockData
        self.StockGraph = StockGraph
        self.UserObject = UserObject
        self.StockGUIObject = StockGUIObject
        self.DashboardController = DashboardController
        self.PopUpGUIObject = PopUpGUIObject
    
    def HandleSearchBarEvent():
        pass
    def GetStockGraphAPI():
        pass
    def GetStockDataAPI():
        pass
    def GetNewslinkAPI():
        pass
    def OpenDashboard():
        pass
    def CreateStockGUI():
        pass
    def AddStockInUserClass():
        pass
    def CreatePopUpGUI():
        pass
    