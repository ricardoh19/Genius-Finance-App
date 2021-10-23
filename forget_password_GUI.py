from tkinter import *
import tkinter as tk
from tkinter import ttk
import loginlogout_controller 

# why does this class need all these attributes?
'''
login_logout_controllerObject,popup_GUI_object,LoginGUIObject,
username,newPassword,ReenteredPassword,SecurityQuestionAnswer
'''
'''
        self.popup_GUI_object = popup_GUI_object
        self.ReenteredPassword = ReenteredPassword
        self.SecurityQuestionAnswer = SecurityQuestionAnswer
        self.LoginGUIObject = LoginGUIObject
        self.login_logout_controllerObject = login_logout_controllerObject
        self.username = username
        self.newPassword = newPassword
'''
class ForgetPasswordGUI():
    def __init__(self, master):
        self.loginlogoutControllerObject = loginlogout_controller.LoginLogoutControllers()
        self.master = master
        self.master.title("Forgot Password")
        self.createMainFrame()
        
    '''
    Intent: creates the main frame for the forgot password GUI
    * Preconditions: master is connected to TKinter. createForgotPasswordUsernamePasswordFrame and createSecurityQuestionFrame
    * have the appropriate GUI code to be called in this method.
    * Postconditions:
    * Post0. main frame for sign up is created
    '''
    def createMainFrame(self): 
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5, sticky="w")
        self.createForgotPasswordUsernamePasswordFrame()
        self.createSecurityQuestionFrame()
        self.exitButton = Button(self.master,text="Close",command=lambda: self.handleCloseEvent()).grid(row = 4,column=1,sticky="se")
        self.ResetPasswordButton = Button(self.master,text="Reset Password",command=lambda: self.handleForgotPasswordEvent()).grid(row = 4,column=1)

    '''
    Intent: creates frame with  reset password, Username, and Password entries for the forgot Password GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. frame with forgotPassword, Username, and Password entries is implemented for forgot Password 
    '''
    def createForgotPasswordUsernamePasswordFrame(self):
        # top credentials frame
        self.forgotPasswordcredentials = Frame(self.master, width = 450, height = 170,borderwidth=2, relief="sunken").grid(row = 1,column=1,padx=20)
        self.usernameLabel = Label( self.forgotPasswordcredentials, text="Enter a Username",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.passwordLabel = Label( self.forgotPasswordcredentials, text="Enter a Password",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row=1, column=1,padx=30,pady=25, ipadx=5,ipady=5,sticky="w")
        self.reenterPasswordLabel = Label( self.forgotPasswordcredentials, text="Reenter the Password",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row=1, column=1,padx=25,pady=25, ipadx=3,ipady=5,sticky="sw")
        self.usernameEntry = Entry(self.forgotPasswordcredentials)
        self.usernameEntry.grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="ne")
        self.passwordEntry = Entry(self.forgotPasswordcredentials)
        self.passwordEntry.grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="e")
        self.reenterPasswordEntry = Entry(self.forgotPasswordcredentials)
        self.reenterPasswordEntry.grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="se")
        
    '''
    Intent: creates the frame with the security question for the forgot Password GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. frame with the security question for sign up is created
    '''
    def createSecurityQuestionFrame(self):
        # security question frame
        self.buttons= Frame(self.master, width = 450, height = 150, borderwidth=2, relief="sunken").grid(row = 2,column=1,padx=20)
        self.securityQuestionLabel = Label( self.forgotPasswordcredentials, text="Security Question: What is your  favorite food?",font='Helvetica 13 bold',borderwidth=3, relief="ridge").grid(row=2, column=1,padx=15,pady=15, ipadx=1,ipady=1,stick="n")
        self.securityQuestionEntry = Entry(self.forgotPasswordcredentials).grid(row = 2,column=1,padx=8,pady=15,ipadx=2,ipady=2)
        
        
    '''
    Intent: handles the close event for forgot password  GUI. When closed, forgot password GUI is closed and login GUI is created and displayed.
    * Preconditions: master is connected to TKinter.
    * loginlogoutController is an instance of the class. 
    * createLoginGUI() is ready to be called from loginlogoutController
    * Postconditions:
    * Post0. forgot password GUI is closed and login GUI is created and displayed
    '''
    def handleCloseEvent(self):
        self.master.destroy()
        self.loginlogoutControllerObject.createLoginGUI()

    '''
    Intent: close the forgot password window .
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. closes the forgot password window
    '''
    def closeWindow(self):
        self.signUpMaster.destroy()

    '''
    Intent: handles the sign up event for forgot password GUI
    * Preconditions:    
    * loginlogoutController is an instance of the class. 
    * Postconditions:
    * Post0. signUpUserProcessing() is called by loginlogoutController
    '''
    def handleForgotPasswordEvent(self):
        self.loginlogoutControllerObject.forgetPasswordProcessing()


