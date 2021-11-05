from stock_controller import StockController
from yahoo_api import YahooAPI
from tkinter import *
import loginlogout_controller,dashboardGUI
from portfolio_controller import PortfolioController
from watchlist_controller import WatchlistController
from dashboardGUI import DashboardGUI
import user
from popupGUI import PopUpGUI

class DashboardController():
    """This class is the intersection of App traffic after login. """
    def __init__(self):
        self.loginlogout_controller = loginlogout_controller.LoginLogoutControllers()
        #self.user_object = user.User()
        #created in this class objects
        self.watchlist_object = None 
        self.stock_controller_object= None #replaced by stock object
        self.portfolio_object = None
        #created during initialization object
        self.yahoo_api_object = YahooAPI() # is created
    
    
    def logOutPushChanges(self):
        """In Dashboard GUI logout button is pressed.
        The controller passes the control back to login/logout controller.
        Login logout controller function is called which pushes the changes to the database"""
        self.loginlogout_controller.logout_push_changes_to_database()
        
    def create_portfolio_controller(self):
        """if portfolio controller object does not exist create it.
        calls method in Portfolio Controller to create Portfolio GUI."""
        if self.portfolio_object == None:
           self.portfolio_object =  PortfolioController(self.user_object,self,self.yahoo_api_object, self.stock_controller_object, self.yahoo_api_object) 
        self.portfolio_object.create_portfolio_GUI_object()
        





    def create_stock_controller(self, stock_symbol):
        """if stock controller object does not exist creates it.
        Function calls Stock Controller Object function: create stock gui"""
        if self.stock_controller_object == None:
            self.stock_controller_object = StockController(stock_symbol, self.user_object, self, self.popup_GUI_object)
        self.stock_controller_object.create_stock_GUI()

    def create_watchlist_controller(self):
        """if portfolio controller object does not exist create it.
        calls method in Portfolio Controller to create Portfolio GUI."""
        if self.watchlist_object == None:
            self.watchlist_object = WatchlistController(self.user_object, self.yahoo_api_object,
                 self.popup_GUI_object,self)
        #call watchlist GUI in Watchlist controller
        
    def create_portfolio_controller(self):
        """if portfolio controller object does not exist create it.
        calls method in Portfolio Controller to create Portfolio GUI."""
        if self.portfolio_object == None:
           self.portfolio_object =  PortfolioController(self.user_object,self,self.yahoo_api_object, self.stock_controller_object, self.yahoo_api_object) 
        self.portfolio_object.create_portfolio_GUI_object()
        
    
    def createDashboardGUI(self):
        """This function creates the Dashboard GUI Object"""
        #self.DashboardGUIObject.create
        root = Tk()
        root.geometry("675x600")
        self.dashboardGUIObject = DashboardGUI(root)
        root.mainloop()

    def searchStockSymbol(self, stock_symbol):
        """Checks if the stock_symbol given in the search bar actually exists.
        If it exists turns over control to Stock controller.
        If it doesn't exist create a pop-up GUI with error message."""
        #check if stock exists
        if self.yahoo_api_object.check_stock_exists(stock_symbol):
            #stock exists hence create stock_controller
            self.create_stock_controller(stock_symbol)
        else:
            #could not find stock_symbol
            popupGUI = PopUpGUI("Could not find stock entered in search bar.")
            popupGUI.createPopUp()

    
      