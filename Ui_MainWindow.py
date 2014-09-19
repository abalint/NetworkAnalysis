# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_MainWindow.ui'
#
# Created: Wed Dec 11 18:31:43 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(249, 198)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.networkScan = QtGui.QPushButton(self.centralwidget)
        self.networkScan.setObjectName("networkScan")
        self.gridLayout.addWidget(self.networkScan, 3, 0, 1, 1)
        self.portScan = QtGui.QPushButton(self.centralwidget)
        self.portScan.setObjectName("portScan")
        self.gridLayout.addWidget(self.portScan, 2, 0, 1, 1)
        self.launchServer = QtGui.QPushButton(self.centralwidget)
        self.launchServer.setObjectName("launchServer")
        self.gridLayout.addWidget(self.launchServer, 1, 0, 1, 1)
        self.getHostNameButton = QtGui.QPushButton(self.centralwidget)
        self.getHostNameButton.setObjectName("getHostNameButton")
        self.gridLayout.addWidget(self.getHostNameButton, 4, 0, 1, 1)
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setObjectName("quitButton")
        self.gridLayout.addWidget(self.quitButton, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 249, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.networkScan.setText(QtGui.QApplication.translate("MainWindow", "Network Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.portScan.setText(QtGui.QApplication.translate("MainWindow", "Port Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.launchServer.setText(QtGui.QApplication.translate("MainWindow", "Launch Server", None, QtGui.QApplication.UnicodeUTF8))
        self.getHostNameButton.setText(QtGui.QApplication.translate("MainWindow", "Get Host Name", None, QtGui.QApplication.UnicodeUTF8))
        self.quitButton.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))

