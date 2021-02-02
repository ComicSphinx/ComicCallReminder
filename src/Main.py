# @Author: Daniil Maslov (ComicSphinx)

import sys
from PyQt5 import QtWidgets
from datetime import datetime as dt

import design.MainWindow
from List import ListWidget
from database.DatabaseUtilities import DatabaseUtilities as dbu

class MainWindow(QtWidgets.QMainWindow, design.MainWindow.Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        if (dbu.verifyDatabaseExist(dbu) == False):
            dbu.createDB(dbu)

        self.initUI()
    
    def initUI(self):
        self.btn_remind.clicked.connect(self.clicked_remind)
        self.btn_show.clicked.connect(self.clicked_show)
        
    def clicked_remind(self):
        time, number, comment = self.getData()
        tmpString = dbu.buildInsert(dbu, time, number, comment)
        dbu.insertDataToDB(dbu, tmpString)
        # в конце нужно очистить все поля и выдать уведомление - сохранено

    def clicked_show(self):
        self.list = ListWidget()
        self.list.show()

    def getData(self):
        time = self.timeEdit.time()
        number = self.numberTextEdit.toPlainText()
        comment = self.commentTextEdit.toPlainText()
        print(time,number,comment)
        return time, number, comment

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()