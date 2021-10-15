from tkinter import *
import tkinter as tk
from tkinter import ttk
from loginlogout_controller import LoginLogoutControllers



class LoginGUI():
    def __init__(self, master,loginlogout_ControllerObject):
        self.loginlogout_ControllerObject = loginlogout_ControllerObject
        self.master = master
        self.master.title("Log In or Register")
        self.createMainFrame()

    def createMainFrame(self):
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=0, pady=5, padx=5)
        self.createUsernamePasswordFrame()
        self.createLoginSignUpForgetPasswordFrame()

    def createUsernamePasswordFrame(self):
            # top credentials frame
        self.credentials = Frame(self.master, width = 350, height = 170,borderwidth=2, relief="sunken").grid(row = 1,column=1)
        self.usernameLabel = Label( self.credentials, text="Username",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.passwordLabel = Label( self.credentials, text="Password",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row=1, column=1,padx=30,pady=25, ipadx=5,ipady=5,sticky="sw")
        self.usernameEntry = Entry(self.credentials).grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="ne")
        self.passwordEntry = Entry(self.credentials).grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="se")
    
    def createLoginSignUpForgetPasswordFrame(self):
        # bottom button frame
        self.buttons= Frame(self.master, width = 350, height = 150, borderwidth=2, relief="sunken").grid(row = 2,column=1,pady=6)
        self.logInButton = Button(self.credentials, text="Log In").grid(row = 2,column=1,padx=30,pady=25,ipadx=2,ipady=2, sticky="nw")
        self.RegisterButton = Button(self.credentials, text="Register").grid(row = 2,column=1,padx=30,pady=25,ipadx=2,ipady=2, sticky="ne")
        self.ForgotButton = Button(self.credentials, text="Forgot Password").grid(row = 2,column=1,padx=30,pady=25,ipadx=2,ipady=2, sticky="s")
        self.exitButton = Button(self.master,text="Exit").grid(row = 4,column=1,sticky="se")
        
    def closeWindow(self):
        self.mainframe.destroy()

   
    def createSignUpGUI(self):
        pass
    def createForgetPassword(self):
        pass
    def handleLoginEvent(self):
        pass

        
root = Tk()
root.geometry("515x490")
loginlogout_controllerObject = LoginLogoutControllers()
my_gui = LoginGUI(root,loginlogout_controllerObject)
root.mainloop()