# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:34:28 2021

@author: Owner
"""
'''

            STAND ALONE PROGRAM AT THE MOMENT
'''


from tkinter import *
import tkinter as tk
from tkinter import ttk

''' Intent: Connects to database, logs user into their account.
    * Preconditions: username and password have to be correcctly  entered and valid
    * Postconditions:
    * Post0. Data entered in GUI is put in database
    * Post1. User is taken to dashboard
    * Exception: Username/Password is incorrect
    '''

class LoginGUI():
    def __init__(self, master):
        # will update new methods and attribute in class diagram
        ''' will add db'''
        self.master = master
        self.master.title("Log In or Register")
        
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5, sticky="w")
        
        # top credentials frame
        self.credentials = Frame(self.master, width = 350, height = 170,borderwidth=2, relief="sunken").grid(row = 1,column=1)
        self.usernameLabel = Label( self.credentials, text="Username",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.passwordLabel = Label( self.credentials, text="Password",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row=1, column=1,padx=30,pady=25, ipadx=5,ipady=5,sticky="sw")
        self.usernameEntry = Entry(self.credentials).grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="ne")
        self.passwordEntry = Entry(self.credentials).grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="se")

        # bottom button frame
        self.buttons= Frame(self.master, width = 350, height = 150, borderwidth=2, relief="sunken").grid(row = 2,column=1,pady=6)
        self.logInButton = Button(self.credentials, text="Log In").grid(row = 2,column=1,padx=30,pady=25,ipadx=2,ipady=2, sticky="nw")
        self.RegisterButton = Button(self.credentials, text="Register").grid(row = 2,column=1,padx=30,pady=25,ipadx=2,ipady=2, sticky="ne")
        self.ForgotButton = Button(self.credentials, text="Forgot Password").grid(row = 2,column=1,padx=30,pady=25,ipadx=2,ipady=2, sticky="s")
        
        
        self.exitButton = Button(self.master,text="Exit").grid(row = 4,column=1,sticky="se")
        
    def closeWindow(self):
        self.mainframe.destroy()

   

        
root = Tk()
root.geometry("350x490")
my_gui = LoginGUI(root)
root.mainloop()