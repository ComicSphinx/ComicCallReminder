# @Author: Daniil Maslov (ComicSphinx)

import sys
from PyQt5 import QtWidgets
from datetime import datetime as dt

import design.MainWindow
import design.List.Ui_List
from database.DatabaseUtilities import DatabaseUtilities as dbu

class MainWindow(QtWidgets.QMainWindow, design.MainWindow.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        if (dbu.verifyDatabaseExist(dbu) == False):
            dbu.createDB(dbu)

        self.initUI()
    
    def initUI(self):
        self.pushButton.clicked.connect(self.btnClicked)
        self.showButton.clicked.connect(self.showClicked)
        
    def btnClicked(self):
        time, number, comment = self.getData()
        tmpString = dbu.buildInsertString(time, number, comment)
        dbu.insertDataToDB(tmpString)
        # в конце нужно очистить все поля и выдать уведомление - сохранено

    def showClicked(self):
        #Ui_List.show()

    def getData(self):
        time = self.timeEdit.time()
        number = self.numberTextEdit.toPlainText()
        comment = self.commentTextEdit.toPlainText()
        return time, number, comment

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()