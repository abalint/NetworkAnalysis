# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_PortScanDisplay.ui'
#
# Created: Wed Dec 11 18:31:44 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_PortScanDisplay(object):
    def setupUi(self, PortScanDisplay):
        PortScanDisplay.setObjectName("PortScanDisplay")
        PortScanDisplay.resize(452, 233)
        self.centralwidget = QtGui.QWidget(PortScanDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.consolTextEdit = QtGui.QTextEdit(self.centralwidget)
        self.consolTextEdit.setObjectName("consolTextEdit")
        self.gridLayout.addWidget(self.consolTextEdit, 0, 1, 1, 1)
        PortScanDisplay.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PortScanDisplay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 452, 21))
        self.menubar.setObjectName("menubar")
        PortScanDisplay.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PortScanDisplay)
        self.statusbar.setObjectName("statusbar")
        PortScanDisplay.setStatusBar(self.statusbar)

        self.retranslateUi(PortScanDisplay)
        QtCore.QMetaObject.connectSlotsByName(PortScanDisplay)

    def retranslateUi(self, PortScanDisplay):
        PortScanDisplay.setWindowTitle(QtGui.QApplication.translate("PortScanDisplay", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.consolTextEdit.setHtml(QtGui.QApplication.translate("PortScanDisplay", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Scanning, please wait.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

