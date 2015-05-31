from AppConfig import *
import getopt

def printUsage(name):
    print "Usage:", name, "(-d <device_num> | -f <filename>) [--no-networking] [--headless] [--debug]"

class CmdLineInterface:
    def __init__(self,  _argv):
        self.config = AppConfig()

        try:
            opts, args = getopt.getopt(_argv, "d:f:", ["device=", "file=", "no-networking", "headless", "debug"])
        except getopt.GetoptError:
            printUsage(_argv[0])
            sys.exit(1)

        for opt, arg in opts:
            if opt in ("-d", "--device"):
                if config.getIsFile:
                    printUsage(_argv[0])
                    sys.exit(1)
                config.deviceID = int(arg)
                config.isDevice = True
            elif opt in ("-f", "--file"):
                if config.getIsDevice:
                    printUsage(_argv[0])
                    sys.exit(1)
                config.fileName = arg
                config.isFile = True
            elif opt == "--headless":
                config.isHeadless = 1 
            elif opt == "--no-networking":
                config.isNetworking = 0
            elif opt == "--debug":
                config.isDebug = 1

        if (not config.isDevice) and (not config.isFile):
            printUsage(_argv[0])
            sys.exit(1)

        if(isDebug):
            if(isHeadless):
                print "Headless mode\n";

            if(not isNetworking):
                print "No networking mode\n";

            if(config.isDevice):
                print "Device mode: using /dev/video", config.deviceID
                          

            if(config.isFile):
                print "File mode: using", config.fileName
                          


