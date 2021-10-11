# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:29:11 2021

@author: Owner
"""


class PortfolioControllers():
    def __init__(self, UserObject,DashboardControllerObject, StockPriceDict,
                 YahooAPIObject, StockController):
        self.UserObject = UserObject
        self.DashboardControllerObject = DashboardControllerObject
        self.StockPriceDict = StockPriceDict
        self.YahooAPIObject = YahooAPIObject
        self.StockController=StockController
    def CallUserToRemoveStock():
        pass
    def CreateStockControllerObject():
        pass
    def GetStockPriceYahooAPIObject():
        pass
    def CreatePortfolioGUIObject():
        pass
    def CreateWatchListController():
        pass