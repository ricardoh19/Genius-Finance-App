from tkinter import *
import tkinter as tk
from tkinter import ttk
root = Tk()
root.geometry("675x600")
print("hi")

frame = Frame(root, width = 10, height = 10,borderwidth=2, relief="sunken")
frame.grid(row = 2,column=1, padx=15, pady=20) 

img = PhotoImage(file="stockprice_chart.png")

picture_label = Label(frame,image=img, )
picture_label.grid(row=3, column=1)
# img = PhotoImage(file="stockprice_chart.png")
# picture_label = Label(frame,image=img)
# picture_label.grid()

root.mainloop()