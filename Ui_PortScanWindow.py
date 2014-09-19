# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PortScanWindow.ui'
#
# Created: Wed Dec 11 18:31:45 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PortScanWindow(object):
    def setupUi(self, PortScanWindow):
        PortScanWindow.setObjectName("PortScanWindow")
        PortScanWindow.resize(187, 106)
        self.centralwidget = QtGui.QWidget(PortScanWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.maxSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.maxSpinBox.setObjectName("maxSpinBox")
        self.gridLayout.addWidget(self.maxSpinBox, 1, 3, 1, 1)
        self.minSpinBox = QtGui.QSpinBox(self.centralwidget)
        self.minSpinBox.setObjectName("minSpinBox")
        self.gridLayout.addWidget(self.minSpinBox, 1, 1, 1, 1)
        self.runPortScanButton = QtGui.QPushButton(self.centralwidget)
        self.runPortScanButton.setObjectName("runPortScanButton")
        self.gridLayout.addWidget(self.runPortScanButton, 2, 3, 1, 1)
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 1, 1, 1)
        PortScanWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(PortScanWindow)
        self.statusbar.setObjectName("statusbar")
        PortScanWindow.setStatusBar(self.statusbar)

        self.retranslateUi(PortScanWindow)
        QtCore.QMetaObject.connectSlotsByName(PortScanWindow)

    def retranslateUi(self, PortScanWindow):
        PortScanWindow.setWindowTitle(QtGui.QApplication.translate("PortScanWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PortScanWindow", "Min", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PortScanWindow", "Max", None, QtGui.QApplication.UnicodeUTF8))
        self.runPortScanButton.setText(QtGui.QApplication.translate("PortScanWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("PortScanWindow", "&Cancel", None, QtGui.QApplication.UnicodeUTF8))

