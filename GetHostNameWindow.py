from PySide.QtCore import *
from PySide.QtGui import *
from Ui_GetHostNameWindow import Ui_GetHostNameWindow
from myFuns import hostName



class GetHostNameWindow(QMainWindow):

    def __init__(self, parent=None):
        super(GetHostNameWindow, self).__init__(parent)

        # set up ui
        self.ui = Ui_GetHostNameWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Get Host Name')

        # signals
        self.ui.getHostNameButton.clicked.connect(self._onGetHostNameClicked)

    def _onGetHostNameClicked(self):
        ip = self.ui.ipInputLineEdit.text()

        hostN = hostName()
        host = hostN.getHostName(ip)

        self.ui.putHostNameLabel.setText(str(host))
