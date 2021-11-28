
from utils import convert_to_type
class User():
    """User class holds login details of user as well as stock associated with the user."""
    def __init__(self, current_user_data, current_user_stocks= None):

        self.current_user_data=current_user_data
        self.check_current_user_data() #checks current user data input is correct type
        #list: id:int, username:str, password:str, securityquestionanswer:str
        self.current_user_stocks={}
        if current_user_stocks!= None and current_user_stocks!= []: # don't try to add stock if there is not any associated with our user
            self.user_stock_to_dict(current_user_stocks) #current_user_stocks is passed in as list make it into a dict
        #dict: key = stocksymbol:str, values: dict: stockid:int. stockowned:int (number of stock owned)
        # [{TSLA: {stockid:2, stockowned:10}, {APPL: {stockid:-1, stockowned:10},]
        else:
            print("Info: No stock associated with user.")
    def __str__(self):
        return f"User Data: {self.current_user_data} \nUser Stock Info: {self.current_user_stocks}\n"
    
    def check_current_user_data(self):
        """Ensures that information is of correct type and changes type if necessary
        """
        id = self.current_user_data[0]
        username = self.current_user_data[1]
        password = self.current_user_data[2]
        # Function in utils.py
        # Checks if the variable is of the wanted type if not tries to convert it. 
        #Throws error message if it can't convert it
        convert_to_type(variable_name= "User id", variable_type= int, variable_value = id)
        convert_to_type(variable_name= "Username", variable_type= str, variable_value = username)
        convert_to_type(variable_name= "password", variable_type= str, variable_value = password)

    def user_stock_to_dict(self, current_user_stocks):
        """Take in all users stocks and make them into the format of a dictionary"""
        for stockinfo in current_user_stocks:
            if stockinfo[2] == self.current_user_data[0]: #make sure to only add stocks associated with this user
                stocksymbol= stockinfo[1]
                stockid = stockinfo[0]
                stockowned = stockinfo[3]
                # Function in utils.py
                # Checks if the variable is of the wanted type if not tries to convert it. 
                # Throws error message if it can't convert it
                convert_to_type(variable_name= "stocksymbol", variable_type= str, variable_value =  stocksymbol)
                convert_to_type(variable_name= "stockid", variable_type= int, variable_value = stockid)
                convert_to_type(variable_name= "stockowned", variable_type= int, variable_value = stockowned)
                                
                self.current_user_stocks[stocksymbol] = \
                    {"stockid": stockid, 
                    "stockowned": stockowned,
                    }
       
    def delete_stock(self, stockname):
        """Function deletes specified stockname from current user stoccks"""
        try:
            del self.current_user_stocks[stockname]
        except KeyError:
            print(f"Unable to remove {stockname} from User because it does not exist as a key in the dictionary.")
            return False
        return True

    def append_stock(self, stocksymbol, userId, stockid = -1, stockOwnedDef = 0):
        """Appends a stock to the users collection of stocks. If not specified the stockid is -1
        to be changed when pushed to DB. Default stock owned is 0. """
        stock = {"stockid": stockid, "stockowned": stockOwnedDef}
        self.current_user_stocks[stocksymbol]= stock

        #stockOwned = stockOwnedDef
        #self.databaseManager.insertDatabaseStockData(stocksymbol,userId,stockOwned)

    def update_stock_owned(self, stocksymbol, stockowned = 0):
        """Changes the amount of a certain stock that the user owns."""
        try:
            # self.current_user_stocks[stocksymbol]
            self.current_user_stocks[stocksymbol]["stockowned"] = stockowned
        except KeyError:
            print(f"Unable to remove {stocksymbol} from User because it does not exist as a key in the dictionary.")
            return False
        return True


    def return_users_stock_symbols(self):
        """Returns a list of all user stocksymbols."""
        return self.current_user_stocks.keys()
    
    def get_stockowned(self, stocksymbol):
        """Returns the current amount of stock owned of specified stock"""
        try:
            return self.current_user_stocks[stocksymbol]["stockowned"]
        except KeyError:
            print(f"Unable to retrieve stock owned of {stocksymbol} from User because {stocksymbol} does not exist as a key in the dictionary.")
            return False
    