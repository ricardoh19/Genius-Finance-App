
from tkinter import *
import tkinter as tk
from tkinter import ttk



class GUI():
    def __init__(self, master):
        self.master = master
        self.master.title("Basic GUI")
        
    
        self.mainframe = Frame(master, width = 300, height = 700)
        self.mainframeLabel = Label( self.mainframe, text="GUI",font='Helvetica 18 bold')
        self.mainframeLabel.pack()
        self.mainframe.pack()
        self.mainframe.pack_propagate(0)
        self.mainframe.place(x=50, y=20)

        
        
    def closeWindow(self):
        self.mainframe.destroy()

   
        


        
root = Tk()
root.geometry("800x600")
my_gui = GUI(root)
root.mainloop()