
class SignUpGUI():
    def __init__(self, LoginLogout):
        self.LoginLogout = LoginLogout
        self.username = ""
        self.password = ""
        self.ReenteredPassword = ""
        self.SecurityQuestionAnswer = ""
        
    def HandleSignUpEvent():
        pass
    def HandleCloseEvent():
        pass
    def CreateMainFrame():
        pass
    def CreateUsernamePasswordFrame():
        pass
    def CreateSecurityQuestionFrame():
        pass
    def create_pop_up(self, message):
        self.LoginLogout.create_popup_GUI( message)