from SimpleCV import Color

class L:

    def __init__(self, blob):
        self.blob = blob
        (tl, tr, bl, br) = self.blob.minRect()
        self.blob.drawMinRect()

        # modified variables to form a square
        if self.height() > self.width():
            mbr = (bl[0]+self.height(), br[1])
            mbl = bl
            mtr = (tl[0]+self.height(), tr[1])
            mtl = tl
        else:
            mbr = br
            mbl = bl
            mtr = (tr[0], br[1]+self.width())
            mtl = (tl[0], bl[1]+self.width())

        self.outsideCorner = mbl
        self.insideCorner = (mtl[0] + (abs(mtl[0]-mtr[0])*.4), mbr[1] + (abs(mtr[1]-mbr[1]) * .4))
        self.outsideUpper = mtl
        self.insideUpper = (mtl[0] + (abs(mtl[0]-mtr[0])*.4), mtl[1])
        self.outsideSide = mbr
        self.insideSide = (mbr[0], mbr[1] + (abs(mtr[1]-mbr[1]) * .4))

        # list of variables for the L on the left side
        self.lOutsideCorner = mbr
        self.lInsideCorner = (mtr[0] - (abs(mtr[0]-mtl[0])*.4), mbl[1] + (abs(mtl[1]-mbl[1]) * .4))
        self.lOutsideUpper = mtr
        self.lInsideUpper = (mtr[0] - (abs(mtr[0]-mtl[0])*.4), mtr[1])
        self.lOutsideSide = mbl
        self.lInsideSide = (mbl[0], mbl[1] + (abs(mtl[1]-mbl[1]) * .4))

        self.area = self.findArea()  # too much math in one function

    def findArea(self):
        bigRectHeight = abs(self.outsideUpper[1]-self.outsideCorner[1])
        bigRectWidth = abs(self.outsideCorner[0]-self.outsideSide[0])
        bigRectArea = bigRectHeight * bigRectWidth

        smallRectHeight =abs(self.insideCorner[1]-self.insideUpper[1])
        smallRectWidth =abs(self.insideCorner[0]-self.insideSide[0])
        smallRectArea = smallRectHeight * smallRectWidth

        return bigRectArea - smallRectArea

    def hasGoodAngle(self):
        if (self.blob.angle() < 10 and self.blob.angle > -10):
            return True
        elif (self.blob.angle() < 100 and self.blob.angle > 80):
            return True
        else:
            return False

    def getOrientation(self):
        if self.blobCenter()[0] > self.rectCenter()[0]:
            self.orientation = 'left'
        else:
            self.orientation = 'right'
        return self.orientation

    def getArea(self):
        return self.area

    def height(self):
        return self.blob.minRectHeight()

    def width(self):
        return self.blob.minRectHeight()

    def rectCenter(self):
        return (self.blob.minRectX(), self.blob.minRectY())

    def blobCenter(self):
        return self.blob.centroid()

    def distanceFrom(self, coords):
        return self.blob.distanceFrom(coords)

    def getPoints(self):
        return self.blob.contour()

    def draw(self,layer=None,color=Color.RED,width=3,alpha=128):
        if( layer is None ):
            layer = self.blob.image.dl()
        if self.getOrientation() == 'right':
            layer.line(self.outsideCorner,self.outsideUpper,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.outsideCorner,self.outsideSide,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.insideCorner,self.insideUpper,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.insideCorner,self.insideSide,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.outsideUpper,self.insideUpper,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.outsideSide,self.insideSide,color,width=width,alpha=alpha,antialias = False)

        else:
            layer.line(self.lOutsideCorner,self.lOutsideUpper,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.lOutsideCorner,self.lOutsideSide,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.lInsideCorner,self.lInsideUpper,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.lInsideCorner,self.lInsideSide,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.lOutsideUpper,self.lInsideUpper,color,width=width,alpha=alpha,antialias = False)
            layer.line(self.lOutsideSide,self.lInsideSide,color,width=width,alpha=alpha,antialias = False)
