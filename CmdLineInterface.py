from AppConfig import *
import getopt

def printUsage(name):
    print "Usage:", name, "(-d <device_num> | -f <filename>) [--no-networking] [--headless] [--debug]"

class CmdLineInterface:
    def __init__(self,  _argv):
        self.config = AppConfig()

        try:
            opts, args = getopt.getopt(_argv, "d:f:", ["device=", "file="])
        except getopt.GetoptError:
            printUsage(_argv[0])
            sys.exit(1)

        for opt, arg in opts:
            if opt in ("-d", "--device"):
                if self.config.getIsFile:
                    printUsage(_argv[0])
                    sys.exit(1)
                self.config.deviceID = int(arg)
                self.config.isDevice = True
            elif opt in ("-f", "--file"):
                if self.config.getIsDevice:
                    printUsage(_argv[0])
                    sys.exit(1)
                self.config.fileName = arg
                self.config.isFile = True
            elif opt == "--headless":
                self.config.isHeadless = 1 
            elif opt == "--no-networking":
                self.config.isNetworking = 0
            elif opt == "--debug":
                self.config.isDebug = 1

        if (not self.config.isDevice) and (not self.config.isFile):
            printUsage(_argv[0])
            sys.exit(1)

        if(isDebug):
            if(isHeadless):
                print "Headless mode\n";

            if(not isNetworking):
                print "No networking mode\n";

            if(self.config.isDevice):
                print "Device mode: using /dev/video", self.config.deviceID
                          

            if(self.config.isFile):
                print "File mode: using", self.config.fileName
                          


