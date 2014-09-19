# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_LaunchServer.ui'
#
# Created: Wed Dec 11 18:31:42 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_LaunchServer(object):
    def setupUi(self, LaunchServer):
        LaunchServer.setObjectName("LaunchServer")
        LaunchServer.resize(461, 147)
        self.centralwidget = QtGui.QWidget(LaunchServer)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.filePathLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.filePathLineEdit.setObjectName("filePathLineEdit")
        self.gridLayout.addWidget(self.filePathLineEdit, 1, 0, 1, 2)
        self.launchButton = QtGui.QPushButton(self.centralwidget)
        self.launchButton.setObjectName("launchButton")
        self.gridLayout.addWidget(self.launchButton, 2, 0, 1, 1)
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 1, 1, 1)
        LaunchServer.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(LaunchServer)
        self.statusbar.setObjectName("statusbar")
        LaunchServer.setStatusBar(self.statusbar)

        self.retranslateUi(LaunchServer)
        QtCore.QMetaObject.connectSlotsByName(LaunchServer)

    def retranslateUi(self, LaunchServer):
        LaunchServer.setWindowTitle(QtGui.QApplication.translate("LaunchServer", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LaunchServer", "Please enter the file path", None, QtGui.QApplication.UnicodeUTF8))
        self.launchButton.setText(QtGui.QApplication.translate("LaunchServer", "Launch", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("LaunchServer", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

