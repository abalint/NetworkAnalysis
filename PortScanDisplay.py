
from PySide.QtCore import *
from PySide.QtGui import *
from Ui_PortScanDisplay import Ui_PortScanDisplay
from datetime import datetime
import socket
import sys
import PySide.QtGui


class PortScanDisplay(QMainWindow):

    def __init__(self,min, max, parent=None):
        super(PortScanDisplay, self).__init__(parent)

        # set up ui
        self.ui = Ui_PortScanDisplay()
        self.ui.setupUi(self)

        self.ui.consolTextEdit.setReadOnly(1)


    def scan(self,min,max):
        remoteServer = "localhost"
        remoteServerIP = socket.gethostbyname(remoteServer)

        line = ("scanning host.")
        self.ui.consolTextEdit.append(line)
        self.ui.consolTextEdit.append(remoteServer)
        print("host."+ remoteServerIP)
        QCoreApplication.processEvents()
        print("-" * 50)
        self.ui.consolTextEdit.append("-" * 50)
        QCoreApplication.processEvents()
        t1 = datetime.now()


        try:
            stringList = []
            for port in range(min, max): #0 - 65535
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                print("scanning Port {}".format(port))
                self.ui.consolTextEdit.append("scanning Port {}".format(port))
                QCoreApplication.processEvents()
                if result == 0:
                    stringList.append("Port {}: Open".format(port))
                    print("Port {}: \t Open".format(port))
                    self.ui.consolTextEdit.append("Port {}: \t Open".format(port))
                    QCoreApplication.processEvents()
                sock.close()

        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            self.ui.consolTextEdit.append("You pressed Ctrl+C")
            QCoreApplication.processEvents()
            sys.exit()

        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            self.ui.consolTextEdit.append('Hostname could not be resolved. Exiting')
            QCoreApplication.processEvents()
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            self.ui.consolTextEdit.append("Couldn't connect to server")
            QCoreApplication.processEvents()
            sys.exit()

        # Checking the time again
        t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total = t2 - t1

        # Printing the information to screen
        if(len(stringList) == 0):
            print("no ports open")
            self.ui.consolTextEdit.append("no ports open")
            QCoreApplication.processEvents()
        print('Scanning Completed in: ', total)
        self.ui.consolTextEdit.append('Scanning Completed in: ')
        self.ui.consolTextEdit.append(str(total))
        QCoreApplication.processEvents()
        print(stringList)
        for ports in stringList:
            self.ui.consolTextEdit.append(ports)
            QCoreApplication.processEvents()
