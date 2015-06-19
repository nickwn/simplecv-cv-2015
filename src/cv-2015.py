#from SimpleCV import *
import sys
from CmdLineInterface import *
from NetworkController import *

################################################################################
################## Main ########################################################
################################################################################

interface = CmdLineInterface(sys.argv)
config = interface.config

networkController = NetworkController()

#if config.isDevice:
#    camera = Camera(camera_index=config.deviceID)

if config.isNetworking:
    networkController.startServer()

while True:

    if(config.isNetworking):
        print "isNetworking"
        networkController.waitForPing()


    if(config.isFile): # Only run once for file mode
        break
