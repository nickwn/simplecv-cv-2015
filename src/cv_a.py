#partial program to test the classes

from GUIManager import *
from VideoDevice import *
from LDetector import *
#from LProcessor import *
from L import *

cam = VideoDevice()
gui = GUIManager()
detector = LDetector()
processor = LProcessor()

cam.startCapture(1)

gui.init()

while gui.disIsNotDone():
    img = cam.getImage()

    detector.elLoad(img)
    detector.elSplit()
    detector.elThresh()
    detector.elContour()
    detector.elFilter()

    foundLs = True
    if len(detector.Ls) >= 2:
        detector.largest2()
    elif len(detector.Ls) == 0:
        foundLs = False
    
    if foundLs:
        processor.determineL(detector.Ls)
        processor.determineAzimuth()
        processor.determineDistance()
        azimuth = processor.getAzimuth()
        distance = processor.getDistance()
        processor.outputData()
    
    gui.setImage(detector.getImage())
    gui.setFeatures(blobs=detector.blobs, ls=detector.Ls)
    gui.show()
