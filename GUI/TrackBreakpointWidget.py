# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrackBreakpointWidget.ui'
#
# Created: Fri Dec 16 02:40:23 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(549, 437)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Stop = QtWidgets.QPushButton(Form)
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.horizontalLayout.addWidget(self.pushButton_Stop)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox_ValueType = QtWidgets.QComboBox(Form)
        self.comboBox_ValueType.setToolTip("")
        self.comboBox_ValueType.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_ValueType.setObjectName("comboBox_ValueType")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.comboBox_ValueType.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_ValueType)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.tableWidget_TrackInfo = QtWidgets.QTableWidget(Form)
        self.tableWidget_TrackInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_TrackInfo.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_TrackInfo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_TrackInfo.setObjectName("tableWidget_TrackInfo")
        self.tableWidget_TrackInfo.setColumnCount(4)
        self.tableWidget_TrackInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TrackInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TrackInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TrackInfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_TrackInfo.setHorizontalHeaderItem(3, item)
        self.tableWidget_TrackInfo.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_TrackInfo.verticalHeader().setVisible(False)
        self.tableWidget_TrackInfo.verticalHeader().setDefaultSectionSize(16)
        self.tableWidget_TrackInfo.verticalHeader().setMinimumSectionSize(16)
        self.gridLayout.addWidget(self.tableWidget_TrackInfo, 0, 0, 1, 1)
        self.label_Info = QtWidgets.QLabel(Form)
        self.label_Info.setText("")
        self.label_Info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Info.setObjectName("label_Info")
        self.gridLayout.addWidget(self.label_Info, 1, 0, 1, 1)
        self.label_AdditionalInfo = QtWidgets.QLabel(Form)
        self.label_AdditionalInfo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_AdditionalInfo.setObjectName("label_AdditionalInfo")
        self.gridLayout.addWidget(self.label_AdditionalInfo, 2, 0, 1, 1)

        self.retranslateUi(Form)
        self.comboBox_ValueType.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_Stop.setText(_translate("Form", "Stop"))
        self.comboBox_ValueType.setItemText(0, _translate("Form", "Byte"))
        self.comboBox_ValueType.setItemText(1, _translate("Form", "2 Bytes"))
        self.comboBox_ValueType.setItemText(2, _translate("Form", "4 Bytes"))
        self.comboBox_ValueType.setItemText(3, _translate("Form", "8 Bytes"))
        self.comboBox_ValueType.setItemText(4, _translate("Form", "Float"))
        self.comboBox_ValueType.setItemText(5, _translate("Form", "Double"))
        self.comboBox_ValueType.setItemText(6, _translate("Form", "String"))
        self.comboBox_ValueType.setItemText(7, _translate("Form", "Array of bytes"))
        item = self.tableWidget_TrackInfo.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Count"))
        item = self.tableWidget_TrackInfo.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Address"))
        item = self.tableWidget_TrackInfo.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Value"))
        item = self.tableWidget_TrackInfo.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Source"))
        self.label_AdditionalInfo.setText(_translate("Form", "Try changing combobox index if the \'Value\' part of table still isn\'t updated"))

