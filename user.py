import logging 

class User():
    """User class holds login details of user as well as stock associated with the user."""
    def __init__(self, current_user_data, current_user_stocks):
        self.current_user_data=current_user_data
        #list: id:int, username:str, password:str, securityquestionanswer:str
        self.current_user_stocks=current_user_stocks
        #dict: key = stockname:str, values: stockid:int. stockowned:int (number of stock owned)
    def DeleteStock(self, stockname):
        """Function deletes specified stockname from current user stoccks"""
        try:
            del self.current_user_stocks[stockname]
        except KeyError:
            logging.error(f"Unable to remove {stockname} from User because it does not exist as a key in the dictionary.")

    def AppendStock(self, stockname, stockid = -1, stockowned = 0):
        """Appends a stock to the users collection of stocks. If not specified the stockid is -1
        to be changed when pushed to DB. Default stock owned is 0. """
        self.current_user_stocks[stockname] = [stockid, stockowned]
    