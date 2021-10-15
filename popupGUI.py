'''class PopupGUI():
    Pop up GUI takes in a message that it 
    displays when calling create pop up function
    def __init__(self, message):
        self.message = message
        #hi heres james
    
    def create_pop_up(message):
        This function creates a tkinter pop up window 
        that displays a given message
        pass'''
        

from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox



class PopUpGUI():
    def __init__(self, master):
        self.master = master
        self.master.title("Basic GUI")
        
    
        self.mainframe = Frame(master, width = 300, height = 700)
        self.mainframeLabel = Label( self.mainframe, text="GUI",font='Helvetica 18 bold')
        self.mainframeLabel.pack()
        self.mainframe.pack()
        self.mainframe.pack_propagate(0)
        self.mainframe.place(x=50, y=20)
        
        #fake buttons that are only used for testing, this class only will represent the message boxes
        self.logInButton = Button(self.mainframe, text="Log In",command=PopUpGUI.LoginClick).grid(row = 2,column=1,padx=30,pady=25,ipadx=2,ipady=2, sticky="nw")
        self.signUpButton = Button(self.mainframe, text="Sign Up",command=PopUpGUI.SignUpClick).grid(row = 2,column=2,padx=30,pady=25,ipadx=2,ipady=2, sticky="nw")
        self.stockAddButton = Button(self.mainframe, text="Stock Add",command=PopUpGUI.StockAddClick).grid(row = 3,column=1,padx=30,pady=25,ipadx=2,ipady=2, sticky="nw")
        self.stockDeleteButton = Button(self.mainframe, text="Stock Delete",command=PopUpGUI.StockDeleteClick).grid(row = 3,column=2,padx=30,pady=25,ipadx=2,ipady=2, sticky="nw")

        
        
    def LoginClick():
        try:
            tkinter.messagebox.showinfo("Login.",  "Login successfully")
        except:
            tkinter.messagebox.showinfo("Login.",  "Login failed")

    
    def SignUpClick():
         try:
            tkinter.messagebox.showinfo("Sign up.",  "Signed up successfully")
         except:
            tkinter.messagebox.showinfo("Sign up.",  "Signed up failed")
            
    
    def StockAddClick():
        try:
            tkinter.messagebox.showinfo("Stock.",  "Stock successfully added")
        except:
            tkinter.messagebox.showinfo("Stock.",  "Stock failed to added")

    
    def StockDeleteClick():
        try:
            tkinter.messagebox.showinfo("Stock.",  "Stock successfully deleted")
        except:
            tkinter.messagebox.showinfo("Stock.",  "Stock failed to delete")







root = Tk()
root.geometry("350x490")
my_gui = PopUpGUI(root)
root.mainloop()
    