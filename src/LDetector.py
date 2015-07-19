from L import *

class LDetector:
    def elLoad(self, img):
        self.img = img

    def elSplit(self):
        self.hsv = self.img.toHSV()

    def elThresh(self):
        self.thresh = self.hsv.hueDistance((249, 249, 249), 5, 5).invert().morphOpen().binarize(10).morphOpen()
        # hueDistance converts the image into a grayscale where black is closest to the specified color, a white is furthest
        # invert turns white into black, and black into white. simplecv won't detect black blobs. 
        # morphOpen lessens noise in the image. First dilates, then erodes
        # binarize converts the image to black and white

    def elContour(self):
        self.blobs = self.thresh.findBlobs(minsize=500)

    def elFilter(self):
        # computes the theoretical L area (if the blob was an L, it would have this area) based off the blobs bounding rectangle and finds lots of useful variables along the way
        #It compares the blob area to the theoretical L area and if it's close enough, they are considered Ls.
        self.pLs = [] #possible Ls
        self.Ls = []
        k = 0
        if self.blobs:
            for blob in self.blobs:
                self.pLs.append(L(blob))

                if (abs(self.LDistance(k)) < 1.05 and abs(self.LDistance(k)) > .95 and blob.area() > 500 and self.pLs[k].hasGoodAngle()):  #the one big filtering statement
                    self.Ls.append(self.pLs[k])

                k=k+1

    def largest2(self):
        #finds the largest 2
        r = 0
        l = 0
        leftLs = []
        rightLs = []
        self.nLs = []
        self.largestPair = []
        for L in self.Ls:
            if L.getOrientation == 'left':
                leftLs.append(L)
                l=l+1
            else:
                rightLs.append(L)
                r=r+1

        leftLs = sorted(leftLs, key=self.getKey)
        rightLs = sorted(rightLs, key=self.getKey)
        if leftLs and rightLs:
            self.Ls = (leftLs[0], rightLs[0])

    def getKey(self, l):
        return l.getArea()

    def LDistance(self, i):
        # finds how different the blob is from an L
        dist = self.blobs[i].area() / self.pLs[i].getArea()
        return dist

    def getImage(self):
        return self.thresh
