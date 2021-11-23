import stock_gui
import yahoo_api
import dashboard_controller
import popupGUI
from tkinter import *

class StockController():
    """Stock controller class is created from dashboard controller 
    and processes user actions passed in from stock controller GUI.
    This class also gets info on stock like ratios, news and graph data 
    from yahoo for the stock gui to display"""
    def __init__(self, stock_symbol, user_object):
        #Passed in objects:
        self.yahoo_api_object = yahoo_api.YahooAPI()
        self.user_object = user_object
        self.stock_symbol=stock_symbol
        self.dashboardController = dashboard_controller.DashboardController(user_object)
        #pull data on this stock from API.
        #self.StockData = self.get_stock_data_API()
        #self.stock_graph_values = self.get_stock_graph_values_from_yahoo_finance #2D list with 2 dict timestamp and stockprice
        #self.newslink = self.get_newslink_Yahoo_API()
        
        #finally create stock GUI
        #self.StockGUIObject = self.create_stock_GUI()
        self.shares_owned = 0
    
    def handle_search_bar_event(self, stock_symbol):
        """looks for stock symbol and creates a stock GUI of stock symbol if successful"""
        #check if stock exists
        if self.yahoo_api_object.check_stock_exists(stock_symbol):
            #stock exists hence create stock_controller
            #get info on this stock from yahoo api
            #self.stock_symbol=stock_symbol
            self.stockData = self.get_stock_data_API(stock_symbol)
            self.stock_graph_values = self.get_stock_graph_values_from_yahoo_finance(stock_symbol) #2D list with 2 dict timestamp and stockprice
            self.newslink = self.get_newslink_Yahoo_API(stock_symbol)
            self.create_stock_GUI(stock_symbol, self.stockData, self.stock_graph_values, self.newslink, self.user_object)
        else:
            #could not find stock_symbol
            message = "Could not find stock entered in search bar."
            self.create_popup_GUI(message)

    def handle_viewInformation_event(self, stock_symbol, portfolioGUI):
        """creates a stock GUI of stock symbol that is selected."""
        #check if stock exists
        if self.yahoo_api_object.check_stock_exists(stock_symbol):
            portfolioGUI.destroy()
            #stock exists hence create stock_controller
            #get info on this stock from yahoo api
            #self.stock_symbol=stock_symbol
            self.stockData = self.get_stock_data_API(stock_symbol)
            self.stock_graph_values = self.get_stock_graph_values_from_yahoo_finance(stock_symbol) #2D list with 2 dict timestamp and stockprice
            self.newslink = self.get_newslink_Yahoo_API(stock_symbol)
            self.create_stock_GUI(stock_symbol, self.stockData, self.stock_graph_values, self.newslink, self.user_object)
        else:
            #could not find stock_symbol
            message = "Could not find stock information selected."
            self.create_popup_GUI(message)
        
    def get_stock_graph_values_from_yahoo_finance(self, stockSymbol):
        """Retrieves values for the stock graph. If call fails opens pop-up gui"""
        self.stock_graph_values = self.yahoo_api_object.get_stock_graph_values(stockSymbol)
        if self.stock_graph_values == 0:
            self.create_popup_GUI("Could not get Stock's graph values from Yahoo Finance.")
        return self.stock_graph_values
        
    def get_stock_data_API(self, stockSymbol):
        """Returns stock data from Yahoo api"""
        return self.yahoo_api_object.get_specific_stock_info(stockSymbol)

    def get_newslink_Yahoo_API(self,stockSymbol):
        """Returns newslink retreieved from Yahoo API Object"""
        return self.yahoo_api_object.get_link(stockSymbol)

        
    def open_dashboard(self):
        """Hands controller back to dashboard controller."""
        self.dashboardController.createDashboardGUI()

    def create_stock_GUI(self,stock_symbol, stockData,stock_graph_values, newslink ,userObject):
        """creates the stock GUI"""
        root = Tk()
        root.geometry("700x700")
        self.stockGUIObject = stock_gui.StockGUI(root,stock_symbol, stockData, stock_graph_values, newslink,userObject )
        root.mainloop()
        

    def add_stock_in_user_class(self, stockid = -1, stockowned = 0):
        """Adds stock in user class by default the stock id is set to -1, and stockowned is 0.
        This stock is now part of the users portfolio stocks."""
        userId = self.user_object.current_user_data[0]
        self.user_object.append_stock(self.stock_symbol,userId, stockid, stockowned)
        #show message to user
        message = "Stock added!"
        self.create_popup_GUI(message)

    def get_stock_owned_from_user_class(self):
        """gets stock owned from user object with stock symbol"""
        self.user_object.get_stockowned(self.stock_symbol)

    def update_stock_owned(self, stockOwned):
        """updates stock owned of specific user."""
        self.user_object.update_stock_owned(self.stock_symbol, stockOwned)
        message = "Shares Updated!"
        self.create_popup_GUI(message)

    def delete_stock(self):
        """deletes stock from user object if successfull. If not, a popup is displayed."""
        success = self.user_object.delete_stock(self.stock_symbol)
        if not success: #if code correct this should never execute
            self.create_popup_GUI("Oh no, we could not delete this stock.")

    def create_popup_GUI(self, message):
        """creates a pop-up GUI with given error message."""
        self.popUpGUIObject = popupGUI.PopUpGUI(message)
        self.popUpGUIObject.createPopUp()   

    def controll_to_dashboard(self):
        """Return controller back to Dashboard controller.
        Dashboard GUI is displayed."""
        self.DashboardController.create_dashboard_GUI()