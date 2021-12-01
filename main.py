from tkinter import *
from loginGUI import LoginGUI
import os

def set_env_variables():
    #export variables to environment for yahoo finance
    os.environ["X_RapidAPI_Host"]= "yh-finance.p.rapidapi.com"
    os.environ["X_RapidAPI_Key"]= 'e4aa3ef749msh8d1181ee3d067f7p1e8b82jsn029f5f35d857'
    os.environ["GENIUS_FINC_DB_NAME"]= "GeniusFinanceDB"
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'Rhern_19'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='GeniusFinanceDB'

def main():
    set_env_variables()
    
    root = Tk()
    root.geometry("515x490")
    loginGUIObject = LoginGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
