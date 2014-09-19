#!/usr/bin/env python
import socket
import subprocess
import sys
import os
import time
import os
from datetime import datetime
import socketserver


#from ipaddr import IPv4Network




class portScan():
    def scan(self,min,max):

        remoteServer = "localhost"
        remoteServerIP = socket.gethostbyname(remoteServer)


        print("wait, scanning host.", remoteServerIP)
        print("-" * 50)
        t1 = datetime.now()


        try:
            stringList = []
            for port in range(min, max): #0 - 1025
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteServerIP, port))
                if result == 0:
                    stringList.append("Port {}: \t Open".format(port))
                    print("Port {}: \t Open".format(port))
                sock.close()

        except KeyboardInterrupt:
            print("You pressed Ctrl+C")
            sys.exit()

        except socket.gaierror:
            print('Hostname could not be resolved. Exiting')
            sys.exit()

        except socket.error:
            print("Couldn't connect to server")
            sys.exit()

        # Checking the time again
        t2 = datetime.now()

        # Calculates the difference of time, to see how long it took to run the script
        total = t2 - t1

        # Printing the information to screen
        print('Scanning Completed in: ', total)
        return stringList

class ipScan():
    def ping(self, addr):
        cmd = "ping %s -n 1 -w 1" % addr
        print("Pinging " + str(addr))
        try:
            return subprocess.check_call(cmd, shell=True)
        except subprocess.CalledProcessError:
            return 1

    def scan(self, addr):
        address = self.truncate(addr)
        lastDig = 0
        connectedList = []
        while lastDig < 51: #
            fullAddr = address + str(lastDig)
            if(ipScan.ping(fullAddr) != 1):
                connectedList.append(fullAddr)
            lastDig += 1
        for i in connectedList:
            print(i)
        return connectedList

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




class ipGetter():
    def network(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        ip = s.getsockname()[0]
        s.close()
        print(ip)
        return ip

class portManagment():
    def openPort(self, port):
        print("in openPort")
        print("port is", port)
        sock = socket.socket()
        sock.bind(("127.0.0.1", port))
        sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 30000, 30000))
        sock.listen(5)


    def closePort(self):
        print("closing port")
        s = socket.socket()
        s.connect(("localhost", 554))
        s.shutdown()
        s.close()

    def getHostname(self):
        sock = socket.socket()
        sock.get

class launchApp():
    def launch(self, path):
        os.startfile(path)



class hostName():
    def getHostName(self, ip):
        try:
            return socket.gethostbyaddr(ip)
        except:
            return "no hostname found"