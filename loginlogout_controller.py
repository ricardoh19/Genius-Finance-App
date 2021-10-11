from popupGUI import PopupGUI
from dashboard_controller import DashboardControllers
from database_manager import DB
from loginGUI import LoginGUI

class LoginLogoutControllers():
    def __init__(self ):
        #initializes and pulls data from DB
        self.DatabaseManagesObject = DB()
        self.DatabaseUserData = DatabaseUserData
        self.DatabaseStockData = DatabaseStockData
        self.current_user_data = current_user_data
        self.current_user_stocks = current_user_stocks
        #create popupgui object
        self.PopUpGUIObject = PopupGUI()

        self.LoginGUIObject = LoginGUI(self)
    def GetSnapshotOfDatabase():
        pass
    def Setcurrent_user_data():
        pass
    def CreateLogin_GUI():
        pass
    def create_database_manager():
        pass
    def SignUpUserProcessing():
        pass
    def ForgetPasswordProcessing():
        pass
    def ValidateUsernamePassword():
        pass
    def CheckUsernameTaken():
        pass
    def VerifySecurityQuestionAnswerUsername():
        pass
    def logout_push_changes_to_database():
        pass
    def CreateDashboardController():
        pass
    
    