# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 10:32:25 2021

@author: Owner
"""


class DashboardControllers():
    def __init__(self, LoginLogoutController, WatchlistObject, StockObject,
                 PortfolioObject, DashboardGUIObject, PopUpGUIObject):
        self.LoginLogoutController = LoginLogoutController
        self.WatchlistObject = WatchlistObject
        self.StockObject= StockObject
        self.PortfolioObject = PortfolioObject
        self.DashboardGUIObject = DashboardGUIObject
        self.PopUpGUIObject = PopUpGUIObject
    
    def HandleLogoutEvent():
        pass
    def CreateStockController():
        pass
    def CreatePortfolioController():
        pass
    def CreateDashboardGUI():
        pass
    def CreateYahooAPI():
        pass
    def HandleSearchBarEvent():
        pass
    def CreatePopUpGUI():
        pass
    