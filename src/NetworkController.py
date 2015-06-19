import sys
import socket

class NetworkController:
    def __init__(self):
        self.portNumber = 3341
    
    def startServer(self):
        self.acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.acceptor.bind(('', self.portNumber))
        except socket.error as msg:
            print "Server Socket failed to initialize"
            sys.exit(2)
    
    def waitForPing(self):
        self.acceptor.listen(2)
        conn, addr = self.acceptor.accept()
