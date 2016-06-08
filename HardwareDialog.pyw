#coding=utf-8

import sys
import os
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3

from ui_hardwaremanager import Ui_HardwareManager

class HardwareDialog(QDialog):

    def __init__(self):

        QDialog.__init__(self)

        self.ui = Ui_HardwareManager()
        self.ui.setupUi(self)

        self.setWindowTitle("HardwareManager")
        self.setFixedHeight(self.height())
        self.setFixedWidth(self.width())
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint);

        # http://stackoverflow.com/questions/10730131/create-dynamic-button-in-pyqt
        # Error: TypeError: connect() slot argument should be a callable or a signal, not 'NoneType' #
        # Note the lambda will avoid the evaluation of the function call, so it'll call
        # self.commander(command) only when clicked
        # self.ui.insert.clicked.connect(lambda: self.insertData())
        self.ui.insert.clicked.connect(self.insertData)
        self.ui.query.clicked.connect(self.queryData)
        self.ui.clean.clicked.connect(self.cleanData)
        self.ui.resource.clicked.connect(self.getResourcePath)

        # self.cpFiles = QStringList()


    def insertData(self):

        # 这里必须这么处理一下才能将serial插入sqlite3数据，否则总是会报如下错误：
        #   sqlite3.InterfaceError: Error binding parameter 0 - probably unsupported type.
        # 这里的原因是直接空过Qt控件获取的字符串是Qstring，而这里需要的字符串类型是Python字符串，
        # 所以需要这么处理一下
        serial = ("%s" % (self.ui.serial.text().toUtf8())).strip()
        dateDir = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

        # To prevent the string length is less than 0
        if ( len(serial) > 0 ) :

            hmConnect = sqlite3.connect("./HardwareManager.db")
            cursor = hmConnect.cursor()

            cursor.execute('CREATE TABLE if not exists HardwareManager (id INTEGER PRIMARY KEY, serial VARCHAR(40), path VARCHAR(100))')

            # check serial NO. was only one
            cursor.execute('SELECT id, path from HardwareManager where serial = ?', [serial])
            if ( cursor.fetchone() != None ) :
                QMessageBox.about(self, "ERROR","Please check the serial number is the only one")
                hmConnect.close()
                return

            # insert data
            argument=(serial, dateDir)
            cursor.execute('INSERT INTO HardwareManager (id, serial, path) VALUES(NULL, ?, ?)', argument)
            hmConnect.commit()

            # save readme data
            currentFilePath = "managerFile/%s" % dateDir
            os.makedirs(currentFilePath)
            readme = open( "%s/readme.txt" % currentFilePath, "w" )
            readme.write(self.ui.readme.toPlainText().toUtf8())
            readme.flush()
            readme.close()

            self.ui.id.setText( "%s" % cursor.lastrowid )
            self.ui.path.setText("%s/readme.txt" % currentFilePath)

            hmConnect.close()

            cpFiles = ("%s" % self.ui.resourcePath.text().toUtf8()).strip().split(';')
            # print(cpFiles)
            for cpFile in cpFiles :
                # print cpFile
                if ( cpFile.__len__() > 0 ):
                    QFile.copy(cpFile, QString(currentFilePath).append("/").append(QFileInfo(cpFile).baseName()).append(".").append(QFileInfo(cpFile).completeSuffix()))

            # mesage for costomer
            QMessageBox.about(self, "Mesg","Insert OK.")


    def queryData(self):

        serial = ("%s" % (self.ui.serial.text())).strip()

        if ( len(serial) > 0 ) :

            hmConnect = sqlite3.connect("./HardwareManager.db")
            cursor = hmConnect.cursor()

            # create data if HardwareManager table don't exists
            cursor.execute('CREATE TABLE if not exists HardwareManager (id INTEGER PRIMARY KEY, serial VARCHAR(40), path VARCHAR(100))')

            # check data
            cursor.execute('SELECT id, path from HardwareManager where serial = ?', [serial])
            row = cursor.fetchone()
            if ( row == None ) :
                QMessageBox.about(self, "ERROR","Please check your serial number")
                hmConnect.close()
                return

            self.ui.id.setText( "%s" % row[0] )
            self.ui.path.setText( "managerFile/%s/readme.txt" % row[1] )

            # maybe this file has lost
            if ( os.path.exists("managerFile/%s/readme.txt" % row[1]) == True) :
                readme = open( "managerFile/%s/readme.txt" % row[1] )
                self.ui.readme.setPlainText(QString.fromUtf8(readme.read()))
                readme.close()
            else :
                QMessageBox.about(self, "Mesg","can't find the readme.txt file")

            hmConnect.close()


    def cleanData(self):

        '''
        clean EditLine widget data
        '''

        self.ui.id.setText("")
        self.ui.serial.setText("")
        self.ui.path.setText("")
        self.ui.readme.setPlainText("")
        self.ui.resourcePath.setText("")

    def getResourcePath(self) :

        '''
        get the copy file paths
        '''

        paths = QFileDialog.getOpenFileNames( self, "Select Files", ".", "*" )
        for path in paths:
            # self.cpFiles.append(path)
            self.ui.resourcePath.setText(QString(path).append(";").append(self.ui.resourcePath.text()))
