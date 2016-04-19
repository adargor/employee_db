# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ErrWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ErrWindow(object):
    def setupUi(self, ErrWindow):
        ErrWindow.setObjectName("ErrWindow")
        ErrWindow.resize(330, 146)
        self.label = QtWidgets.QLabel(ErrWindow)
        self.label.setGeometry(QtCore.QRect(40, 20, 261, 71))
        self.label.setObjectName("label")
        self.errButton = QtWidgets.QPushButton(ErrWindow)
        self.errButton.setGeometry(QtCore.QRect(110, 100, 113, 32))
        self.errButton.setObjectName("errButton")

        self.retranslateUi(ErrWindow)
        QtCore.QMetaObject.connectSlotsByName(ErrWindow)

    def retranslateUi(self, ErrWindow):
        _translate = QtCore.QCoreApplication.translate
        ErrWindow.setWindowTitle(_translate("ErrWindow", "Ошибка"))
        self.label.setText(_translate("ErrWindow", "Все поля должны быть заполнены"))
        self.errButton.setText(_translate("ErrWindow", "ОК"))

