# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 20:43:28 2021

@author: Owner
"""
from tkinter import *
import tkinter as tk
from tkinter import ttk
'''

            STAND ALONE PROGRAM AT THE MOMENT
'''

''' Intent: Connects to database, creates user an account.
    * Preconditions: username has to unique, password has to be acceptable (will say what is required), 
    enter a security question answer
    * Postconditions:
    * Post0. Data entered in GUI is put in database
    * Exception 1: Username is taken already
    * Exception 2: Password does not fit the requirements or passwords do not match
    '''


class SignUpGUI():
    def __init__(self, master):
        ''' will add db'''
        # will update new methods and attribute in class diagram
        self.master = master
        self.master.title("Sign Up:")
        self.isClicked = False
        
        # logo on top left side
        self.logo = Label(self.master, text="Genius Finance",font='Helvetica 12',height = 6, width = 13,borderwidth=2, relief="solid").grid(row=0,column=1, pady=5, padx=5, sticky="w")
        
        # top credentials frame
        self.credentials = Frame(self.master, width = 450, height = 170,borderwidth=2, relief="sunken").grid(row = 1,column=1)
        self.usernameLabel = Label( self.credentials, text="Enter a Username",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row = 1,column=1,padx=30,pady=25,ipadx=5,ipady=5, sticky="nw")
        self.passwordLabel = Label( self.credentials, text="Enter a Password",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row=1, column=1,padx=30,pady=25, ipadx=5,ipady=5,sticky="w")
        self.reenterPasswordLabel = Label( self.credentials, text="Reenter the Password",font='Helvetica 13 bold',borderwidth=1, relief="ridge").grid(row=1, column=1,padx=25,pady=25, ipadx=3,ipady=5,sticky="sw")
        self.usernameEntry = Entry(self.credentials).grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="ne")
        self.passwordEntry = Entry(self.credentials).grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="e")
        self.reenterPasswordEntry = Entry(self.credentials).grid(row = 1,column=1,padx=8,pady=15,ipadx=2,ipady=2, sticky="se")
        
        # security question frame
        self.buttons= Frame(self.master, width = 450, height = 150, borderwidth=2, relief="sunken").grid(row = 2,column=1,pady=6)
        self.securityQuestionLabel = Label( self.credentials, text="Security Question: What is your  favorite food?",font='Helvetica 13 bold',borderwidth=3, relief="ridge").grid(row=2, column=1,padx=15,pady=15, ipadx=1,ipady=1,stick="n")
        self.securityQuestionEntry = Entry(self.credentials).grid(row = 2,column=1,padx=8,pady=15,ipadx=2,ipady=2)
        
        #exit and sign up button
        self.exitButton = Button(self.master,text="Close").grid(row = 4,column=1,sticky="se")
        self.SignUpButton = Button(self.master,text="Sign Up").grid(row = 4,column=1)

        
    def closeWindow(self):
        ''' will eventually fix and call this method to close out of program'''
        self.master.destroy()

    def usernameTaken():
        # if username is already in db throw exception
        pass

        
root = Tk()
root.geometry("600x500")

my_gui = SignUpGUI(root)

root.mainloop()