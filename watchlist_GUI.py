from tkinter import *
import tkinter as tk
from tkinter import ttk
import yahoo_api

import stock_controller

# this class controls the graphical user interface of the watchlist GUI. Its methods include 
# createMainFrame, StockTrendFrame, selectItem, viewInformation, closeWindow.
class WatchlistGUI():
    def __init__(self, master, userObject, stocksTrendingUp,
                 stocksTrendingDown, description, stockInfo):
        self.master = master
        self.master.title("Watchlist")
        self.userObject = userObject

        self.stocksTrendingDown = stocksTrendingDown # list
        self.stocksTrendingUp = stocksTrendingUp # list
        self.description = description
        self.stockInfo = stockInfo # dict
        self.createMainFrame(userObject)
    


    '''
    Intent: creates the main frame for the watchlist GUI
    * Preconditions: master is connected to TKinter. 
    * createLoginFrame has the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for watchlist is created
    '''
    def createMainFrame(self,userObject): 
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=0, pady=5, padx=5)
        self.portfolioTitle = Label(self.master, text="Stocks to Watch",font='Helvetica 12',height = 2, width = 13,borderwidth=2, relief="solid").grid(row=1,column=1, pady=5, padx=5, sticky="s")
        self.StockTrendFrame(userObject)
        self.exitButton = Button(self.master,text="Exit", command=lambda:self.closeWindow()).grid(row = 4,column=1,sticky="se")
        
        
    
    def fixed_map(self,option):
        # Returns the style map for 'option' with any styles starting with
        # ("!disabled", "!selected", ...) filtered out

        # style.map() returns an empty list for missing options, so this should
        # be future-safe
        style = ttk.Style()
        return [elm for elm in style.map("Treeview", query_opt=option)
            if elm[:2] != ("!disabled", "!selected")]

    '''
    Intent: creates the stock table frame for the watchlist GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. stock table frame is displayed.
    '''
    def StockTrendFrame(self, userObject):
        style = ttk.Style()
        style.map("Treeview", 
        foreground=self.fixed_map("foreground"),
        background=self.fixed_map("background"))

        self.tree = ttk.Treeview(self.master, column=("Stock_Symbol", "percentage_change","description"), show='headings', height=5)
        self.tree.grid(row = 2,column=1)
        self.tree.heading('Stock_Symbol', text='Stock Symbol')
        self.tree.heading('percentage_change', text='Percentage Change')
        self.tree.heading('description', text='Description')
        self.yahoo_api_object = yahoo_api.YahooAPI()

        curItem = self.tree.focus()

        # insert stocks trending UP
        for i in self.stocksTrendingUp:
            try:
                self.tree.insert('', 'end', text=i, values=(i, f"{round(self.stockInfo[i]['PercentageChange'], 1)}%", "Stock is trending up."),tags = ('up'))
            except KeyError:
                self.tree.insert('', 'end', text=i, values=(i, f"{round(self.stockInfo[i]['PercentageChange'], 1)}%", 'Stock is trending up.'),tags = ('up'))

        # insert stocks trending DOWN
        for i in self.stocksTrendingDown:
            try:
                self.tree.insert('', 'end', text=i, values=(i, f"{round(self.stockInfo[i]['PercentageChange'], 1)}%", "Stock is trending down."),tags = ('down'))
            except KeyError:
                self.tree.insert('', 'end', text=i, values=(i, f"{round(self.stockInfo[i]['PercentageChange'], 1)}%", 'Stock is trending down.'),tags = ('down'))

        self.tree.tag_configure('up', background='green')
        self.tree.tag_configure('down', background='red')
        

    

  
    
    '''
    Intent: close the portfolio window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the portfolio window
    '''    
    def closeWindow(self):
        self.master.destroy()

    
    
    