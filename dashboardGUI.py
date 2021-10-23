from tkinter import *
import tkinter as tk
from tkinter import ttk
import dashboard_controller


class DashboardGUI():
    def __init__(self, master):
        self.dashboardControllerObject = dashboard_controller.DashboardController()
        #self.popup_GUI_object = popup_GUI_object
        self.master = master
        self.master.title("Dashboard")
        self.createMainFrame()

    '''
    Intent: creates the main frame for the dashboard GUI
    * Preconditions: master is connected to TKinter. 
    * createWatchlistPortfolioFrame and createSearchbarFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for dashboard is created
    '''
    def createMainFrame(self):
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=0, pady=5, padx=5)
        self.createWatchlistPortfolioFrame()
        self.createSearchbarFrame()
        self.exitButton = Button(self.master,text="Exit", command=lambda:self.closeWindow()).grid(row = 4,column=1,sticky="se")

    
    '''
    Intent: creates the search bar frame for the login GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. search bar frame is created.
    '''
    def createSearchbarFrame(self):
        self.inputtxt = Text(self.master, height = 2, width = 25, bg = "light yellow").grid(row = 2,column=4,sticky="ne")


    '''
    Intent: creates the watchlist frame for the login GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. watchlist frame is created.
    '''
    def createWatchlistPortfolioFrame(self):
        pass


    """Logout button is pressed. 
    Tells Dashboard controller to do logout processing"""
    def handleLogoutEvent(self):
        self.DashboardControllerObject.handleLogoutEvent()
        self.closeWindow()
        self.loginlogout_ControllerObject.createLoginGUI()

    def handle_watchlist_event(self):
        pass
    def handle_portfolio_event(self):
        """Calls Dashboard Controller to create portfolio"""
        self.DashboardControllerObject.create_portfolio_controller()

    def handle_searchbar_event(self):
        """Gets stock_symbol selected and passes it on 
        to dashboard controller for processing."""
        stock_symbol = "" #ToDo
        #call Dashboard controller function to process search bar stock_symbol
        self.DashboardControllerObject.handle_search_bar_event(stock_symbol)

    def closeWindow(self):
        self.master.destroy()