from popupGUI import PopupGUI
from dashboard_controller import DashboardController
from database_manager import DB
from loginGUI import LoginGUI
from user import User
from sign_up_GUI import SignUpGUI

class LoginLogoutControllers():
    def __init__(self ):
        #initializes and pulls data from DB
        self.databaseManagerObject = DB()
        # get this data from DB Manager
        self.databaseUserData = None #2d list list: #list: id:int, username:str, password:str, securityquestionanswer:str
        self.databaseStockData = None#list of dict: key = stockname:str, values: stockid:int. stockowned:int (number of stock owned)
        self.currentUserData = None #list: id:int, username:str, password:str, securityquestionanswer:str
        self.currentUserStocks = None #dict: key = stockname:str, values: stockid:int. stockowned:int (number of stock owned)
        #create popupgui object
        #self.popup_GUI_object = PopupGUI()
        self.userObject = None
        self.sign_up_gui_object = None
        #Load data from db
        self.getSnapshotOfDatabase()
        #self.set_current_user_data()
        #create login GUI
        #self.CreateLogin_GUI()

    """Creates Login Gui. """
    def createLogin_GUI(self):
        self.LoginGUIObject = LoginGUI(self)

    """Pull all the database data through the database manager. 
    So now we put what we pulled in self.DatabaseUserData self.DatabaseStockData.
    Going to need to add two more methods to databaseManager.py - 
    getAllDatabaseUserData()
    getAllDatabaseStockData()
    """
    def getSnapshotOfDatabase(self):
        userData = self.databaseManagerObject.getAllDatabaseUserData()
        stockData = self.databaseManagerObject.getAllDatabaseStockData()
        self.databaseUserData = [userData]
        self.databaseStockData = [stockData]
        return self.databaseUserData,self.databaseStockData


    """Now we have the username, password check it against self.DatabaseUserData. 
    Get userId from that and create self.currentUserData self.currentUserStocks"""
    # username has to be unique
    def setCurrentUserData(self,username):
        for data in self.databaseUserData:
            for objectData in data:   
                if objectData[1] == username:
                    self.currentUserData = objectData
                else:
                    self.currentUserData = (-1, '', '', '')
        return self.currentUserData


    '''uses setCurrentUserData() to pull user data and get userId. THen it uses userId to get stock data'''
    def setCurrentStockData(self,username):
        userData = self.setCurrentUserData(username)
        userId = userData[0]
        
        for data in self.databaseStockData:
            for StockObject in data:                   
                if StockObject[2] == userId:
                    self.currentUserStocks = StockObject
        return self.currentUserStocks
            

    """Here we check if the passed in securityQuestionAnswer 
    is the same as in the username.
    returns true/false"""
    def verifySecurityQuestionAnswerUsername(self, securityQuestionAnswer, username):
        userData = self.setCurrentUserData(username)
        if userData[3] == securityQuestionAnswer:
            return True
        return False
        
    
    
    """checks username against DB.
    checks len of pw checks, special characters, atleast one uppercase, everything else to do with it and
    Calls checkUsernameTaken.
    returns true/false"""
    def validateUsernamePassword(self, username, passwordEntered):
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
       
        
        

    """If new user, check if the username already exist. 
    returns true/false"""
    def checkUsernameTaken(self, username):
        for data in self.databaseUserData:
            for objectData in data: 
                if objectData[1] == username:
                    return True
        return False
        

    """ Do ValidateUsernamePassword. If valid:
    CreateUserObject then CreateDashboardController.
    Else error message pop-up GUI."""
    def loginUser(self, username, password):
        if self.validateUsernamePassword(username,password):
            self.createUserObject(self.currentUserData, self.currentUserStocks)


    """Creates user object. """
    def createUserObject(self, currentUserData, currentUserStocks):
        self.userObject = User(currentUserData, currentUserStocks)


    
        





    

    
    def CreateDashboardController(self):
        """Creates Dashboard Controller"""
        #DashboardController(self, self.user_object,self.popup_GUI_object) #dont need reference

    
    def create_popup_GUI(self, message):
        """creates a pop-up GUI with given error message."""
        #self.popup_GUI_object.create_pop_up(message)



    def logout_push_changes_to_database(self):
        """Check what has to be changed userobject vs self.current_user_data self.current_user_stocks.
        Whatever has to be change it (insert if doesnt exist stockid or user id -1, update else."""
        
    def SignUpUserProcessing(self, username, password):
        """Called by Sign up GUI passes in username password. 
        Calls validate username password.
        If valid calls Login GUI. else popup"""
        pass

    def create_sign_up_GUI(self):
        self.sign_up_gui_object = SignUpGUI(self)
        

    def ForgetPasswordProcessing(self, security_question_answer, newpassword, username):
        """Call VerifySecurityQuestionAnswerUsername if its correct reset password for user in DB.
        then creates login gui.
        Else error message pop up GUI."""
        pass
    