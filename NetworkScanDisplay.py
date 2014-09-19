from PySide.QtCore import *
from PySide.QtGui import *
from Ui_NetworkScanDisplay import Ui_NetworkScanDisplay
import subprocess
import myFuns


#self.ui.consolTextEdit.append("-" * 50)
#QCoreApplication.processEvents()


class NetworkScanDisplay(QMainWindow):

    def __init__(self, parent=None):
        super(NetworkScanDisplay, self).__init__(parent)

        # set up ui
        self.ui = Ui_NetworkScanDisplay()
        self.ui.setupUi(self)
        self.setWindowTitle('Network Scanner')
        self.ui.consolTextEdit.setReadOnly(1)



    def ping(self, addr):
        cmd = "ping %s -n 1 -w 1" % addr
        print("Pinging " + str(addr))
        self.ui.consolTextEdit.append("Pinging " + str(addr))
        QCoreApplication.processEvents()
        try:
            return subprocess.check_call(cmd, shell=True)
        except subprocess.CalledProcessError:
            return 1

    def scan(self, ):
        ipGetter = myFuns.ipGetter()
        addr = ipGetter.network()
        print(addr)
        address = self.truncate(str(addr))
        lastDig = 0
        connectedList = []
        while lastDig < 255: #255
            fullAddr = address + str(lastDig)
            if(self.ping(fullAddr) != 1):
                connectedList.append(fullAddr)
            lastDig += 1
        print("users online:")
        self.ui.consolTextEdit.append("users online:")
        QCoreApplication.processEvents()

        if(len(connectedList) == 0):
            print("no connections")
            self.ui.consolTextEdit.append("no connections")
            QCoreApplication.processEvents()
        for i in connectedList:
            print(i)
            self.ui.consolTextEdit.append(i)
            QCoreApplication.processEvents()



    def truncate(self,addr):
        count = 0
        dotCount = 0
        truncatedLine = ""
        for i in addr:
            if(i =='.'):
                dotCount = dotCount + 1
            if(dotCount == 3):
                return addr[0:count+1]
            count = count + 1
