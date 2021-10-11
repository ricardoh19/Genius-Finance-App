from __future__ import print_function
import sys
import mysql.connector
from mysql.connector import errorcode




# Create and modify the Genius Finance database.
class DB():
    def __init__(self):
        self.createDatabaseManager() 
        #creates db if necessary

    '''
    Intent: Connects to SQL database, returns cursor to database
    * Preconditions: myuser, mypassword, myhost (and db if given) variables to have valid values for the root 
    * user of a given MySQL server or a given database
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
    Intent: Creates tables for database.
    * Preconditions: 
    * 
    * Postconditions:
    * Post0. Database GeniusFinanceDB and table/tables are created successfully.
    * Post1. Table already Exists
    * post2. Failed creating database
    '''
    def createDatabaseManager(self):
        '''
        Intent: Creates the database 
        * Preconditions: 
        * DB_name variable is created and set to correct database name.
        * Postconditions:
        * Post0. Database GeniusFinanceDB is created successfully.
        * post1. Failed creating database
        '''
        def create_database(cursor):
            try:
                cursor.execute(f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
            except mysql.connector.Error as err:
                print(f"Failed creating database: {err}")
                sys.exit(1)

        DB_NAME = 'GeniusFinanceDB'
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
            cursor.execute(f"USE {DB_NAME}")
        except mysql.connector.Error as err:
            print(f"Database {DB_NAME} does not exists.")
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print(f"Database {DB_NAME} created successfully.")
                cnx.database = DB_NAME
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
    *cursor is connected to correct database
    * Postconditions:
    * PostO. selects all data that is stored in the User table
    * Post1. Displays None
    '''
    def getDatabaseUserData(self):
        cursor, cnx = self.connect_to_db(db="GeniusFinanceDB")
        query = (f'SELECT * FROM User')
        cursor.execute(query)
        

    '''
    Intent: Query Stock data from database
    * Preconditions: 
    * cursor is connected to correct database
    * Postconditions:
    * PostO. selects all data that is stored in the Stock table
    * Post1. Displays None
    '''
    def getDatabaseStockData(self):
        cursor, cnx = self.connect_to_db(db="GeniusFinanceDB")
        query = (f'SELECT * FROM Stock')
        cursor.execute(query)
        

    '''
    Intent: Inserts data into User table
    * Preconditions: 
    * cursor is connected to correct database
    * Postconditions:
    * PostO. username, password, securityQuestionAnswer is in the database
    * Post1. Data is not inserted into the database
    '''
    def insertDatabaseUserData(self, username, password, securityQuestionAnswer):
        cursor, cnx = self.connect_to_db(db="GeniusFinanceDB")
        query = ("INSERT INTO User "
                    "(username, password, securityQuestionAnswer) "
                    "VALUES (%s, %s, %s)")
        data = (username, password,securityQuestionAnswer)
        cursor.execute(query, data)
        cnx.commit()

    '''
    Intent: Inserts data into Stock table
    * Preconditions: 
    * cursor is connected to correct database
    * Postconditions:
    * PostO. username, password, securityQuestionAnswer is in the database
    * Post1. Data is not inserted into the database
    '''
    def insertDatabaseStockData(self, stockName,userId,stockOwnedAmount):
        cursor, cnx = self.connect_to_db(db="GeniusFinanceDB")
        query = ("INSERT INTO Stock "
                    "(stockName, SELECT userId FROM User WHERE userId='2', stockOwnedAmount)"
                    "VALUES (%s, %s,%s)")
                    
        data = (stockName,userId,stockOwnedAmount)
        cursor.execute(query, data)
        cnx.commit()
        
