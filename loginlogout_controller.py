from popupGUI import PopupGUI
from dashboard_controller import DashboardController
from database_manager import DB
from loginGUI import LoginGUI
from user import User
from sign_up_GUI import SignUpGUI

class LoginLogoutControllers():
    def __init__(self ):
        #initializes and pulls data from DB
        self.DatabaseManagesObject = DB()
        # get this data from DB Manager
        self.DatabaseUserData = None #2d list list: #list: id:int, username:str, password:str, securityquestionanswer:str
        self.DatabaseStockData = None#list of dict: key = stocksymbol :str, values: stockid:int. stockowned:int (number of stock owned)
        self.current_user_data = None #list: id:int, username:str, password:str, securityquestionanswer:str
        self.current_user_stocks = None #dict: key = stocksymbol:str, values: stockid:int. stockowned:int (number of stock owned)
        #create popupgui object
        self.popup_GUI_object = PopupGUI()
        self.user_object = None
        self.sign_up_gui_object = None
        #Load data from db
        self.GetSnapshotOfDatabase()
        self.set_current_user_data()
        #create login GUI
        self.CreateLogin_GUI()
        
    def GetSnapshotOfDatabase(self):
        """Pull all the database data through the database manager. 
        So now we put what we pulled in self.DatabaseUserData self.DatabaseStockData."""
        pass

    def set_current_user_data(username, password):
        """Now we have the username, password check it against self.DatabaseUserData. 
        Get userid from that and create self.current_user_data self.current_user_stocks"""
        pass

    def CreateLogin_GUI(self):
        """Creates Login Gui. """
        self.LoginGUIObject = LoginGUI(self)

    def login_user(self, username, password):
        """ Do ValidateUsernamePassword. If valid:
        CreateUserObject then CreateDashboardController.
        Else error message pop-up GUI."""
        
    def SignUpUserProcessing(self, username, password):
        """Called by Sign up GUI passes in username password. 
        Calls validate username password.
        If valid calls Login GUI. else popup"""
        pass

    def ForgetPasswordProcessing(self, security_question_answer, newpassword, username):
        """Call VerifySecurityQuestionAnswerUsername if its correct reset password for user in DB.
        then creates login gui.
        Else error message pop up GUI."""

        pass
    def ValidateUsernamePassword(self):
        """checks against DB.
        checks len of pw checks everything else to do with it and
        Calls check username taken.
        returns true/false"""
        pass
    def CheckUsernameTaken(self):
        """If new user check if the username already exist. 
        
        returns true/false"""
        pass
    def VerifySecurityQuestionAnswerUsername(self, security_question_answer, username):
        """Here we check if the passed in security_question_answer 
        is the same in the username.
        returns true/false"""
        
    def logout_push_changes_to_database(self):
        """Check what has to be changed userobject vs self.current_user_data self.current_user_stocks.
        Whatever has to be change it (insert if doesnt exist stockid or user id -1, update else."""
        #self.DatabaseManagesObject
    
    def create_sign_up_GUI(self):
        self.sign_up_gui_object = SignUpGUI(self)
        
    def CreateDashboardController(self):
        """Creates Dashboard Controller"""
        DashboardController(self, self.user_object,self.popup_GUI_object) #dont need reference

    def CreateUserObject(self, current_user_data, current_user_stocks):
        """Creates user object"""
        self.user_object = User(current_user_data, current_user_stocks)
    
    def create_popup_GUI(self, message):
        """creates a pop-up GUI with given error message."""
        self.popup_GUI_object.create_pop_up(message)