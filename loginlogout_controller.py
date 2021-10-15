from popupGUI import PopupGUI
from dashboard_controller import DashboardController
from database_manager import DB
from loginGUI import LoginGUI
from user import User
from sign_up_GUI import SignUpGUI

# ...
class LoginLogoutControllers():
    def __init__(self ):
        #initializes and pulls data from DB
        self.databaseManagerObject = DB()
        # get this data from DB Manager
        self.DatabaseUserData = None #2d list list: #list: id:int, username:str, password:str, securityquestionanswer:str
        self.DatabaseStockData = None#list of dict: key = stocksymbol :str, values: stockid:int. stockowned:int (number of stock owned)
        self.current_user_data = None #list: id:int, username:str, password:str, securityquestionanswer:str
        self.current_user_stocks = None #dict: key = stocksymbol:str, values: stockid:int. stockowned:int (number of stock owned)
        #create popupgui object
        #self.popup_GUI_object = PopupGUI()
        self.userObject = None
        self.sign_up_gui_object = None
        #Load data from db
        self.getSnapshotOfDatabase() 
        #self.setCurrentUserData()# needs username as parameter

        #create login GUI
        self.createLogin_GUI()

    '''
    Intent: creates the GUI frame to log-in user.
    * Preconditions: LogIn GUI class is created.
    * Postconditions:
    * Post0. LogIn GUI class is created and called.
    '''
    def createLogin_GUI(self):
        self.LoginGUIObject = LoginGUI(self)

    
    '''
    Intent: Pulls all data from database and stores it in user and stock lists. Returns the lists.
    * Preconditions: self.databaseManagerObject is created and initializeded to class DB.
    * self.databaseUserData is created.
    * self.databaseStockData is created.
    * Postconditions:
    * Post0. all userData is inserted into self.databaseUserData and all Stock is inserted into
    * self.databaseStockData.
    * Post1. No data is pulled from database if connection to database fails.
    '''
    def getSnapshotOfDatabase(self):
        userData = self.databaseManagerObject.getDatabaseUserData()
        stockData = self.databaseManagerObject.getDatabaseStockData()
        self.databaseUserData = [userData]
        self.databaseStockData = [stockData]
        return self.databaseUserData,self.databaseStockData


    '''
    Intent: Compares username to all usernames in the database. Returns a list of the corresponding user data.
    * Returns an object of user data corresponding to the specific username. Returns None if nothing is found for username.
    * Preconditions: 
    * username is unique to the database.
    * self.databaseUserData is created.
    * If self.databaseUserData is None, return None.
    * Postconditions:
    * Post0. An object of the User data pertaining to specific user with username is set.
    '''
    def setCurrentUserData(self,username):
        if self.databaseUserData == None:
            return self.currentUserData

        for data in self.databaseUserData:
            for objectData in data:   
                if objectData[1] == username:
                    self.currentUserData = objectData
                else:
                    self.currentUserData = (-1, '', '', '')
        return self.currentUserData


    '''
    Intent: compares userId to all userId's in the database to get stock data. Returns a list of the corresponding stock data.
    * Returns None if nothing is found for specific userId.
    * Preconditions: 
    * setCurrentUserData() has returned a user object. 
    * userId is taken from setCurrentUserData().
    * If self.setCurrentUserData(username) is None, self.currentUserStocks == None.
    * Postconditions:
    * Post0. An object of the stock data pertaining to specific user with userId is set.
    '''
    def setCurrentStockData(self,username):
        if self.setCurrentUserData(username) == None:
            return self.currentUserStocks
        userData = self.setCurrentUserData(username)
        userId = userData[0]
        
        for data in self.databaseStockData:
            for StockObject in data:                   
                if StockObject[2] == userId:
                    self.currentUserStocks = StockObject
        return self.currentUserStocks
            

   
    '''
    Intent: Compares securityQuestionAnswer to data in the database pertaining to specific username. 
    * Returns True if securityQuestionAnswer matches with username's securityQuestionAnswer. Returns False otherwise.
    * Preconditions: if self.setCurrentUserData() == None, return True
    * This method would only be called when User forgets password or signs up.
    * Postconditions: 
    * Post0. securityQuestionAnswer is validated.
    * Post1. securityQuestionAnswer is not validated if self.setCurrentUserData(username) equal to None. 
    '''
    def verifySecurityQuestionAnswerUsername(self, securityQuestionAnswer, username):
        if self.setCurrentUserData(username) == None:
            return True 
        userData = self.setCurrentUserData(username)
        if userData[3] == securityQuestionAnswer:
            return True
        return False
        
   
   
    '''
    Intent: Checks if username if unique and password is validated. Returns True if both validated. Return False otherwise.
    * Preconditions: 
    * self.checkUsernameTaken(username) returns a boolean.
    * If username or passwordEntered equal None, return False.
    * Postconditions:
    * Post0. Username and password are both validated.
    * Post1. username or password are not validated if equal None.
    '''
    def validateUsernamePassword(self, username, passwordEntered):
        if username == None or passwordEntered == None:
            return False
        if self.checkUsernameTaken(username):
            return False
        
        if len(passwordEntered) < 10:
            return False
        
        # check for special characters
        specialChars = "!#$^*"
        charCount = 0
        for char in specialChars:
            if char in passwordEntered:
                charCount+=1
        if charCount < 1:
            return False
        
        # check for uppercase letters
        if passwordEntered.islower():
            return False
        return True
       
        
        

    
    '''
    Intent: Checks if username already in database if new user. Returns True if username exists, False otherwise.
    * Preconditions: 
    * self.databaseUserData is created.
    * username entered != None
    * Postconditions:
    * Post0. username is compared to all other usernames in database.
    * Post1. username is not compared if equal to None.
    '''
    def checkUsernameTaken(self, username):
        if username == None:
            return False
        for data in self.databaseUserData:
            for objectData in data: 
                if objectData[1] == username:
                    return True
        return False
        

    """ Do ValidateUsernamePassword. If valid:
    CreateUserObject then CreateDashboardController.
    Else error message pop-up GUI."""
    '''
    Intent: Logs the User in by creating user object then creating dashboard controller. 
    * Preconditions: 
    * self.validateUsernamePassword(username,password) validates the username and password of user.
    * self.createPopupGui creates the popup GUI with text when called.
    * self.createDashboardController() creates the dashboard when called.
    * Postconditions:
    * Post0. creates user object if username and password validated by the method validateUsernamePassword(username,password)
    * Post1. does not create the user object. Shows popup GUI with error message.
    '''
    def loginUser(self, username, password):
        if self.validateUsernamePassword(username,password):
            self.createUserObject(self.currentUserData, self.currentUserStocks)
            self.createDashboardController()
            
        else:
            self.createPopupGUI("Error")
            

    
    '''
    Intent: Creates User object by passing currentUserData and currentUserStocks as parameters. Returns user object
    * Preconditions: 
    * Postconditions:
    * Post0. User object created and returned.
    * Post1. User object is returned as None.
    '''
    def createUserObject(self, currentUserData, currentUserStocks):
        self.userObject = User(currentUserData, currentUserStocks)
        return self.userObject

    
        





    

    
    def createDashboardController(self):
        """Creates Dashboard Controller"""
        #DashboardController(self, self.user_object,self.popup_GUI_object) #dont need reference
        pass
    
    def createPopupGUI(self, message):
        """creates a pop-up GUI with given error message."""
        #self.popup_GUI_object.create_pop_up(message)
        pass


    def logout_push_changes_to_database(self):
        """Check what has to be changed userobject vs self.current_user_data self.current_user_stocks.
        Whatever has to be change it (insert if doesnt exist stockid or user id -1, update else."""
        pass
    def signUpUserProcessing(self, username, password):
        """Called by Sign up GUI passes in username password. 
        Calls validate username password.
        If valid calls Login GUI. else popup"""
        pass

    def create_sign_up_GUI(self):
        self.sign_up_gui_object = SignUpGUI(self)
        

    def forgetPasswordProcessing(self, security_question_answer, newpassword, username):
        """Call VerifySecurityQuestionAnswerUsername if its correct reset password for user in DB.
        then creates login gui.
        Else error message pop up GUI."""
        pass
    