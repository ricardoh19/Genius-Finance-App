from popupGUI import PopupGUI
from dashboard_controller import DashboardControllers
from database_manager import DB
from loginGUI import LoginGUI

class login_logout_controllers():
    def __init__(self ):
        #initializes and pulls data from DB
        self.DatabaseManagesObject = DB()
        # get this data from DB Manager
        self.DatabaseUserData = None
        self.DatabaseStockData = None
        self.current_user_data = None
        self.current_user_stocks = None
        #create popupgui object
        self.popup_GUI_object = PopupGUI()

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
    
    