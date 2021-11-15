from tkinter import *
import tkinter as tk
from tkinter import ttk
import dashboard_controller
import stock_controller
import webbrowser
from datetime import datetime
import matplotlib.pyplot as plt
# this class controls the graphical user interface of the stock window. 

# Why do some controller need popupgui object , other controllers as parameters?


class StockGUI():
    def __init__(self, master, stock_symbol, stockData, stock_graph_values, newslink, userObject):
        self.stock_controllerObject = stock_controller.StockController(stock_symbol, userObject)
        self.dashboard_controllerObject = dashboard_controller.DashboardController(userObject)
        self.master = master
        self.master.title("Stock")
        self.userObject = userObject
        self.stockSymbol = stock_symbol
        self.stockData = stockData
       
        self.stockPrice = self.stockData[self.stockSymbol]['stockPrice']
        self.currentRatio = self.stockData[self.stockSymbol]['currentRatio']
        self.epsRating = self.stockData[self.stockSymbol]['trailingEPS']
        self.debtToEquity = self.stockData[self.stockSymbol]['DebtToEquityRatio']

    
        self.stock_graph_values = stock_graph_values
        self.newsLink = newslink
        self.createMainFrame()

    '''
    Intent: creates the main frame for the stock GUI
    * Preconditions: master is connected to TKinter. 
    * createPortfolioFrame, createSearchBarFrame, and createWatchlistFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for stock is created
    '''
    def createMainFrame(self):
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=0, pady=5, padx=5)
        self.stockName= Label(self.master, text=self.stockSymbol,font='Helvetica 15',height = 2, width = 15,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5,sticky="n")
        
        self.sharesOwned= Label(self.master, text="Shares Owned:",font='Helvetica 12',height = 2, width = 13,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5,sticky="sw")
        self.shares = Entry(self.master,width=4)
        self.shares.grid(row=0,column=1, pady=5, padx=5,ipady=4, ipadx=2, sticky="s")
        self.enter = Button(self.master,text="Enter").grid(row = 0,column=1,sticky="se")
        
        #middle of GUI
        self.createStockSummaryFrame()
        self.createGraphFrame()
        
        #bottom of GUI
        self.closeButton = Button(self.master,text="Close", command=lambda:self.closeWindow()).grid(row = 4,column=1,sticky="se")
        self.newsLink = Button(self.master,text="Link to News article/articles", command=lambda:self.handleNewsLink())
        self.newsLink.grid(row = 4,column=1,sticky="s")
        self.addToPortfolio = Button(self.master,text="Add to Portfolio",command=lambda:self.handleAddToPortfolio()).grid(row = 4,column=1,sticky="sw")

    '''
    Intent: creates the stock frame for the stock GUI
    * Preconditions: master is connected to TKinter. 
    * createPortfolioFrame, createSearchBarFrame, and createWatchlistFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for stock is created
    '''
    def createStockSummaryFrame(self):
        self.stock = Frame(self.master, width = 400, height = 170,borderwidth=2, relief="sunken").grid(row = 1,column=1)
        self.stock_value = Label( self.stock, text="Stock Price: " + str(self.stockPrice), font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.current_ratio = Label( self.stock, text="Current Ratio: " + str(self.currentRatio), font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="w")
        self.eps_rating = Label( self.stock, text="EPS Rating: " + str(self.epsRating), font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="sw")
        self.debt_to_equity_ratio = Label( self.stock, text="Debt to Equity Ratio: " + str(self.debtToEquity), font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="e")

    def createGraphFrame(self):
        """
        stock controller graph values is set to zero if something went wrong in api call.
        In this case don't display the graph. 
        Just display an error message were the graph should be or something like that.
        """
        self.graph = Frame(self.master, width = 415, height = 170,borderwidth=2, relief="sunken").grid(row = 2,column=1, padx=15, pady=20)
        #TO-DO: put chart image inside of the frame 
    
    '''
    Intent: 
    * Preconditions: 
    * Postconditions:
    * Post0. 
    '''    
    def handleNewsLink(self):
        website = self.stock_controllerObject.get_newslink_Yahoo_API(self.stockSymbol)
        webbrowser.open(website)

    '''
    Intent: 
    * Preconditions: 
    * Postconditions:
    * Post0. 
    '''    
    def handleAddToPortfolio(self):
        self.stock_controllerObject.add_stock_in_user_class()
        

    '''
    Intent: close the portfolio window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the portfolio window
    '''    
    def closeWindow(self):
        self.master.destroy()
        self.dashboard_controllerObject.createDashboardGUI()
 
    def convert_timestamp(self, timestamp_list):
        """Takes in list of timestamps and converts each timestamp into a datetime object."""
        dt_objects = []
        for timestamp in timestamp_list:
            dt_object = datetime.fromtimestamp(timestamp)
            # print(dt_object)
            # print(dt_object.hour)
            # print(dt_object.minute)
            # print(dt_object.day)
            
            dt_objects.append(dt_object.hour +dt_object.minute/60)
        print(dt_objects)
        return dt_objects
    
    def create_chart_image(self):
        """"Turns the given data into an image and saves that image"""
        hour_list = self.convert_timestamp(self.stock_graph_values[0])

        # Data for plotting
        x = hour_list # time: list of hours
        y = self.stock_graph_values[1] #stockprices list

        fig, ax = plt.subplots()
        ax.plot(x, y)
        #name axis and set title
        ax.set(xlabel='time in hours', ylabel='stockprice in USD',
            title='Stockprice over the past 24 hours.')
        ax.grid()
        #save chart as image
        fig.savefig("stockprice_chart.png")
        plt.show()