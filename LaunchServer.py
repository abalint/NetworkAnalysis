from PySide.QtCore import *
from PySide.QtGui import *
from myFuns import launchApp
from Ui_LaunchServer import Ui_LaunchServer


class LaunchServer(QMainWindow):

    def __init__(self, parent=None):
        super(LaunchServer, self).__init__(parent)

        # set up ui
        self.ui = Ui_LaunchServer()
        self.ui.setupUi(self)

        # signals
        self.ui.launchButton.clicked.connect(self._onLaunchButtonClicked)
        self.ui.cancelButton.clicked.connect(self._onCancelPortScan)

    def _onLaunchButtonClicked(self):
        filePath = self.ui.filePathLineEdit.text()
        print(filePath)
        launchApp.launch(self, filePath)


    def _onCancelPortScan(self):
        self.close()