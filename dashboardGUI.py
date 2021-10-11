
class DashboardGUI():
    def __init__(self, DashboardControllerObject,popup_GUI_object):
        self.DashboardControllerObject = DashboardControllerObject
        self.popup_GUI_object = popup_GUI_object

    def handle_logout_event(self):
        """Logout button is pressed. 
        Tells Dashboard controller to do logout processing"""
        self.DashboardControllerObject.handle_logout_event()
        #TO:DO frame destroyed

    def handle_searchbar_event(self):
        """Gets stocksymbol selected and passes it on 
        to dashboard controller for processing."""
        stocksymbol = "" #ToDo
        #call Dashboard controller function to process search bar stocksymbol
        self.DashboardControllerObject.handle_search_bar_event(stocksymbol)
    
    def handle_watchlist_event():

        pass
    def handle_portfolio_event(self):
        """Calls Dashboard Controller to create portfolio"""
        self.DashboardControllerObject.create_portfolio_controller()

    def CreateMainFrame():
        pass
    def CreateSearchbarFrame():
        pass
    def CreateWatchlistPortfolioFrame():
        pass
    