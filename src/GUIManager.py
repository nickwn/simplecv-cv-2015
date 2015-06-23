from SimpleCV import Image, Display
import time

class GUIManager:

  def init(self):
    self.dis = Display(title='FRC Team 3341 Targeting')
    
  def setImage(self, image):
    self.img = image
    
  def setImageText(self, imageText):
    self.img.drawtext(imagetext, self.img.height/2, self.img.width/2)
    
  def show(self, isFile):
    self.img.save(self.dis)
    
    if isFile:
      while not self.dis.mouseLeft:
        time.sleep(0) #I had to put something here or else the compiler would think there were "indentation errors" below
        
    else:
      while not self.dis.mouseRight:
        time.sleep(0)
