import logging
from database_manager import DB
from dashboard_controller import DashboardControllers
import os

def set_env_variables():
    #export variables to environment for yahoo finance
    os.environ["X_RapidAPI_Host"]= "yh-finance.p.rapidapi.com"
    os.environ["X_RapidAPI_Key"]= "9928c7260amshad0766390e03e89p1f4683jsn18824f37a5dc"


def main():
    #contains what is happening when APP is started
    set_env_variables()
    logging.basicConfig(filename='geniusfinclogs.log', encoding='utf-8', level=logging.DEBUG, force=True)    
    #create DB manager
    db_manager_object = DB()


if __name__ == "__main__":
    main()