__author__ = 'andrew'
import myFuns

class InformationDisplay():
    def portScan(self):
        scanner = myFuns.portScan()
        scanner.scan()

    def ipScan(self):
        scanner = myFuns.ipScan()
        scanner.scan()

    def ping(addr):
        ping = myFuns.ipScan()
        ping.ping(addr)

    def ipGetter(self):
        getter = myFuns.ipGetter()
        getter.network()
