from tkinter import *
from loginGUI import LoginGUI
import os

def set_env_variables():
    #export variables to environment for yahoo finance
    os.environ["X_RapidAPI_Host"]= "yh-finance.p.rapidapi.com"
    os.environ["X_RapidAPI_Key"]= 'd943eab528msh01a1fdad73971cdp15b8abjsnbfae5e1c791a'
    os.environ["GENIUS_FINC_DB_NAME"]= "GeniusFinanceDB"
    os.environ['SQLUser']='root'
    os.environ['SQLPassword']= 'Veritas!10'
    os.environ['SQLHost'] = "localhost"
    os.environ['DB_NAME'] ='GeniusFinanceDB'

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