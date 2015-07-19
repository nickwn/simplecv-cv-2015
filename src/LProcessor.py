from L import *
import math

class LProcessor:

    secondL = None
    firstL = None
    def __init__(self):  #set initial values
        self.focalLength = 640
        self.imgWidth = 640
        self.imgHeight = 480
        self.distanceLEdgeToCenter = 0.034925
        self.horizontalLLength = 0.1778
        self.verticalLLength = 0.1778
        self.fullHorizontalLLength = 0.425458
        self.lCount = 0

    def determineL(self, ls):  #left L first, right L second
        self.firstL = ls[0]
        self.lCount=1
        if (len(ls) == 2):
            self.secondL = ls[1]
            self.lCount=2

    def getAzimuth(self):
        return self.azimuth

    def getDistance(self):
        if self.distanceFullHorizontal < self.distanceVertical:
            return self.distanceFullHorizontal
        else:
            return self.distanceVertical

    def determineCenter(self):
        if (self.lCount == 1):
            return self.determineCenter1L()
        elif (self.lCount == 2):
            return self.determineCenter2Ls()

    def determineCenter1L(self):
        self.pixelsToCenter = self.distanceLEdgeToCenter * self.firstL.width() / self.horizontalLLength
        center = []
        if (self.firstL.getOrientation() == 'right'):
            self.pixelsToCenter *= -1
        center.append(self.firstL.lOutsideCorner[0] + self.pixelsToCenter)
        center.append((self.firstL.lOutsideUpper[1] + self.firstL.lOutsideUpper[1]) / 2)
        return center

    def determineCenter2Ls(self):
        fPoints = self.firstL.getPoints()
        x1 = 0
        y1 = 0
        i=0
        for point in fPoints:
            x1 += point[0]
            y1 += point[1]

        avgX1 = x1/len(fPoints)
        avgY1 = y1/len(fPoints)

        sPoints = self.secondL.getPoints()
        x2 = 0
        y2 = 0
        for p in sPoints:
            x2 += p[0]
            y2 += p[1]

        avgX2 = x2/len(sPoints)
        avgY2 = y2/len(sPoints)
        avgX = (avgX1 + avgX2)/2
        avgY = (avgY1 + avgY2)/2
        return (avgX, avgY)

    def determineAzimuth(self):
        self.azimuth = ((self.imgWidth/2.0)-self.determineCenter()[0]) / self.focalLength
        self.azimuth *= 180.0 / math.pi

    def determineDistance(self):
        if (self.lCount == 1):
            return self.determineDistance1L()
        else:
            return self.determineDistance2Ls()

    def determineDistance1L(self):
        self.distanceFullHorizontal = self.horizontalLLength * self.focalLength / self.firstL.width()
        self.distanceVertical = self.verticalLLength * self.focalLength / self.firstL.height()

    def determineDistance2Ls(self):
        '''
         Currently the distance is calculated using the horizontal length between the side points of each L.
         Additionally, length is calculated using the shorter vertical distance of both L's.
         '''
        self.lengthFullHorizontal = math.sqrt(math.pow(self.firstL.lOutsideSide[0] - self.secondL.outsideSide[0],2) + math.pow(self.firstL.lOutsideSide[1] - self.secondL.outsideSide[1],2))
        self.distanceFullHorizontal = self.fullHorizontalLLength * self.focalLength / self.lengthFullHorizontal
        lengthVertical = (self.firstL.height() + self.secondL.height()) / 2 #fmin(firstL.getVerticalLength(), secondL.getVerticalLength());
        self.distanceVertical = self.verticalLLength * self.focalLength / lengthVertical

    def outputData(self):
        dir = ("Left Facing", "Right Facing")
        print("Final Results")
        print("================================================================")
        print("L1: /l" + "Horizontal Length [In Pixels]: " + str(self.firstL.width()) + ", Vertical Length [In Pixels]: " + str(self.firstL.height()) + ", Orientation: " + self.firstL.getOrientation())
        if (self.lCount > 1):
            print("L2:" + "Horizontal Length [In Pixels]: " + str(self.secondL.width()) + ", Vertical Length [In Pixels]: " + str(self.secondL.height()) + ", Orientation: " + self.secondL.getOrientation())
        print("Calculated Azimuth: " + str(self.azimuth))
        print("Calculated Distance (Full Horizontal) [In Meters]: " + str(self.distanceFullHorizontal))
        print("Calculated Distance (Vertical Average) [In Meters]: " + str(self.distanceVertical))
        print("Calculated Distance (Full Horizontal) [In Feet]: " + str(self.distanceFullHorizontal * 3.2808))
        print("Calculated Distance (Vertical Average) [In Feet]: " + str(self.distanceVertical * 3.2808))

