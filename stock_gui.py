from tkinter import *
import tkinter as tk
from tkinter import ttk

import stock_controller
# this class controls the graphical user interface of the stock window. 
class StockGUI():
    def __init__(self,master):
        self.stock_controllerObject = stock_controller.StockController()
        self.master = master
        self.master.title("Stock")
        self.createMainFrame()
    '''
    Intent: creates the main frame for the stock GUI
    * Preconditions: master is connected to TKinter. 
    * createPortfolioFrame, createSearchBarFrame, and createWatchlistFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for stock is created
    '''
    def create_main_frame():
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=0, pady=5, padx=5)
        self.stockName= Label(self.master, text="Stock Name"+"(STNM)",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5)
        self.sharesOwned= Label(self.master, text="Shares Owned:",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=1,column=1, pady=5, padx=5)
        self.shares = Entry(self.master)
        self.shares.grid(row = 1,column=2,padx=8,pady=15,ipadx=2,ipady=2)
        self.enter = Button(self.master,text="Enter").grid(row = 1,column=3)
        
        #middle of GUI
        self.createStockSummaryFrame()
        self.create_graph_frame()
        
        #bottom of GUI
        self.closeButton = Button(self.master,text="Close", command=lambda:self.closeWindow()).grid(row = 4,column=1,sticky="se")
        self.newsLink = Button(self.master,text="Link to News article/articles").grid(row = 4,column=1,sticky="s")
        self.addToPortfolio = Button(self.master,text="Add to Portfolio").grid(row = 4,column=1,sticky="sw")

    '''
    Intent: creates the stock frame for the stock GUI
    * Preconditions: master is connected to TKinter. 
    * createPortfolioFrame, createSearchBarFrame, and createWatchlistFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for stock is created
    '''
    def createStockSummaryFrame():
        self.stock = Frame(self.master, width = 350, height = 170,borderwidth=2, relief="sunken").grid(row = 1,column=1)
        self.stock_value = Label( self.stock, text="Stock Price:",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.current_ratio = Label( self.stock, text="Current Ratio:",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="w")
        self.eps_rating = Label( self.stock, text="EPS Rating:",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="sw")
        self.debt_to_equity_ratio = Label( self.stock, text="Debt to Equity Ratio:",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="e")

    def create_graph_frame():
        """
        stock controller graph values is set to zero if something went wrong in api call.
        In this case don't display the graph. 
        Just display an error message were the graph should be or something like that.
        """
        self.graph = Frame(self.master, width = 350, height = 170,borderwidth=2, relief="sunken").grid(row = 2,column=2)
        #will add graph once we figure out how to convert timeseries and stock price 
    
    


    
    