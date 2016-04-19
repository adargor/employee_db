# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddWindow(object):
    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(400, 300)
        self.label_2 = QtWidgets.QLabel(AddWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 20, 59, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 59, 16))
        self.label_3.setObjectName("label_3")
        self.nameLine = QtWidgets.QLineEdit(AddWindow)
        self.nameLine.setGeometry(QtCore.QRect(140, 20, 113, 21))
        self.nameLine.setObjectName("nameLine")
        self.ageLine = QtWidgets.QLineEdit(AddWindow)
        self.ageLine.setGeometry(QtCore.QRect(140, 50, 113, 21))
        self.ageLine.setObjectName("ageLine")
        self.btnCommit = QtWidgets.QPushButton(AddWindow)
        self.btnCommit.setGeometry(QtCore.QRect(120, 250, 113, 32))
        self.btnCommit.setObjectName("btnCommit")
        self.btnClose = QtWidgets.QPushButton(AddWindow)
        self.btnClose.setGeometry(QtCore.QRect(240, 250, 113, 32))
        self.btnClose.setObjectName("btnClose")
        self.label = QtWidgets.QLabel(AddWindow)
        self.label.setGeometry(QtCore.QRect(50, 120, 81, 16))
        self.label.setObjectName("label")
        self.departmentBox = QtWidgets.QComboBox(AddWindow)
        self.departmentBox.setGeometry(QtCore.QRect(130, 110, 191, 30))
        self.departmentBox.setObjectName("departmentBox")
        self.jobLine = QtWidgets.QLineEdit(AddWindow)
        self.jobLine.setGeometry(QtCore.QRect(140, 80, 113, 21))
        self.jobLine.setObjectName("jobLine")
        self.label_4 = QtWidgets.QLabel(AddWindow)
        self.label_4.setGeometry(QtCore.QRect(50, 80, 81, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(AddWindow)
        self.btnClose.clicked.connect(AddWindow.close)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "Добавление сотрудника"))
        self.label_2.setText(_translate("AddWindow", "Имя:"))
        self.label_3.setText(_translate("AddWindow", "Возраст:"))
        self.btnCommit.setText(_translate("AddWindow", "OK"))
        self.btnClose.setText(_translate("AddWindow", "Отмена"))
        self.label.setText(_translate("AddWindow", "Отдел:"))
        self.label_4.setText(_translate("AddWindow", "Должность:"))

