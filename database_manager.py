from __future__ import print_function
import sys
import mysql.connector
from mysql.connector import errorcode




# This class creates and maintains the Genius Finance database with methods: connect_to_db, createDatabaseManager,create_database, getDatabaseUserData, getDatabaseStockData, insertDatabaseUserData, insertDatabaseStockData.
class DB():
    def __init__(self):
        #creates db if necessary
        self.createDatabaseManager() 
        self.DB_NAME = 'GeniusFinanceDB'

    '''
    Intent: Connects to SQL database, returns cursor and cnx (connection) to database.
    * Cursor interacts with the MySQL server and executes operations on the database.  
    * Preconditions: myuser, mypassword, myhost (and db if given) variables to have valid values for the root 
    * user of a given MySQL server or a given database.
    * Postconditions:
    * Post0. The connection to a database db is established (if db is not None) 
    * Post1. The connection to a MySQL server is established (if db is None)
    '''
    def connect_to_db(self, myuser='root', mypassword='Rhern_19',myhost= "localhost", db = None):
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
    * 
    * Postconditions:
    * Post0. Database is created successfully if database does not exist already.
    * Post1. Tables are created successfully if tables do not exist already.
    * Post1. Failed creating database and error is shown if database can not be created.
    '''
    def createDatabaseManager(self):
        '''
        Intent: Creates the database 
        * Preconditions: 
        * DB_name variable is created and set to correct database name.
        * Postconditions:
        * Post0. Database GeniusFinanceDB is created successfully if no exception is thrown.
        * post1. if exception (mysql.connector.Error) is thrown, database is not created
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
            print(f"Database {self.DB_NAME} does not exists.")
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print(f"Database {self.DB_NAME} created successfully.")
                cnx.database = self.DB_NAME
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
    Intent: Query User data from database
    * Preconditions: 
    * cursor is connected to correct database (GeniusFinanceDB)
    * User table already exists.
    * Postconditions:
    * PostO. Selects all data that is stored in the User table if the table contains data.
    * Post1. Displays None if no data is in the User table
    '''
    def getDatabaseUserData(self):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM User")
        cursor.execute(query)
        

    '''
    Intent: Query Stock data from database
    * Preconditions: 
    * cursor is connected to correct database (GeniusFinanceDB)
    * Stock table already exists.
    * userId (Int) that is passed as a parameter already exists.
    * Postconditions:
    * Post0. Selects all data that matches with given userId.
    * Post1. Displays None if no data pertaining to userId is in the Stock table.
    '''
    def getDatabaseStockData(self, userId):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("SELECT * FROM User WHERE userId='userId'")
        cursor.execute(query)
        

    '''
    Intent: Inserts data into User table
    * Preconditions: 
    * cursor is connected to correct database
    * username, password, and securityQuestionAnswer are verified.
    * username, password, and securityQuestionAnswer are strings.
    * Postconditions:
    * PostO. username, password, securityQuestionAnswer is inserted into the database if connection to database is successful.
    * Post1. Data is not inserted into the database if connection to database fails.
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
    '''
    def insertDatabaseStockData(self, stockName,userId,stockOwnedAmount):
        cursor, cnx = self.connect_to_db(db=self.DB_NAME)
        query = ("INSERT INTO Stock "
                    "(stockName, SELECT userId FROM User WHERE userId='userId', stockOwnedAmount)"
                    "VALUES (%s, %s,%s)")
                    
        data = (stockName,userId,stockOwnedAmount)
        cursor.execute(query, data)
        cnx.commit()
        
