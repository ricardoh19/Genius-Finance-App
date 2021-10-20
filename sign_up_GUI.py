from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import loginGUI
import loginlogout_controller 


# this class controls the graphical user interface of the Sign Up window. Its methods include createMainFrame, 
# createSignUpUsernamePasswordFrame, createSecurityQuestionFrame, handleLoginEvent, handleSignUpEvent, 
# handleCloseEvent.
class SignUpGUI():
    def __init__(self, master):
        # will update new methods and attribute in class diagram
        self.signUpMaster = master
        self.loginlogoutControllerObject = loginlogout_controller.LoginLogoutControllers()
        self.signUpMaster.title("Sign Up")
        self.createMainFrame()

    '''
    Intent: creates the main frame for the Sign Up GUI
    * Preconditions: master is connected to TKinter. createSignUpUsernamePasswordFrame and createSecurityQuestionFrame
    * have the appropriate GUI codeto be called in this method.
    * Postconditions:
    * Post0. main frame for sign up is created
    '''
    def createMainFrame(self): 
        # logo on top left side
        self.logo = Label(self.signUpMaster, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5, sticky="w")
        self.createSignUpUsernamePasswordFrame()
        self.createSecurityQuestionFrame()
        self.exitButton = Button(self.signUpMaster,text="Close",command=lambda: self.handleCloseEvent()).grid(row = 4,column=1,sticky="se")
        self.SignUpButton = Button(self.signUpMaster,text="Sign Up",command=lambda: self.handleSignUpEvent()).grid(row = 4,column=1)

    '''
    Intent: creates frame with  SignUp, Username, and Password entries for the sign up GUI
    * Preconditions: master is connected to TKinter. 
    * Postconditions:
    * Post0. frame with SignUp, Username, and Password entries is implemented for sign up 
    '''
    def createSignUpUsernamePasswordFrame(self):
        # top credentials frame
        self.signUpcredentials = Frame(self.signUpMaster, width = 450, height = 170,borderwidth=2, relief="sunken").grid(row = 1,column=1,padx=20)
        self.usernameLabel = Label( self.signUpcredentials, text="Enter a Username",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.passwordLabel = Label( self.signUpcredentials, text="Enter a Password",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row=1, column=1,padx=30,pady=25, ipadx=5,ipady=5,sticky="w")
        self.reenterPasswordLabel = Label( self.signUpcredentials, text="Reenter the Password",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row=1, column=1,padx=25,pady=25, ipadx=3,ipady=5,sticky="sw")
        self.usernameEntry = Entry(self.signUpcredentials)
        self.usernameEntry.grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="ne")
        self.passwordEntry = Entry(self.signUpcredentials)
        self.passwordEntry.grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="e")
        self.reenterPasswordEntry = Entry(self.signUpcredentials)
        self.reenterPasswordEntry.grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="se")
        
    '''
    Intent: creates the frame with the security question for the sign up GUI
    * Preconditions: master is connected to TKinter.
    * Postconditions:
    * Post0. frame with the security question for sign up is created
    '''
    def createSecurityQuestionFrame(self):
        # security question frame
        self.buttons= Frame(self.signUpMaster, width = 450, height = 150, borderwidth=2, relief="sunken").grid(row = 2,column=1,padx=20)
        self.securityQuestionLabel = Label( self.signUpcredentials, text="Security Question: What is your  favorite food?",font='Helvetica 13 bold',borderwidth=3, relief="ridge").grid(row=2, column=1,padx=15,pady=15, ipadx=1,ipady=1,stick="n")
        self.securityQuestionEntry = Entry(self.signUpcredentials).grid(row = 2,column=1,padx=8,pady=15,ipadx=2,ipady=2)
        
        
    '''
    Intent: handles the close event for sign up GUI. When closed, sign up GUI is closed and login GUI is created and displayed.
    * Preconditions: master is connected to TKinter.
    * loginlogoutController is an instance of the class. 
    * createLoginGUI() is ready to be called from loginlogoutController
    * Postconditions:
    * Post0. sign up GUI is closed and login GUI is created and displayed
    '''
    def handleCloseEvent(self):
        self.signUpMaster.destroy()
        self.loginlogoutControllerObject.createLoginGUI()

    '''
    Intent: handles the sign up event for sign up GUI
    * Preconditions:    
    * loginlogoutController is an instance of the class. 
    * Postconditions:
    * Post0. signUpUserProcessing() is called by loginlogoutController
    '''
    def handleSignUpEvent(self):
        self.loginlogoutControllerObject.signUpUserProcessing(self.usernameEntry.get(),self.passwordEntry.get(),self.reenterPasswordEntry.get() )

        
            



