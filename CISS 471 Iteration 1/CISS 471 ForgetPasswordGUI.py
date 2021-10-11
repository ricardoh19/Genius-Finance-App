# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:23:37 2021

@author: Owner
"""


class ForgetPasswordGUI():
    def __init__(self, LoginLogoutControllerObject,PopUpGUIObject,LoginGUIObject,
                 username,newPassword,ReenteredPassword,SecurityQuestionAnswer):
        self.PopUpGUIObject = PopUpGUIObject
        self.ReenteredPassword = ReenteredPassword
        self.SecurityQuestionAnswer = SecurityQuestionAnswer
        self.LoginGUIObject = LoginGUIObject
        self.LoginLogoutControllerObject = LoginLogoutControllerObject
        self.username = username
        self.newPassword = newPassword
        
        
    def HandleResetPasswordEvent():
        pass
    def HandleCloseEvent():
        pass
    def CreateMainFrame():
        pass
    def CreateUsernameSecurityQuestionFrame():
        pass
    def CreateNewPasswordFrame():
        pass