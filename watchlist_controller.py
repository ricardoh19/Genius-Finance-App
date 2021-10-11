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
        self.StockTrendingUp = self.calculate_watchlist_stock_trending_up()
        self.StocksTrendingDown = self.calculate_watchlist_stock_trending_up()
        self.StockPercentageChange = self.calculate_percentage_change()
        #string: description
        self.description = "description"
        
        self.WatchlistGUIObject= self.create_watchlist_GUI()

        
    def calculate_percentage_change(self):
        pass
    def calculate_watchlist_stock_trending_up(self):
        pass
    def calculate_watchlist_stock_trending_down(self):
        pass
    def control_to_stock_controller_object(self):
        pass
    def create_watchlist_GUI(self):
        return WatchlistGUI(self, self.popup_GUI_object, self.StockTrendingUp,
                 self.StocksTrendingDown, self.description, self.StockPercentageChange)
    
