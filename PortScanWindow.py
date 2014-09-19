from PySide.QtCore import *
from PySide.QtGui import *
from Ui_PortScanWindow import Ui_PortScanWindow
from PortScanDisplay import PortScanDisplay
from myFuns import launchApp


class PortScanWindow(QMainWindow):

    def __init__(self, parent=None):
        super(PortScanWindow, self).__init__(parent)

        # set up ui
        self.ui = Ui_PortScanWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Port Scanner')
        self.ui.minSpinBox.setMinimum(0)
        self.ui.minSpinBox.setMaximum(65535)

        self.ui.maxSpinBox.setMinimum(0)
        self.ui.maxSpinBox.setMaximum(65535)
        self.ui.maxSpinBox.setValue(65535)

        # signals
        self.ui.runPortScanButton.clicked.connect(self._onRunPortScanButtonClicked)
        self.ui.cancelButton.clicked.connect(self._onCancelPortScan)

    def _onRunPortScanButtonClicked(self):
        min = self.ui.minSpinBox.value()
        max = self.ui.maxSpinBox.value()
        print(min, max)


        portScanDisplay = PortScanDisplay(min, max, self)
        portScanDisplay.show()
        portScanDisplay.update()
        portScanDisplay.scan(min,max)



    def _onCancelPortScan(self):
        self.close()