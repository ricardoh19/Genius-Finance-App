from tkinter import *
import tkinter as tk
from tkinter import ttk
import dashboard_controller
import loginlogout_controller
import portfolio_controller

#  this class controls the graphical user interface of the dashboard window. Its methods include 
# createSearchbarFrame, createWatchlistPortfolioFrame,
# handleWatchlistEvent, handlePortfolioEvent, handleSearchbarEvent, closeWindow.
class DashboardGUI():
    def __init__(self, master,userObject):
        self.dashboardControllerObject = dashboard_controller.DashboardController(userObject)
        self.loginlogout_ControllerObject = loginlogout_controller.LoginLogoutControllers()
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
        self.exitButton = Button(self.master,text="Log Out", command=lambda:self.handleLogoutEvent()).grid(row = 4,column=1,sticky="se")

    
    '''
    Intent: Creates the search bar frame for the login GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. search bar label and entry box is created.
    '''
    def createSearchbarFrame(self):
        self.logo = Label(self.master, text="Search for stock (SYMBOL): ",font='Helvetica 12').grid(row = 0,column=1,sticky="n",pady=50)
        self.inputtxt = Text(self.master, height = 2, width = 25, bg = "light yellow").grid(row = 0,column=1,sticky="e")


    '''
    Intent: creates the frame that contains the watchlist and portfolio for the dashboard GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. frame that contains the watchlist and portfolio is created
    '''
    def createWatchlistPortfolioFrame(self):
        self.watchListPortfolioFrame = Frame(self.master, width = 450, height = 200,borderwidth=2, relief="sunken").grid(row = 2,column=1)
        self.watchlistLabel = Button( self.watchListPortfolioFrame, text="Watchlist",font='Helvetica 13 bold',borderwidth=1, relief="ridge")
        self.watchlistLabel.grid(row = 2,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="w")
        self.portoflioLabel = Button( self.watchListPortfolioFrame, text="Portoflio", command=lambda:self.handlePortfolioEvent(), font='Helvetica 13 bold',borderwidth=1, relief="ridge")
        self.portoflioLabel.grid(row=2, column=1,padx=30,pady=25, ipadx=5,ipady=5,sticky="e")


    '''
    Intent: handles the logic for the user clicking the watchlist button.
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. 
    '''
    def handleWatchlistEvent(self):
        pass

    '''
    Intent: handles the logic for the user clicking portfolio button.
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. 
    '''
    def handlePortfolioEvent(self):
        """Calls Dashboard Controller to create portfolio"""
        self.dashboardControllerObject.create_portfolio_controller()


    '''
    Intent: handles the logic for the user clicking Search button after enterting information into search bar.
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. 
    '''
    def handleSearchbarEvent(self):
        """Gets stock_symbol selected and passes it on 
        to dashboard controller for processing."""
        stock_symbol = "" #ToDo
        #call Dashboard controller function to process search bar stock_symbol
        self.DashboardControllerObject.handle_search_bar_event(stock_symbol)


    '''
    Intent: handles the logic for the user clicking logout button.
    * Preconditions: 
    * Postconditions:
    * Post0. 
    '''
    def handleLogoutEvent(self):
        self.dashboardControllerObject.logOutPushChanges()
        self.closeWindow()
        self.loginlogout_ControllerObject.createLoginGUI()
        
    

    '''
    Intent: close the dashboard window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the dashboard window
    '''
    def closeWindow(self):
        self.master.destroy()

