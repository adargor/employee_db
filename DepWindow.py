# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DepWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DepWindow(object):
    def setupUi(self, DepWindow):
        DepWindow.setObjectName("DepWindow")
        DepWindow.resize(544, 398)
        DepWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.gridLayout = QtWidgets.QGridLayout(DepWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.delDepButton = QtWidgets.QPushButton(DepWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delDepButton.sizePolicy().hasHeightForWidth())
        self.delDepButton.setSizePolicy(sizePolicy)
        self.delDepButton.setAutoDefault(False)
        self.delDepButton.setObjectName("delDepButton")
        self.gridLayout.addWidget(self.delDepButton, 5, 0, 1, 3)
        self.depTable = QtWidgets.QTableWidget(DepWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depTable.sizePolicy().hasHeightForWidth())
        self.depTable.setSizePolicy(sizePolicy)
        self.depTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.depTable.setTabKeyNavigation(False)
        self.depTable.setAlternatingRowColors(True)
        self.depTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.depTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.depTable.setObjectName("depTable")
        self.depTable.setColumnCount(2)
        self.depTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.depTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.depTable.setHorizontalHeaderItem(1, item)
        self.depTable.horizontalHeader().setStretchLastSection(True)
        self.depTable.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.depTable, 0, 0, 1, 4)
        self.lineEditDep = QtWidgets.QLineEdit(DepWindow)
        self.lineEditDep.setObjectName("lineEditDep")
        self.gridLayout.addWidget(self.lineEditDep, 2, 3, 1, 1)
        self.addDepButton = QtWidgets.QPushButton(DepWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDepButton.sizePolicy().hasHeightForWidth())
        self.addDepButton.setSizePolicy(sizePolicy)
        self.addDepButton.setAutoDefault(False)
        self.addDepButton.setObjectName("addDepButton")
        self.gridLayout.addWidget(self.addDepButton, 1, 0, 2, 3)
        self.exitDepButton = QtWidgets.QPushButton(DepWindow)
        self.exitDepButton.setAutoDefault(False)
        self.exitDepButton.setObjectName("exitDepButton")
        self.gridLayout.addWidget(self.exitDepButton, 5, 3, 1, 1)

        self.retranslateUi(DepWindow)
        QtCore.QMetaObject.connectSlotsByName(DepWindow)

    def retranslateUi(self, DepWindow):
        _translate = QtCore.QCoreApplication.translate
        DepWindow.setWindowTitle(_translate("DepWindow", "База данных отделов"))
        self.delDepButton.setText(_translate("DepWindow", "Удалить"))
        item = self.depTable.horizontalHeaderItem(0)
        item.setText(_translate("DepWindow", "Id"))
        item = self.depTable.horizontalHeaderItem(1)
        item.setText(_translate("DepWindow", "Название отдела"))
        self.addDepButton.setText(_translate("DepWindow", "Добавить отдел"))
        self.exitDepButton.setText(_translate("DepWindow", "Выход"))

