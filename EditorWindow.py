# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditorWindow(object):
    def setupUi(self, EditorWindow):
        EditorWindow.setObjectName("EditorWindow")
        EditorWindow.resize(400, 300)
        self.label = QtWidgets.QLabel(EditorWindow)
        self.label.setGeometry(QtCore.QRect(50, 20, 59, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EditorWindow)
        self.label_2.setGeometry(QtCore.QRect(50, 70, 59, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(EditorWindow)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 59, 16))
        self.label_3.setObjectName("label_3")
        self.idLine = QtWidgets.QLineEdit(EditorWindow)
        self.idLine.setEnabled(False)
        self.idLine.setGeometry(QtCore.QRect(160, 20, 113, 21))
        self.idLine.setObjectName("idLine")
        self.nameLine = QtWidgets.QLineEdit(EditorWindow)
        self.nameLine.setGeometry(QtCore.QRect(160, 70, 113, 21))
        self.nameLine.setObjectName("nameLine")
        self.ageLine = QtWidgets.QLineEdit(EditorWindow)
        self.ageLine.setGeometry(QtCore.QRect(160, 110, 113, 21))
        self.ageLine.setObjectName("ageLine")
        self.btnCommit = QtWidgets.QPushButton(EditorWindow)
        self.btnCommit.setGeometry(QtCore.QRect(120, 250, 113, 32))
        self.btnCommit.setObjectName("btnCommit")
        self.btnClose = QtWidgets.QPushButton(EditorWindow)
        self.btnClose.setGeometry(QtCore.QRect(240, 250, 113, 32))
        self.btnClose.setObjectName("btnClose")
        self.label_4 = QtWidgets.QLabel(EditorWindow)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 81, 16))
        self.label_4.setObjectName("label_4")
        self.departmentBox = QtWidgets.QComboBox(EditorWindow)
        self.departmentBox.setGeometry(QtCore.QRect(160, 190, 171, 26))
        self.departmentBox.setObjectName("departmentBox")
        self.label_5 = QtWidgets.QLabel(EditorWindow)
        self.label_5.setGeometry(QtCore.QRect(50, 150, 81, 16))
        self.label_5.setObjectName("label_5")
        self.jobLine = QtWidgets.QLineEdit(EditorWindow)
        self.jobLine.setGeometry(QtCore.QRect(160, 150, 113, 21))
        self.jobLine.setObjectName("jobLine")

        self.retranslateUi(EditorWindow)
        self.btnClose.clicked.connect(EditorWindow.close)
        QtCore.QMetaObject.connectSlotsByName(EditorWindow)

    def retranslateUi(self, EditorWindow):
        _translate = QtCore.QCoreApplication.translate
        EditorWindow.setWindowTitle(_translate("EditorWindow", "Редактор данных сотрудника"))
        self.label.setText(_translate("EditorWindow", "Id:"))
        self.label_2.setText(_translate("EditorWindow", "Имя:"))
        self.label_3.setText(_translate("EditorWindow", "Возраст:"))
        self.btnCommit.setText(_translate("EditorWindow", "OK"))
        self.btnClose.setText(_translate("EditorWindow", "Отмена"))
        self.label_4.setText(_translate("EditorWindow", "Отдел:"))
        self.label_5.setText(_translate("EditorWindow", "Должность:"))

