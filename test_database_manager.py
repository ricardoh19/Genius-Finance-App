from database_manager import DB

def test_database_manager():
    databaseTest = DB()

    # 2 method
    #databaseTest.insertDatabaseUserData("ricardoh","passwrd","sosa")
    # 1 mthod
    #databaseTest.getDatabaseUserData(1)

    # 3 method
    #databaseTest.insertDatabaseStockData("stock2",38,50)
    # 4 method
    #databaseTest.getDatabaseStockData(1)

    # 5 method
    #databaseTest.updateDatabaseUserData(1, "password", "skateboarding")
    #print(databaseTest.getDatabaseUserData())

    # 6 method
    #databaseTest.updateDatabaseStockData(1, 40)
    print (databaseTest.getDatabaseStockData())

    
if __name__ == "__main__":
    test_database_manager()
    