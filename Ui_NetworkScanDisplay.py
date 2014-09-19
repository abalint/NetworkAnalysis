# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_NetworkScanDisplay.ui'
#
# Created: Wed Dec 11 18:31:43 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_NetworkScanDisplay(object):
    def setupUi(self, NetworkScanDisplay):
        NetworkScanDisplay.setObjectName("NetworkScanDisplay")
        NetworkScanDisplay.resize(453, 234)
        self.centralwidget = QtGui.QWidget(NetworkScanDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.consolTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.consolTextEdit.setObjectName("consolTextEdit")
        self.gridLayout.addWidget(self.consolTextEdit, 0, 0, 1, 1)
        NetworkScanDisplay.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(NetworkScanDisplay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
        self.menubar.setObjectName("menubar")
        NetworkScanDisplay.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(NetworkScanDisplay)
        self.statusbar.setObjectName("statusbar")
        NetworkScanDisplay.setStatusBar(self.statusbar)

        self.retranslateUi(NetworkScanDisplay)
        QtCore.QMetaObject.connectSlotsByName(NetworkScanDisplay)

    def retranslateUi(self, NetworkScanDisplay):
        NetworkScanDisplay.setWindowTitle(QtGui.QApplication.translate("NetworkScanDisplay", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

