# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 302, 171))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.timeEdit = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.timeEdit.setMinimumSize(QtCore.QSize(300, 50))
        self.timeEdit.setMaximumSize(QtCore.QSize(100, 50))
        self.timeEdit.setObjectName("timeEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.timeEdit)
        self.numberTextEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.numberTextEdit.setMaximumSize(QtCore.QSize(150, 100))
        self.numberTextEdit.setObjectName("numberTextEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numberTextEdit)
        self.commentTextEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.commentTextEdit.setMaximumSize(QtCore.QSize(150, 100))
        self.commentTextEdit.setObjectName("commentTextEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.commentTextEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 170, 301, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.showButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.showButton.setMinimumSize(QtCore.QSize(0, 50))
        self.showButton.setObjectName("showButton")
        self.horizontalLayout.addWidget(self.showButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Comic Call Reminder"))
        self.numberTextEdit.setPlaceholderText(_translate("MainWindow", "Номер телефона"))
        self.commentTextEdit.setPlaceholderText(_translate("MainWindow", "Комментарий"))
        self.pushButton.setText(_translate("MainWindow", "Запомнить"))
        self.showButton.setText(_translate("MainWindow", "Просмотреть список"))