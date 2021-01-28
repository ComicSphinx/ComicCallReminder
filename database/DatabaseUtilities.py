import sqlite3
import os
from datetime import datetime as dt

class DatabaseUtilities():

    databaseFilePath = "database/database.db"
    
    def verifyDatabaseExist(self):
        if (os.path.exists(self.databaseFilePath)):
            return 1
        else:
            return 0

    def createDB(self):
        """ Create database and connect to it """
        connection, cursor = self.connectDB(self)
        """ Create table in database (year, month | day | minutes | record)"""
        cursor.execute("CREATE TABLE records (year int, month int, day int, te time , number VARCHAR(12), comment VARCHAR(200));")
        """ Save changes and close connection """
        self.saveAndCloseDB(self, connection)

    def connectDB(self):
        """ Connect to database """
        connection = sqlite3.connect(self.databaseFilePath)
        cursor = connection.cursor()
        return connection, cursor
    
    def saveAndCloseDB(self, connection):
        """ Save changes """
        connection.commit()
        """ Close connection """
        connection.close()

    def insertDataToDb(self, str):
        connection, cursor = self.connectDB(self)
        cursor.execute(str)
        self.saveAndCloseDB(self, connection)


    def buildInsertString(self, time, number, comment):
        tmpString = "INSERT INTO records VALUES("
        tmpString += str(dt.now().year)
        tmpString += "," + str(dt.now().month)
        tmpString += "," + str(dt.now().day)
        tmpString += "," + str(time)
        tmpString += "," + str(number)
        tmpString += "," + comment + "');"
        return tmpString     