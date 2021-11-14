from dashboard_controller import DashboardController

def test_dashboard():
    userObject = None
    DashboardControllerTest = DashboardController(userObject)

    # search symbol method
    dashboardGUI = None
    stock_symbol = "tsla"
    result = DashboardControllerTest.searchStockSymbol(stock_symbol, dashboardGUI)
    print(result)
    
if __name__ == "__main__":
    test_dashboard()
    