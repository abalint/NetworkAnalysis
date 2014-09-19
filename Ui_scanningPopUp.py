# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_scanningPopUp.ui'
#
# Created: Wed Dec 11 18:31:45 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ScanningPopUp(object):
    def setupUi(self, ScanningPopUp):
        ScanningPopUp.setObjectName("ScanningPopUp")
        ScanningPopUp.resize(151, 118)
        self.gridLayout = QtGui.QGridLayout(ScanningPopUp)
        self.gridLayout.setObjectName("gridLayout")
        self.okButton = QtGui.QPushButton(ScanningPopUp)
        self.okButton.setObjectName("okButton")
        self.gridLayout.addWidget(self.okButton, 1, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(ScanningPopUp)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.retranslateUi(ScanningPopUp)
        QtCore.QMetaObject.connectSlotsByName(ScanningPopUp)

    def retranslateUi(self, ScanningPopUp):
        ScanningPopUp.setWindowTitle(QtGui.QApplication.translate("ScanningPopUp", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("ScanningPopUp", "ok", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("ScanningPopUp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Scanning... Please wait.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

