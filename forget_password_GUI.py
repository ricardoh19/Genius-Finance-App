# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 09:23:37 2021

@author: Owner
"""


class ForgetPasswordGUI():
    def __init__(self, login_logout_controllerObject,popup_GUI_object,LoginGUIObject,
                 username,newPassword,ReenteredPassword,SecurityQuestionAnswer):
        self.popup_GUI_object = popup_GUI_object
        self.ReenteredPassword = ReenteredPassword
        self.SecurityQuestionAnswer = SecurityQuestionAnswer
        self.LoginGUIObject = LoginGUIObject
        self.login_logout_controllerObject = login_logout_controllerObject
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