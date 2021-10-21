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


    def createMainFrame(self):
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=0, pady=5, padx=5)
        self.createWatchlistPortfolioFrame()
        self.exitButton = Button(self.master,text="Exit", command=lambda:self.closeWindow()).grid(row = 4,column=1,sticky="se")

    
    def createSearchbarFrame(self):
        pass

    def createWatchlistPortfolioFrame(self):
        self.buttons= Frame(self.master, width = 500, height = 400, borderwidth=2, relief="sunken").grid(row = 1,column=1,pady=4)

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