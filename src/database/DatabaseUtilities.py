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
        connection, cursor = self.connectDB(self)
        cursor.execute("CREATE TABLE records (year int, month int, day int, te time , number VARCHAR(12), comment VARCHAR(200));")
        self.saveAndCloseDB(self, connection)

    def connectDB(self):
        connection = sqlite3.connect(self.databaseFilePath)
        cursor = connection.cursor()
        return connection, cursor
    
    def saveAndCloseDB(self, connection):
        connection.commit()
        connection.close()

    def insertDataToDB(self, str):
        connection, cursor = self.connectDB(self)
        cursor.execute(str)
        self.saveAndCloseDB(self, connection)

    def buildInsert(self, time, number, comment):
        insert = "INSERT INTO records VALUES("
        insert += "'" + str(dt.now().year)
        insert += "','" + str(dt.now().month)
        insert += "','" + str(dt.now().day)
        insert += "','" + str(time)
        insert += "','" + str(number)
        insert += "', '" + comment + "');"
        return insert     

    def buildSelect(self, year, month, day):
        select = "SELECT * FROM records WHERE year = "
        select += str(year)
        select += " AND month = "
        select += str(month)
        select += " AND day = "
        select += str(day)
        return select

    def getTimesNumbersCommentsBySelect(self, data):
        times = []
        numbers = []
        comments = []
        for i in range(len(data)):
            times.append(data[i][3])
            numbers.append(data[i][4])
            comments.append(data[i][5])
        return times, numbers, comments