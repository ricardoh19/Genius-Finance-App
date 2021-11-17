from tkinter import *
import tkinter as tk
from tkinter import ttk
import dashboard_controller
import stock_controller
import webbrowser
from datetime import datetime
from PIL import ImageTk,Image 
import matplotlib.pyplot as plt



# this class controls the graphical user interface of the stock window. 
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
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid", background='LightBlue1')
        self.logo.grid(row=0,column=0, pady=5, padx=5)
        self.stockName= Label(self.master, text=self.stockSymbol,font='Helvetica 15',height = 2, width = 15,borderwidth=2, relief="solid", background= 'LightBlue1')
        self.stockName.grid(row=0,column=1, pady=5, padx=5,sticky="n")
        
        self.owned_frame = Frame(self.master, width = 400, height = 170,borderwidth=2, relief="sunken", background='LightBlue1')
        self.owned_frame.grid(row = 1,column=1)
        self.sharesOwned= Label(self.owned_frame, text="Shares Owned:",font='Helvetica 12',height = 2, width = 13,borderwidth=2, relief="solid", background="white")
        self.sharesOwned.grid(row=0,column=0, pady=5, padx=5)
        self.shares = Entry(self.owned_frame,width=4)
        self.shares.grid(row=0,column=1, pady=5, padx=5,ipady=4, ipadx=2)
        self.enter = Button(self.owned_frame,text="Enter",command=lambda:self.handleUpdateSharesOwned(self.shares.get()), background="lightgreen")
        self.enter.grid(row = 0,column=2)
        
        #middle of GUI
        self.createStockSummaryFrame()
        self.createGraphFrame()
        
        #bottom of GUI
        self.bottom_frame = Frame(self.master, width = 400, height = 170,borderwidth=2, relief="sunken", background='LightBlue1')
        self.bottom_frame.grid(row = 4,column=1)
        self.closeButton = Button(self.bottom_frame,text="Close", command=lambda:self.closeWindow(), background="red")
        self.closeButton.grid(row = 0,column=2,sticky="se")
        self.newsLink = Button(self.bottom_frame,text="Link to News article/articles", command=lambda:self.handleNewsLink(), background='LightBlue1')
        self.newsLink.grid(row = 0,column=1,sticky="s")
        self.addToPortfolio = Button(self.bottom_frame,text="Add to Portfolio",command=lambda:self.handleAddToPortfolio(), background="lightgreen")
        self.addToPortfolio.grid(row = 0,column=0,sticky="sw")

    '''
    Intent: creates the stock frame for the stock GUI
    * Preconditions: master is connected to TKinter. 
    * createPortfolioFrame, createSearchBarFrame, and createWatchlistFrame have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for stock is created
    '''
    def createStockSummaryFrame(self):
        self.stock = Frame(self.master, width = 400, height = 170,borderwidth=2, relief="sunken", background='LightBlue1')
        self.stock.grid(row = 2,column=1)
        self.stock_value = Label( self.stock, text="Stock Price: " + str(self.stockPrice), font='Helvetica 13 bold',borderwidth=1, relief="ridge", background="white")
        self.stock_value.grid(row = 0,column=0,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.current_ratio = Label( self.stock, text="Current Ratio: " + str(self.currentRatio), font='Helvetica 13 bold',borderwidth=1, relief="ridge", background="white")
        self.current_ratio.grid(row = 1,column=0,padx=30,pady=25,ipadx=5,ipady=5, sticky="ne")
        self.eps_rating = Label( self.stock, text="EPS Rating: " + str(self.epsRating), font='Helvetica 13 bold',borderwidth=1, relief="ridge", background="white")
        self.eps_rating.grid(row = 0,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="sw")
        self.debt_to_equity_ratio = Label( self.stock, text="Debt to Equity Ratio: " + str(self.debtToEquity), font='Helvetica 13 bold',borderwidth=1, relief="ridge", background="white")
        self.debt_to_equity_ratio.grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="se")

    def createGraphFrame(self):
        """
        stock controller graph values is set to zero if something went wrong in api call.
        In this case don't display the graph. 
        Just display an error message were the graph should be or something like that.
        """
        #TO-DO: put chart image inside of the frame 
        print('hi')
        #self.create_chart_image()
        image = Image.open("stockprice_chart.png")
        resize_image = image.resize((400, 300))
        img = ImageTk.PhotoImage(resize_image)
    
        panel = Label(self.master, image = img, width=400, height=300)
        panel.image = img
        panel.grid(row = 3,column=1)
        
    
  
    def handleNewsLink(self):
        website = self.stock_controllerObject.get_newslink_Yahoo_API(self.stockSymbol)

        if website == "Error could not retrieve a newslink.":
            message = f"Could not retrieve a newslink related to {self.stockSymbol}."
            self.popUpGUIObject = popupGUI.PopUpGUI(message)
            self.popUpGUIObject.createPopUp()
        
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
    Intent: 
    * Preconditions: 
    * Postconditions:
    * Post0. 
    '''    
    def handleUpdateSharesOwned(self, stockOwned):
        # use stock owned parameter
        self.stock_controllerObject.update_stock_owned(stockOwned)
        

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
        # plt.show()