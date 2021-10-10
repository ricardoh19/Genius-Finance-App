# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:18:56 2021

@author: Owner
"""


class LoginLogoutControllers():
    def __init__(self,LoginGUIObject,DatabaseManagesObject,DatabaseUserData,DatabaseStockData,
                 PopUpGUIObject,CurrentUserData,CurrentUserStocks):
        self.LoginGUIObject = LoginGUIObject
        self.DatabaseManagesObject = DatabaseManagesObject
        self.DatabaseUserData = DatabaseUserData
        self.DatabaseStockData = DatabaseStockData
        self.PopUpGUIObject = PopUpGUIObject
        self.CurrentUserData = CurrentUserData
        self.CurrentUserStocks = CurrentUserStocks
    #
    def GetSnapshotOfDatabase():
        pass
    def SetCurrentUserData():
        pass
    def CreateLogin_GUI():
        pass
    def CreateDatabaseManages():
        pass
    def SignUpUserProcessing():
        pass
    def ForgetPasswordProcessing():
        pass
    def ValidateUsernamePassword():
        pass
    def CheckUsernameTaken():
        pass
    def VerifySecurityQuestionAnswerUsername():
        pass
    def LogoutPushChangesToDatabase():
        pass
    def CreateDashboardController():
        pass
    
    