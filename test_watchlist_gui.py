from tkinter import *
import watchlist_GUI
from test_user import create_valid_user_object
from main import set_env_variables
set_env_variables()
root = Tk()
root.geometry("700x700")

stock_symbol = "TSLA"
stockInfo = {'TSLA':{'currentRatio': 1.508, 'trailingEPS': 1.897, 'PERatio': 412.6252, 'DebtToEquityRatio': 42.552, 'stockPrice': 782.75}}


description = "This"
userObject = create_valid_user_object()
loginGUIObject = watchlist_GUI.WatchlistGUI(root, userObject,[["TSLA", 0.2]], 
        [["AAPL", -0.3]], description, stockInfo )
root.mainloop()