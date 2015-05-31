from AppConfig import *
import getopt
import sys

def printUsage(name):
    print "Usage:", name, "(-d <device_num> | -f <filename>) [--no-networking] [--headless] [--debug]"

class CmdLineInterface:
    def __init__(self,  _argv):
        self.name = _argv[0]
        _argv = _argv[1:]
        self.config = AppConfig()

        try:
            opts, args = getopt.getopt(_argv, "d:f:", ["device=", "file=", "no-networking", "headless", "debug"])
        except getopt.GetoptError:
            printUsage(self.name)
            sys.exit(1)

        for opt, arg in opts:

            if opt in ("-d", "--device"):
                if self.config.isFile:
                    printUsage(self.name)
                    sys.exit(1)
                self.config.deviceID = int(arg)
                self.config.isDevice = True

            elif opt in ("-f", "--file"):
                if self.config.isDevice:
                    printUsage(self.name)
                    sys.exit(1)
                self.config.fileName = arg
                self.config.isFile = True

            elif opt == "--headless":
                self.config.isHeadless = True

            elif opt == "--no-networking":
                self.config.isNetworking = 0

            elif opt == "--debug":
                self.config.isDebug = True

        # exactly device mode OR file mode must be specified
        if (not self.config.isDevice) and (not self.config.isFile):
            printUsage(self.name)
            sys.exit(1)

        if(self.config.isDebug):
            print "Debug Mode"

            if(self.config.isHeadless):
                print "Headless mode";

            if(not self.config.isNetworking):
                print "No networking mode";

            if(self.config.isDevice):
                print "Device mode: using /dev/video" + str(self.config.deviceID)
                          

            if(self.config.isFile):
                print "File mode: using", self.config.fileName

    def getConfig(self):
        return self.config

