from popupGUI import PopUpGUI
from tkinter import *
import tkinter as tk
import dashboard_controller 
from database_manager import DB
from user import User
import loginGUI
import dashboardGUI
import sign_up_GUI
import forget_password_GUI



# this class controls the logic of loginGUI, signUpGUI, and forgetPassword. 
# It is the coordinator between these classes the its GUI classes. The methods in this class are createLoginGUI, 
# getSnapshotOfDatabase, setCurrentUserData, setCurrentStockData, verifySecurityQuestionAnswerUsername,
# validateUsernamePassword, checkUsernameTaken, createUserObject, loginUser, createDashboardController, createDashboardGUI,
# createPopupGUI, createSignUpGUI, signUpUserProcessing, logout_push_changes_to_database, forgotPasswordProcessing
class LoginLogoutControllers():
    def __init__(self):
        #initializes and pulls data from DB
        self.databaseManagerObject = DB()
        # get this data from DB Manager
        self.DatabaseUserData = None #2d list list: #list: id:int, username:str, password:str, securityquestionanswer:str
        self.DatabaseStockData = None#list of dict: key = stocksymbol :str, values: stockid:int. stockowned:int (number of stock owned)
        self.currentUserData = None #list: id:int, username:str, password:str, securityquestionanswer:str
        self.currentUserStocks = None #dict: key = stocksymbol:str, values: stockid:int. stockowned:int (number of stock owned)
        self.userObject = None
        self.sign_up_gui_object = None
        self.LoginGUIObject = None
        #Load data from db
        self.getSnapshotOfDatabase()
        #self.setCurrentUserData()# needs username as parameter

        
       

    '''
    Intent: creates the GUI frame to log-in user.
    * Preconditions: LogIn GUI class is created.
    * Postconditions:
    * Post0. LogIn GUI class is created and called.
    '''
    def createLoginGUI(self):
        root = Tk()
        root.geometry("515x490")
        self.LoginGUIObject = loginGUI.LoginGUI(root)
        root.mainloop()
        
    

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
                
        if self.currentUserData == None:
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
        
        self.currentUserStocks = []
        for data in self.databaseStockData:
            for stockObject in data:                   
                if stockObject[2] == userId:
                    self.currentUserStocks.append(stockObject)
        return self.currentUserStocks
            

   
    '''
    Intent: Compares securityQuestionAnswer to data in the database pertaining to specific username. 
    * Returns True if securityQuestionAnswer matches with username's securityQuestionAnswer. Returns False otherwise.
    * Preconditions: if self.setCurrentUserData() == None, return True
    * This method would only be called when User forgets password.
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

    '''
    Intent: Checks if password entered matches with the password connected to the specific username 
    * Preconditions: 
    * self.databaseUserData is created.
    * password entered != None
    * Postconditions:
    * Post0. password is compared to password of username entered in database.
    * Post1. password is not compared if equal to None.
    '''
    def checkPasswordCorrect(self, username, password):
        if password == None:
            return False
        for data in self.databaseUserData:
            for objectData in data: 
                if objectData[1] == username:
                    if objectData[2] == password:
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
    def loginUser(self, username, password, loginGUI):
        if not self.checkUsernameTaken(username):
            popupGUI = PopUpGUI("Username not found")
            popupGUI.createPopUp()
            
        elif self.validateUsernamePassword(username,password) and self.checkPasswordCorrect(username, password):
            loginGUI.destroy()
            self.createDashboardController(username)
        else:
            popupGUI = PopUpGUI("Username or password is incorrect")
            popupGUI.createPopUp()
            
           
    
    '''
    Intent: Creates User object by passing username parameter. Returns user object
    * Preconditions: 
    * Postconditions:
    * Post0. User object created and returned.
    * Post1. User object is returned as None.
    '''
    def createUserObject(self,username):
        self.currentUserData = self.setCurrentUserData(username)
        self.currentUserStocks = self.setCurrentStockData(username)
        self.userObject = User(self.currentUserData, self.currentUserStocks)
        return self.userObject


    '''
    Intent: Creates Dashboard Controller and calls functions to creat user object and dashboard GUI.
    * Preconditions: 
    * dashboardController() exists
    * Postconditions:
    * Post0. dashboard controller class is created.
    '''
    def createDashboardController(self,username):
        self.userObject = self.createUserObject(username)

        dashboardController = dashboard_controller.DashboardController(self.userObject)
        dashboardController.createDashboardGUI()
        
    
    
    '''
    Intent: creates a pop-up GUI with given error message."
    * Preconditions: 
    * popupGuiObject is an instance of PopUpGUI class.
    * message is a string
    * Postconditions:
    * Post0. pop up message is created
    '''
    def createPopupGUI(self, message):
        popUpGUIObj = PopUpGUI(message)
        popUpGUIObj.createPopUp()
        

   
    '''
    Intent: creates sign-up GUI
    * Preconditions: 
    * Tkinter is imported and working
    * signUpGUI exists
    * Postconditions:
    * Post0. signUpGUI is created
    '''
    def createSignUpGUI(self):
        root = Tk()
        root.geometry("650x500")
        self.sign_up_gui_object = sign_up_GUI.SignUpGUI(root)
        root.mainloop()
       
    
    
    '''
    Intent: logic for signing user up. Displays appropriate message to user.
    * Preconditions: 
    * PopUpGUI exists
    * Postconditions:
    * Post0. shows user appropriate message based on sign-up status
    '''
    def signUpUserProcessing(self, username, password, secondPassword,securityQuestion, signUpGUI):
        if self.checkUsernameTaken(username):
            popupGUI = PopUpGUI("Username is taken.")
            popupGUI.createPopUp()
            
        elif password != secondPassword:
            popupGUI = PopUpGUI("Passwords do not match.")
            popupGUI.createPopUp()

        elif self.validateUsernamePassword(username,password):
            signUpGUI.destroy()
            # add user information to database
            self.databaseManagerObject.insertDatabaseUserData(username, password, securityQuestion)
            self.createDashboardController(username)
            
        else:
            popupGUI = PopUpGUI("Username or password is incorrect")
            popupGUI.createPopUp()
            
    '''
    Intent: verifies user information when using forgot Password feature.
    * Preconditions: 
    * PopUpGUI exists
    * Postconditions:
    * Post0. user's password is changed successfully.
    * Post1. user's password is not changed. Shows popup GUI with error message.
    '''
    def forgetPasswordProcessing(self, username, newPassword, newPassword2, security_question_answer, forgetPasswordGUI):
        """Call VerifySecurityQuestionAnswerUsername if its correct reset password for user in DB.
        then creates login gui.
        Else error message pop up GUI."""
        if not self.checkUsernameTaken(username):
            popupGUI = PopUpGUI("Username not found")
            popupGUI.createPopUp()
        elif newPassword != newPassword2:
            popupGUI = PopUpGUI("New passwords do not match.")
            popupGUI.createPopUp()

        # check security question answer
        elif not self.verifySecurityQuestionAnswerUsername(security_question_answer, username):
            popupGUI = PopUpGUI("Security Question is wrong")
            popupGUI.createPopUp()

        elif self.validateUsernamePassword(username,newPassword):
            forgetPasswordGUI.destroy()
            # update user information in database
            self.databaseManagerObject.updateDatabaseUserData(username, "password", newPassword)
            self.createLoginGUI()
        else:
            popupGUI = PopUpGUI("information entered is incorrect")
            popupGUI.createPopUp()

    
    '''
    Intent: creates forgot password GUI
    * Preconditions: 
    * Tkinter is imported and working
    * signUpGUI exists
    * Postconditions:
    * Post0. forgot password GUI is created
    '''
    def createForgottenPasswordGUI(self):
        root = Tk()
        root.geometry("650x500")
        forgetPasswordObject = forget_password_GUI.ForgetPasswordGUI(root)
        root.mainloop()



    '''
    Intent: Check what has to be changed userobject vs self.current_user_data self.current_user_stocks.
    * Preconditions: 
    * 
    * Postconditions:
    * Post0. Changes are pushed to database.
    '''
    def logout_push_changes_to_database(self,username, finalUserObject):
        """Check what has to be changed userobject vs self.current_user_data self.current_user_stocks.
        Whatever has to be change it (insert if doesnt exist stockid or user id equal -1, update else."""
        userObject = self.createUserObject(username)
        userId = userObject.current_user_data[0]
        
        for i in finalUserObject.current_user_stocks:
            if i not in userObject.current_user_stocks:
                self.databaseManagerObject.insertDatabaseStockData(i, userId, finalUserObject.current_user_stocks[i]['stockowned'])
       
        
