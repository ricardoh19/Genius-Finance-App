from tkinter import *
from loginGUI import LoginGUI
import logging
from database_manager import DB
from dashboard_controller import DashboardController
import os

def set_env_variables():
    #export variables to environment for yahoo finance
    os.environ["X_RapidAPI_Host"]= "yh-finance.p.rapidapi.com"
    os.environ["X_RapidAPI_Key"]= "00e8271059mshd972b8e57433016p1d29a2jsnb5292e742ac2"
    os.environ["GENIUS_FINC_DB_NAME"]= "GeniusFinanceDB"


def main():
    #contains what is happening when APP is started
    set_env_variables()
    #logging.basicConfig(filename='geniusfinclogs.log', encoding='utf-8', level=print, force=True)    
    #create DB manager
    #db_manager_object = DB()
    
    root = Tk()
    root.geometry("515x490")
    loginGUIObject = LoginGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()