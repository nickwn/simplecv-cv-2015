from L import *

class LDetector:
    def elLoad(self, img):
        self.img = img

    def elSplit(self):
        self.hsv = self.img.toHSV()

    def elThresh(self):
        self.thresh = self.hsv.hueDistance((249, 249, 249), 5, 5).invert().morphOpen().binarize(10).morphOpen()

    def elContour(self):
        self.blobs = self.thresh.findBlobs()

    def elFilter(self):
        self.pLs = [] #possible Ls
        self.Ls = []
        k = 0
        if self.blobs:
            for blob in self.blobs:
                self.pLs.append(L(blob))

                if (abs(self.LDistance(k)) < 1.1 and abs(self.LDistance(k)) > .7 and blob.area() > 200 and self.pLs[k].hasGoodAngle()):  #the one big filtering statement
                    self.Ls.append(self.pLs[k])

                k=k+1

    def largest2(self):
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
        dist = self.blobs[i].area() / self.pLs[i].getArea()
        return dist

    def getImage(self):
        return self.thresh
