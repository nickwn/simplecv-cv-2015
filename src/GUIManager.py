from SimpleCV import Image, Display
import time

class GUIManager:

  def init(self):
    self.dis = Display(title='FRC Team 3341 Targeting')  # creates a window
    
  def setImage(self, image):
    self.img = image
    
  def setImageText(self, imageText):
    self.img.drawtext(imagetext, self.img.height/2, self.img.width/2)  
    # the height and width may need to be switched around
    # it could also be that the image is bigger than the display
    
  def setFeatures(self, blobs=None, ls=None):  #draws the features like blobs and Ls
    if self.blobs:
      for b in blobs:
        b.draw()

    if ls:
        for l in ls:
          l.draw()  # the L draw function draws the Ls upside down for some reason
    
  def show(self):  
    # I took out the isFile parameter because a video is not displayed differently than an image in simplecv
    # the thing where it waits for a key to be pressed was taken out too because it made the program crash
    self.img.save(self.dis)
    
  def disIsNotDone(self):
    # this is used to find if the window has been exited out of
    return self.dis.isNotDone()
    
