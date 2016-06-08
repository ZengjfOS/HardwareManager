# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\HardWareManager\hardwaremanager.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_HardwareManager(object):
    def setupUi(self, HardwareManager):
        HardwareManager.setObjectName(_fromUtf8("HardwareManager"))
        HardwareManager.resize(465, 326)
        self.verticalLayout_2 = QtGui.QVBoxLayout(HardwareManager)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.frame = QtGui.QVBoxLayout()
        self.frame.setObjectName(_fromUtf8("frame"))
        self.serialIDPath = QtGui.QGridLayout()
        self.serialIDPath.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.serialIDPath.setContentsMargins(10, -1, -1, -1)
        self.serialIDPath.setHorizontalSpacing(5)
        self.serialIDPath.setObjectName(_fromUtf8("serialIDPath"))
        self.label_path = QtGui.QLabel(HardwareManager)
        self.label_path.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_path.setObjectName(_fromUtf8("label_path"))
        self.serialIDPath.addWidget(self.label_path, 3, 0, 1, 1)
        self.label_id = QtGui.QLabel(HardwareManager)
        self.label_id.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_id.setObjectName(_fromUtf8("label_id"))
        self.serialIDPath.addWidget(self.label_id, 2, 0, 1, 1)
        self.label_serial = QtGui.QLabel(HardwareManager)
        self.label_serial.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_serial.setObjectName(_fromUtf8("label_serial"))
        self.serialIDPath.addWidget(self.label_serial, 1, 0, 1, 1)
        self.serial = QtGui.QLineEdit(HardwareManager)
        self.serial.setObjectName(_fromUtf8("serial"))
        self.serialIDPath.addWidget(self.serial, 1, 1, 1, 1)
        self.id = QtGui.QLineEdit(HardwareManager)
        self.id.setReadOnly(True)
        self.id.setObjectName(_fromUtf8("id"))
        self.serialIDPath.addWidget(self.id, 2, 1, 1, 1)
        self.label_resource = QtGui.QLabel(HardwareManager)
        self.label_resource.setFrameShadow(QtGui.QFrame.Plain)
        self.label_resource.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_resource.setObjectName(_fromUtf8("label_resource"))
        self.serialIDPath.addWidget(self.label_resource, 4, 0, 1, 1)
        self.getResourcePath = QtGui.QHBoxLayout()
        self.getResourcePath.setObjectName(_fromUtf8("getResourcePath"))
        self.resourcePath = QtGui.QLineEdit(HardwareManager)
        self.resourcePath.setObjectName(_fromUtf8("resourcePath"))
        self.getResourcePath.addWidget(self.resourcePath)
        self.resource = QtGui.QPushButton(HardwareManager)
        self.resource.setMinimumSize(QtCore.QSize(30, 0))
        self.resource.setMaximumSize(QtCore.QSize(30, 16777215))
        self.resource.setObjectName(_fromUtf8("resource"))
        self.getResourcePath.addWidget(self.resource)
        self.serialIDPath.addLayout(self.getResourcePath, 4, 1, 1, 1)
        self.path = QtGui.QLineEdit(HardwareManager)
        self.path.setReadOnly(True)
        self.path.setObjectName(_fromUtf8("path"))
        self.serialIDPath.addWidget(self.path, 3, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.clean = QtGui.QPushButton(HardwareManager)
        self.clean.setMinimumSize(QtCore.QSize(0, 80))
        self.clean.setObjectName(_fromUtf8("clean"))
        self.verticalLayout.addWidget(self.clean)
        self.serialIDPath.addLayout(self.verticalLayout, 1, 2, 4, 1)
        self.frame.addLayout(self.serialIDPath)
        self.insertQueryButton = QtGui.QHBoxLayout()
        self.insertQueryButton.setObjectName(_fromUtf8("insertQueryButton"))
        self.insert = QtGui.QPushButton(HardwareManager)
        self.insert.setObjectName(_fromUtf8("insert"))
        self.insertQueryButton.addWidget(self.insert)
        self.query = QtGui.QPushButton(HardwareManager)
        self.query.setObjectName(_fromUtf8("query"))
        self.insertQueryButton.addWidget(self.query)
        self.frame.addLayout(self.insertQueryButton)
        self.readme = QtGui.QTextEdit(HardwareManager)
        self.readme.setObjectName(_fromUtf8("readme"))
        self.frame.addWidget(self.readme)
        self.verticalLayout_2.addLayout(self.frame)

        self.retranslateUi(HardwareManager)
        QtCore.QMetaObject.connectSlotsByName(HardwareManager)
        HardwareManager.setTabOrder(self.serial, self.resourcePath)
        HardwareManager.setTabOrder(self.resourcePath, self.insert)
        HardwareManager.setTabOrder(self.insert, self.query)
        HardwareManager.setTabOrder(self.query, self.readme)
        HardwareManager.setTabOrder(self.readme, self.resource)
        HardwareManager.setTabOrder(self.resource, self.clean)
        HardwareManager.setTabOrder(self.clean, self.id)
        HardwareManager.setTabOrder(self.id, self.path)

    def retranslateUi(self, HardwareManager):
        HardwareManager.setWindowTitle(_translate("HardwareManager", "HardwareManager", None))
        self.label_path.setText(_translate("HardwareManager", "Path:", None))
        self.label_id.setText(_translate("HardwareManager", "ID:", None))
        self.label_serial.setText(_translate("HardwareManager", "Serial NO.:", None))
        self.label_resource.setText(_translate("HardwareManager", "Resource:", None))
        self.resource.setText(_translate("HardwareManager", "...", None))
        self.clean.setText(_translate("HardwareManager", "Clean All", None))
        self.insert.setText(_translate("HardwareManager", "Insert", None))
        self.query.setText(_translate("HardwareManager", "Query", None))

