from PySide.QtGui import *
from PySide.QtCore import *
from Ui_MainWindow import Ui_MainWindow
from PortScanWindow import PortScanWindow
from LaunchServer import LaunchServer
from NetworkScanDisplay import NetworkScanDisplay
from GetHostNameWindow import GetHostNameWindow
import myFuns


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # set up ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('Network Analyzer')

        # connect signals
        self.ui.portScan.clicked.connect(self._onPortScanClicked)
        self.ui.launchServer.clicked.connect(self._onLaunchServerClicked)
        self.ui.networkScan.clicked.connect(self._onNetworkScanClicked)
        self.ui.getHostNameButton.clicked.connect(self._onGetHostNameClicked)
        self.ui.quitButton.clicked.connect(self._onQuitClicked)

    def _onPortScanClicked(self):
        portScanWindow = PortScanWindow(self)
        portScanWindow.show()

    def _onLaunchServerClicked(self):
        launchWindow = LaunchServer(self)
        launchWindow.show()

    def _onNetworkScanClicked(self):
        networkScanWindow = NetworkScanDisplay(self)
        networkScanWindow.show()
        networkScanWindow.scan()

    def _onGetHostNameClicked(self):
        getHostNameWindow = GetHostNameWindow(self)
        getHostNameWindow.show()

    def _onQuitClicked(self):
        self.close()