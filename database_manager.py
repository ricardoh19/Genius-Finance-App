from __future__ import print_function
import sys
import mysql.connector
from mysql.connector import errorcode

import os


# This class creates and maintains the Genius Finance database with methods: 
# connect_to_db, createDatabaseManager,create_database, getDatabaseUserData, 
# getDatabaseStockData, insertDatabaseUserData, insertDatabaseStockData.
class DB():
    def __init__(self):
        #creates db if necessary
        #get db name from environment 
        try:
            self.DB_NAME = str(os.getenv('DB_NAME'))
        except Exception as e:
            print("Check that MySQL database name is provided in main.py .")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
            sys.exit(1)
        
        self.createDatabaseManager() 
        

    '''
    Intent: Connects to SQL database, returns cursor and cnx (connection) to database.
    * Cursor interacts with the MySQL server and executes operations on the database.  
    * Preconditions: myuser, mypassword, myhost (and db if given) variables to have valid values for the root 
    * user of a given MySQL server or a given database.
    * Postconditions:
    * Post0. The connection to a database db is established (if db is not None) 
    * Post1. The connection to a MySQL server is established (if db is None)
    '''
    def connect_to_db(self, db = None):
        try:
            myuser = str(os.getenv('SQLUser'))
            mypassword = str(os.getenv('SQLPassword')) 
            myhost = str(os.getenv('SQLHost'))
        except Exception as e:
            print("Check that MySQL database user, password and host are provided in main.py .")
            print("Oops!", sys.exc_info()[0], "occurred.")
            print("Exception: ", e)
        if db:
            cnx = mysql.connector.connect(
            user=myuser, 
            password=mypassword,
            host=myhost,
            database=db)
            self.cursor = cnx.cursor()
            return self.cursor, cnx            
        else:
            cnx = mysql.connector.connect(
            user=myuser, 
            password=mypassword,
            host=myhost)
            self.cursor = cnx.cursor()
            return self.cursor, cnx
        
    '''
    Intent: Creates database and tables in that database.
    * Preconditions: 
    * Connection to database is established.
    * Tables User and Stock are already formatted and ready to be created.
    * Postconditions:
    * Post0. Database is created successfully if database does not exist already.
    * Post1. Tables are created successfully if tables do not exist already.
    * Post2. Failed creating database and error is thrown if database can not be created.
    * Post3. Failed creating tables and error is thrown if tables can not be created.
    '''
    def createDatabaseManager(self):
        '''
        Intent: Creates the database 
        * Preconditions: 
        * DB_name variable is created and set to correct database name.
        * Postconditions:
        * Post0. Database GeniusFinanceDB is created successfully if no exception is thrown.
        * post1. if exception (mysql.connector.Error) is thrown, database can not created
        '''
        def create_database(cursor):
            
            try:
                cursor.execute(f"CREATE DATABASE {self.DB_NAME} DEFAULT CHARACTER SET 'utf8'")
            except mysql.connector.Error as err:
                print(f"Failed creating database: {err}")
                sys.exit(1)

        #DB_NAME = 'GeniusFinanceDB'
        TABLES = {}
        TABLES['User'] = (
            "CREATE TABLE `User` ("
            "  `userId` int(11) NOT NULL AUTO_INCREMENT,"
            "  `username` varchar(40)  NOT NULL,"
            "  `password` varchar(15) NOT NULL,"
            "  `securityQuestionAnswer` varchar(15) NOT NULL,"
            "  PRIMARY KEY (`userId`)"
            ") ENGINE=InnoDB")

        TABLES['Stock'] = (
            "CREATE TABLE `Stock` ("
            "  `stockId` int(11) NOT NULL AUTO_INCREMENT,"
            "  `stockName` varchar(20) NOT NULL,"
            "  `userId` int(11) NOT NULL,"
            "  `StockOwnedAmount` int(11) NOT NULL,"
            "  PRIMARY KEY (`stockId`), FOREIGN KEY (`userId`) REFERENCES `User` (`userId`) "
            ") ENGINE=InnoDB")
            
        #connect to mysql server as root user
        cursor, cnx = self.connect_to_db()
       

        #check if database name already exists otherwise create it 
        try:
            cursor.execute(f"USE {self.DB_NAME}")
            
        except mysql.connector.Error as err:
            print(f"Database { self.DB_NAME} does not exists.")
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print(f"Database { self.DB_NAME} created successfully.")
                cnx.database =  self.DB_NAME
                
            else:
                print(err)
                sys.exit(1)

        #specify table description for the table 
        
        for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                
                else:
                    print(err.msg)
            else:
                print("OK")

        
        cursor.close()
        cnx.close()

   
    '''
    Intent: Query User data from database. Return a list of all User data from database
    * Preconditions: 
    * cursor is connected to correct database (GeniusFinanceDB)
    * User table already exists.
    * Postconditions:
     * Post0. Selects all data from the User table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getDatabaseUserData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM User")
        cursor.execute(query)
        return [i for i in cursor]
        


    '''
    Intent: Query all Stock data from database,return a list of all Stock data from database. 
    * Preconditions: 
    * cursor is connected to correct database (GeniusFinanceDB)
    * Stock table already exists.
    * Postconditions:
    * Post0. Selects all data from the Stock table if connection to database if successful.
    * Post1. Displays None if connection to database is not successful.
    '''
    def getDatabaseStockData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM Stock")
        cursor.execute(query)
        return [i for i in cursor]


    '''
    Intent: Inserts data into User table
    * Preconditions: 
    * cursor is connected to correct database
    * User table already exists.
    * username, password, and securityQuestionAnswer are validated.
    * username, password, and securityQuestionAnswer are strings.
    * Postconditions:
    * PostO. username, password, securityQuestionAnswer is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
    * Post2. Data is not inserted into the database if a parameter or all parameters are equal to None.
    '''
    def insertDatabaseUserData(self, username, password, securityQuestionAnswer):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("INSERT INTO User "
                    "(username, password, securityQuestionAnswer) "
                    "VALUES (%s, %s, %s)")
        data = (username, password,securityQuestionAnswer)
        cursor.execute(query, data)
        cnx.commit()

    '''
    Intent: Inserts data into Stock table
    * Preconditions: 
    * userId matches with userID that is currently logged in.
    * DB_Name is equal to 'GeniusFinanceDB'.
    * Table that is being inserted to is "Stock" and already exists.
    * cursor is connected to correct database (GeniusFinanceDB)
    * Postconditions:
    * PostO. stockName and stockOwnedAmount is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
    * Post2. Data is not inserted into the database if a parameter or all parameters are equal to None.
    '''
    def insertDatabaseStockData(self, stockName,userId,stockOwnedAmount):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"INSERT INTO Stock"
                    "(stockName, userId, stockOwnedAmount) "
                    "VALUES (%s, %s, %s)")
        data = (stockName, userId, stockOwnedAmount)
        cursor.execute(query,data)
        cnx.commit()


   
    '''
    Intent: Deletes data from Stock table
    * Preconditions: 
    * DB_Name is equal to 'GeniusFinanceDB'.
    * Table that is being deleted from is "Stock" and already exists.
    * cursor is connected to correct database (GeniusFinanceDB)
    * Postconditions:
    * PostO. stockName and stockOwnedAmount is inserted into the database if connection to database is successful.
    * Post1. Data is not deleted from the database if connection to database fails.
    * Post2. Data is not deleted from the database if a parameter or all parameters are equal to None.
    '''
    def deleteDatabaseStockData(self, stockName):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"DELETE FROM Stock WHERE stockName = '{stockName}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Updates data into User table
    * Preconditions: 
    * userId matches with userID that is currently logged in.
    * DB_Name is equal to 'GeniusFinanceDB'.
    * Table that is being updated to is "User" and already exists.
    * cursor is connected to correct database (GeniusFinanceDB)
    * usernameOrPassword is a string that is either equal to "username" or "password"
    * newValue is a validated username or password
    * username or password are the only valued from User table that can be changed.

    * Postconditions:
    * PostO. username is updated in the database if connection to database is successful.
    * Post1. password is updated in the database if connection to database is successful.
    * Post2. Data is not updated in the database if connection to database fails.
    * Post3. Data is not updated in the database if username or password input type is not a string
    * Post4. Data is not updated in the database if username or password is equal to None.
    '''
    def updateDatabaseUserData(self, username, usernameOrPassword, newValue):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        if usernameOrPassword == "username":
            query = (f"UPDATE User SET username = '{newValue}' WHERE username = '{username}'")
        elif usernameOrPassword == "password":
            query = (f"UPDATE User SET password = '{newValue}' WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()

    '''
    Intent: Updates data into Stock table
    * Preconditions: 
    * userId matches with userID that is currently logged in.
    * DB_Name is equal to 'GeniusFinanceDB'.
    * Table that is being updated to is "Stock" and already exists.
    * cursor is connected to correct database (GeniusFinanceDB)
    * stockOwnedAmount is an integer and the only value from Stock table that can being changed.
    * Postconditions:
    * PostO. stockOwnedAmount is updated in the database if connection to database is successful.
    * Post1. Data is not updated in the database if connection to database fails.
    * post2. Data is not updated in the database if stockOwnedAmount input type is not an integer
    '''
    def updateDatabaseStockData(self, username,stockOwnedAmount):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = (f"UPDATE Stock SET stockOwnedAmount = {stockOwnedAmount} WHERE username = '{username}'")
        cursor.execute(query)
        cnx.commit()
        
    