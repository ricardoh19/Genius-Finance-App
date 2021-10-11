
class WatchlistControllers():
    def __init__(self, StocksTrendingUp, StocksTrendingDown, StockPercentageChange,
                 description, UserObject, YahooAPIObject, WatchlistGUIObject,
                 PopUpGUIObject,DashboardControllerObject):
        self.StockTrendingUp = StocksTrendingUp
        self.StocksTrendingDown = StocksTrendingDown
        self.StockPercentageChange = StockPercentageChange
        self.description = description
        self.UserObject = UserObject
        self.YahooAPIObject = YahooAPIObject
        self.WatchlistGUIObject= WatchlistGUIObject
        self.PopUpGUIObject = PopUpGUIObject
        self.DashboardControllerObject = DashboardControllerObject
        
    def CalculatePercentageChange():
        pass
    def CalculateWatchlistStockTrendingUp():
        pass
    def CalculateWatchlistStockTrendingDown():
        pass
    def CreateStockControllerObject():
        pass
    
