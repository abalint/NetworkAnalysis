# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_GetHostNameWindow.ui'
#
# Created: Wed Dec 11 18:31:41 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_GetHostNameWindow(object):
    def setupUi(self, GetHostNameWindow):
        GetHostNameWindow.setObjectName("GetHostNameWindow")
        GetHostNameWindow.resize(417, 160)
        self.centralwidget = QtGui.QWidget(GetHostNameWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.getHostNameButton = QtGui.QPushButton(self.centralwidget)
        self.getHostNameButton.setObjectName("getHostNameButton")
        self.gridLayout.addWidget(self.getHostNameButton, 3, 0, 1, 1)
        self.ipInputLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.ipInputLineEdit.setObjectName("ipInputLineEdit")
        self.gridLayout.addWidget(self.ipInputLineEdit, 1, 0, 1, 1)
        self.putHostNameLabel = QtGui.QLabel(self.centralwidget)
        self.putHostNameLabel.setText("")
        self.putHostNameLabel.setObjectName("putHostNameLabel")
        self.gridLayout.addWidget(self.putHostNameLabel, 2, 0, 1, 1)
        GetHostNameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(GetHostNameWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 417, 21))
        self.menubar.setObjectName("menubar")
        GetHostNameWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(GetHostNameWindow)
        self.statusbar.setObjectName("statusbar")
        GetHostNameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GetHostNameWindow)
        QtCore.QMetaObject.connectSlotsByName(GetHostNameWindow)

    def retranslateUi(self, GetHostNameWindow):
        GetHostNameWindow.setWindowTitle(QtGui.QApplication.translate("GetHostNameWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GetHostNameWindow", "Enter IP address", None, QtGui.QApplication.UnicodeUTF8))
        self.getHostNameButton.setText(QtGui.QApplication.translate("GetHostNameWindow", "Get Host Name", None, QtGui.QApplication.UnicodeUTF8))

