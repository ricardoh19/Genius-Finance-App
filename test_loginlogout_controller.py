from loginlogout_controller import LoginLogoutControllers

def test_getSnapshotOfDatabase():
    loginlogoutController = LoginLogoutControllers()
    result = loginlogoutController.getSnapshotOfDatabase()
    print(result)

def test_setCurrentUserData():
    loginlogoutController = LoginLogoutControllers()
    result = loginlogoutController.setCurrentUserData("john")
    print(result)

def test_setCurrentStockData():
    loginlogoutController = LoginLogoutControllers()
    result = loginlogoutController.setCurrentStockData("john")
    print(result)


def test_verifySecurityQuestionAnswerUsername():
    loginlogoutController = LoginLogoutControllers()
    result = loginlogoutController.verifySecurityQuestionAnswerUsername("sosa", "john")
    print(result)


def test_validateUsernamePassword():
    loginlogoutController = LoginLogoutControllers()
    # unique username and validated password
    result = loginlogoutController.validateUsernamePassword("johnO", "Passwrd1233#")
    print(result)

def test_checkUsernameTaken():
    loginlogoutController = LoginLogoutControllers()
    # unique username and validated password
    result = loginlogoutController.checkUsernameTaken("john")
    print(result)

def test_checkPasswordCorrect():
    loginlogoutController = LoginLogoutControllers()
    # unique username and validated password
    result = loginlogoutController.checkPasswordCorrect("ricardo", "Password1234!")
    print(result)

def test_loginUser():
    loginlogoutController = LoginLogoutControllers()
    # unique username and validated password
    result = loginlogoutController.loginUser("johnO", "Passwrd1234#")
    print(result)



if __name__ == "__main__":
    #test_getSnapshotOfDatabase()
    #test_setCurrentUserData()
    #test_setCurrentStockData()
    #test_verifySecurityQuestionAnswerUsername()
    #test_validateUsernamePassword()
    #test_checkUsernameTaken()
    #test_loginUser()
    test_checkPasswordCorrect()
    