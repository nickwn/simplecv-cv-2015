#from SimpleCV import *
import sys
from CmdLineInterface import *
from NetworkController import *

################################################################################
################## Main ########################################################
################################################################################

interface = CmdLineInterface(sys.argv)
config = interface.getConfig()

networkController = NetworkController()

if config.isNetworking:
    networkController.startServer()

while True:

    if(config.isNetworking):
        networkController.waitForPing()


    if(config.isFile): # Only run once for file mode
        break
