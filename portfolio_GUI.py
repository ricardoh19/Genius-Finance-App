from tkinter import *
import tkinter as tk
from tkinter import ttk
import yahoo_api
import stock_controller
import dashboard_controller
import portfolio_controller
import watchlist_controller


class PortfolioGUI():
    def __init__(self, master, stocksymbol_price_change_dict, portfolio_value, userObject):
        self.master = master
        self.master.configure(background= "LightYellow")
        self.master.title("Portfolio")
        
        self.userObject = userObject
        self.portfolioControllerObject = portfolio_controller.PortfolioController(userObject)
        self.portfolio_value = portfolio_value
        self.createMainFrame(self.userObject)
        self.stocksymbol_price_change_dict = stocksymbol_price_change_dict
        self.yahoo_api_object = yahoo_api.YahooAPI()
        

    '''
    Intent: creates the main frame for the Portfolio GUI
    * Preconditions: master is connected to TKinter. 
    * createLoginFrame has the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for Portfolio is created
    '''
    def createMainFrame(self,userObject): 
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid", background="LightBlue1").grid(row=0,column=0, pady=5, padx=5)
        self.portfolioTitle = Label(self.master, text="My Stocks",font='Helvetica 12',height = 2, width = 13,borderwidth=2, relief="solid", background="LightBlue1").grid(row=1,column=1, pady=5, padx=5, sticky="sw")
        self.portfolioValueTitle = Label(self.master, text=f"Portfolio Value: {self.portfolio_value}",font='Helvetica 12',height = 2, width = 25,borderwidth=2, relief="solid", background="LightBlue1").grid(row=1,column=1, pady=5, padx=5, sticky="se")
        
        self.createMyStocksFrame(userObject)
        self.exitButton = Button(self.master,text="Exit", command=lambda:self.closeWindow(), background="red").grid(row = 4,column=1,sticky="se")
        
        #self.WatchlistButton = Button(self.master,text="Go to Watchlist", command=lambda:self.openWatchlist()).grid(row = 4,column=1,sticky="sw")
        
    
    '''
    Intent: creates the users stocks frame for the portfolio GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. user's stocks frame is created
    '''
    def createMyStocksFrame(self, userObject):
        self.tree = ttk.Treeview(self.master, column=("Stock_Symbol", "Shares_owned","Stock_Price"), show='headings', height=5)
        self.tree.grid(row = 2,column=1)

        self.tree.heading('Stock_Symbol', text='Stock Symbol')
        self.tree.heading('Stock_Price', text='Stock Price')
        self.tree.heading('Shares_owned', text='Shares Owned')
        
        self.yahoo_api_object = yahoo_api.YahooAPI()

    
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        curItem = self.tree.focus()


        stockSymbol = 'example'
        self.stockController = stock_controller.StockController(stockSymbol, userObject)

       
        
        for i in userObject.current_user_stocks:
            self.stockData = self.stockController.get_stock_data_API(i)
            try:
                self.stockPrice = self.stockData[i]['stockPrice']
                self.sharesOwned = userObject.current_user_stocks[i]['stockowned']
                self.tree.insert('', 'end', text=i, values=(i, self.sharesOwned, self.stockPrice))
            except KeyError:
                self.sharesOwned = userObject.current_user_stocks[i]['stockowned']
                self.tree.insert('', 'end', text=i, values=(i, self.sharesOwned, 'n/a'))
       
       
        

    def selectItem(self, a):
        curItem = self.tree.focus()
        stockSymbol = self.tree.item(curItem)['text']
        
        self.viewInformationButton = Button(self.master, text="View Information", command=lambda:self.viewInformation(stockSymbol)).grid(row = 4,column=1,sticky="sw",padx=120)
        self.removeButton = Button(self.master,text="Remove", command=lambda:self.removeStock(self.userObject, stockSymbol)).grid(row = 4,column=1,sticky="s",padx=150)


    '''
    Intent: 
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. 
    '''    
    def viewInformation(self, stockSymbol):
        self.stockController = stock_controller.StockController(stockSymbol, self.userObject)
        self.stockController.handle_viewInformation_event(stockSymbol, self.master)
    
    '''
    Intent: close the portfolio window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the portfolio window
    '''    
    def closeWindow(self):
        self.master.destroy()
        self.dashboardController = dashboard_controller.DashboardController(self.userObject)
        self.dashboardController.createDashboardGUI()

    def handlePortfolioValue(self):
        self.portfolioControllerObject.calculate_portfolio_value()

    '''
    Intent: remove stock from list of stocks in portfolio window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. removes stock from portfolio window
    '''            
    def removeStock(self, userObject, stockSymbol):
        del userObject.current_user_stocks[stockSymbol]
        self.tree.delete(*self.tree.get_children())
        for i in userObject.current_user_stocks:
            self.stockData = self.stockController.get_stock_data_API(i)
            try:
                self.stockPrice = self.stockData[i]['stockPrice']
                self.sharesOwned = userObject.current_user_stocks[i]['stockowned']
                self.tree.insert('', 'end', text=i, values=(i, self.sharesOwned, self.stockPrice))
            except KeyError:
                self.sharesOwned = userObject.current_user_stocks[i]['stockowned']
                self.tree.insert('', 'end', text=i, values=(i, self.sharesOwned, 'n/a'))
    
    '''
    Intent: creates a button on the frame that allows user to go to watchlist gui
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. allows user to go to watchlist gui from portfolio window
    '''  
    def openWatchlist(self):
        self.watchlistController = watchlist_controller.WatchlistController(self.userObject)
        self.watchlistController.create_watchlist_GUI()
        self.closeWindow()



