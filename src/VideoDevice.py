from SimpleCV import Image, Camera
import sys

class VideoDevice:

  def __init__(self):
    self.isFinished = 0
    self.isInitialized = False
  
  def startCapture(self, deviceID):
    self.initCamera(deviceID)
    self.isInitialized = True
    self.devID = deviceID
    
  def initCamera(self, deviceID):
    try:
      self.cam = Camera(camera_index=deviceID)
      testimg = self.cam.getImage()
      
    except Exception, e:
      print e
      print('A bad ID may have been inputted')
      sys.exit(1)
      
  def getImage(self):
    return self.cam.getImage()
    
  def __del__(self):
    self.isFinished = 1
