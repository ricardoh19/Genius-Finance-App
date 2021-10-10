import logging
from database_controller import DatabaseController
import os

def set_env_variables():
    #export variables to environment
    os.environ["X_RapidAPI_Host"]= "yh-finance.p.rapidapi.com"
    os.environ["X_RapidAPI_Key"]= "9928c7260amshad0766390e03e89p1f4683jsn18824f37a5dc"


def main():
    set_env_variables()
    logging.basicConfig(filename='geniusfinclogs.log', encoding='utf-8', level=logging.DEBUG, force=True)    
    pass

if __name__ == "__main__":
    main()