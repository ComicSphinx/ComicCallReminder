import sys
from PyQt5 import QtWidgets
import design.ListWidget
from database.DatabaseUtilities import DatabaseUtilities as dbu
from datetime import datetime as dt

class ListWidget(QtWidgets.QWidget, design.ListWidget.Ui_List):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.printRecords()

    def printRecords(self):
        select = dbu.buildSelect(dbu, dt.now().year, dt.now().month, dt.now().day)
        times, numbers, comments = dbu.getTimesNumbersCommentsBySelect(dbu, select)
        labelA = QtWidgets.QLabel("hah")

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ListWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()