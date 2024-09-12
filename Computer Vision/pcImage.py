import math
class pcImage: 
    mono=[]
    gray=[]
    red=[]
    green=[]
    blue=[]
    width=0
    height=0
    convo=[]
    hough=[]
    
    def __init__(self):
        self.mono=[]
        self.gray=[]
        self.width=0
        self.height=0
        self.convo=[]
        self.hough=[]
        self.red=[]
        self.green=[]
        self.blue=[]

    def grayToRGB(self):
        from copy import deepcopy
        temp=deepcopy(self.gray)
        for y in range(0,self.height):
            for x in range(0,self.width):
                temp[y][x]=temp[y][x]*2        
        self.red=deepcopy(temp)
        self.green=deepcopy(temp)
        self.blue=deepcopy(temp)
    
        
         
                        
        
    def makeNegative(self):
        for y in range(0,self.height):
            for x in range(0,self.width):
                self.gray[y][x]=127-self.gray[y][x]
                if self.mono[y][x]==0:
                    self.mono[y][x]=1
                else:
                    self.mono[y][x]=0

    def makeDarker(self,percentage):
        for y in range(0,self.height):
            for x in range(0,self.width):    
                self.gray[y][x]=int(self.gray[y][x]*percentage/100)

    def makeLighter(self,percentage):
        for y in range(0,self.height):
            for x in range(0,self.width):    
                self.gray[y][x]=127-((127-self.gray[y][x])*percentage//100)

    def convolute(self,matrix,space="gray"):
        considerSpace=self.gray
        if space=="gray":
            considerSpace=self.gray
        elif space=="hough":
            considerSpace=self.hough
        matrixHeight=len(matrix)
        if matrixHeight<1:
            print("Bad matrix")
            return
        if matrixHeight % 2 ==0:
            print("Bad matrix")
            return
        firstRow=matrix[0]
        matrixWidth=len(firstRow)
        if matrixWidth<1:
            print("Bad matrix")
            return
        if matrixWidth % 2 ==0:
            print("Bad matrix")
            return
        allRows=[]
        for y in range(0,self.height):
              newRow=[]
              for x in range(0,self.width):
                  newRow.append(0)
              allRows.append(newRow)
        self.convo=allRows  
        for y in range(0,self.height):
            for x in range(0,self.width):
               lookLeft=int(0-(matrixWidth-1)/2)
               lookRight=int((matrixWidth-1)/2)
               lookUp=int(0-(matrixHeight-1)/2)
               lookDown=int((matrixHeight-1)/2)
               centerY=int(matrixHeight/2)
               centerX=int(matrixWidth/2)
               pixelSum=0
               pixelCount=0
               for yOffset in range(lookUp,lookDown+1):
                   for xOffset in range(lookLeft,lookRight+1):
                       considerNeighborX=x+xOffset
                       considerNeighborY=y+yOffset
                       if considerNeighborX<0 or considerNeighborX >= self.width or considerNeighborY <0 or considerNeighborY >= self.height:
                           continue
                       pixelCount=pixelCount+1
                       pixelSum=pixelSum+considerSpace[considerNeighborY][considerNeighborX]*matrix[centerY+yOffset][centerX+xOffset]
               newPixelValue=int(pixelSum/pixelCount)
               #Where do we write this to?
               self.convo[y][x]=newPixelValue

    def compressConvo(self,threshold=0):
        # Iterate over self.convo
        highest=self.convo[0][0]
        lowest=self.convo[0][0]
        for y in range(0,self.height):
            for x in range(0,self.width):    
                 if self.convo[y][x] > highest:
                    highest=self.convo[y][x]
                 if self.convo[y][x] < lowest:
                    lowest=self.convo[y][x]
        imageRange=highest-lowest
        ratio=127/imageRange
        #print(imageRange)
        #print(highest)
        #print(lowest)
        offset=0-lowest
        for y in range(0,self.height):
            for x in range(0,self.width):
                newValue=self.convo[y][x]+offset
                newValue=int(newValue*ratio)
                if newValue<threshold:
                    newValue=0
                self.convo[y][x]=newValue        

    def compressHough(self,threshold=0):
        # Iterate over self.convo
        highest=self.hough[0][0]
        lowest=self.hough[0][0]
        for y in range(0,self.height):
            for x in range(0,self.width):    
                 if self.hough[y][x] > highest:
                    highest=self.hough[y][x]
                 if self.hough[y][x] < lowest:
                    lowest=self.hough[y][x]
        imageRange=highest-lowest
        ratio=127/imageRange
        #print(imageRange)
        #print(highest)
        #print(lowest)
        offset=0-lowest
        for y in range(0,self.height):
            for x in range(0,self.width):
                newValue=self.hough[y][x]+offset
                newValue=int(newValue*ratio)
                if newValue<threshold:
                    newValue=0
                self.hough[y][x]=newValue 

    def findBlob(self):
        self.convolute([[5,5,5,5,5],[5,3,3,3,5],[5,3,0,3,5],[5,3,3,3,5],[5,5,5,5,5]],"hough")
        self.hough=self.convo
        
    def findEdges(self):
        self.convolute([[-2,-1,0,1,2],[-2,-1,0,1,2],[-2,-1,0,1,2],[-2,-1,0,1,2],[-2,-1,0,1,2]])
        vertical=self.convo
        self.convolute([[-2,-2,-2,-2,-2],[-1,-1,-1,-1,-1],[0,0,0,0,0],[1,1,1,1,1],[2,2,2,2,2]])
        horizontal=self.convo
        for y in range(0,self.height):
            for x in range(0,self.width):
                if y<10 or x<10 or y>=self.height-10 or x>=self.width-10:
                    # Avoid finding the outer edges of the image
                    self.convo[y][x]=0
                    
                else:
                    self.convo[y][x]=max(abs(vertical[y][x]),abs(horizontal[y][x]))

    def markEdges(self,color=0):
        for y in range(0,self.height):
            for x in range(0,self.width):
                if self.convo[y][x]>0:
                    self.gray[y][x]=color
        
        
    def markEdgesRed(self):
        for y in range(0,self.height):
            for x in range(0,self.width):
                if self.convo[y][x]>0:
                    self.red[y][x]=127
                    self.green[y][x]=0
                    self.blue[y][x]=0
                

    def markHoughRed(self):
        for y in range(0,self.height):
            for x in range(0,self.width):
                if self.hough[y][x]>25:
                    self.red[y][x]=127
                    self.green[y][x]=0
                    self.blue[y][x]=0


        


    def shrinkNicely(self,percentage=50):
        percentage=(percentage/100)**0.5
        newWidth=int(self.width*percentage)
        newHeight=int(self.height*percentage)
        newRows=[]
        newRow=[]
        newPixelWidth=1/percentage
        newPixelHeight=1/percentage # Only proportional shrink allowed so far
        pixelResidue=1
        for q in range(0,self.height):
            lastPixel=0
            newRow=[]
            pixelResidue=1
            for p in range(0,newWidth):
                newPixelValue=0
                moreNeeded=newPixelWidth
                while moreNeeded>0:
                    if moreNeeded<=pixelResidue:
                        newPixelValue=newPixelValue+self.gray[q][lastPixel]*moreNeeded
                        pixelResidue = pixelResidue - moreNeeded
                        moreNeeded=0
                    else:
                        newPixelValue=newPixelValue+self.gray[q][lastPixel]*pixelResidue
                        moreNeeded=moreNeeded-pixelResidue
                        lastPixel = lastPixel+1
                        pixelResidue=1
                newPixelValue=int(newPixelValue//newPixelWidth)
                newRow.append(newPixelValue)
            newRows.append(newRow)
        finalImage=[]
        for y in range(0,newHeight):
            horizontal=[]
            for x in range(0,newWidth):
                horizontal.append(255)
            finalImage.append(horizontal)
        for x in range(0,newWidth):
            lastPixel=0
            pixelResidue=1
            for y in range(0,newHeight):
                newPixelValue=0
                moreNeeded=newPixelHeight
                while moreNeeded>0:
                    if moreNeeded <= pixelResidue:
                        newPixelValue=newPixelValue+newRows[lastPixel][x]*moreNeeded
                        pixelResidue=pixelResidue-moreNeeded
                        moreNeeded=0
                    else:
                        newPixelValue=newPixelValue+newRows[lastPixel][x]*pixelResidue
                        moreNeeded=moreNeeded-pixelResidue
                        lastPixel=lastPixel+1
                        pixelResidue=1
                newPixelValue=int(newPixelValue//newPixelHeight)
                finalImage[y][x]=newPixelValue
        self.gray=finalImage
        self.height=newHeight 
        self.width=newWidth
        print(self.width)

    def rect(self,x1,y1,x2,y2,color=0):
        self.line(x1,y1,x2,y1,color)
        self.line(x1,y1,x1,y2,color)
        self.line(x1,y2,x2,y2,color)
        self.line(x2,y1,x2,y2,color)

    def brightestHoughPixelValue(self):
        brightest=0
        for y in range(0,self.height):
            for x in range(0,self.width):
                if self.hough[y][x]>brightest:
                    brightest=self.hough[y][x]
        return brightest

    def brightestHoughPixelCoords(self):
        bestX=0
        bestY=0
        brightest=0
        for y in range(0,self.height):
            for x in range(0,self.width):
                if self.hough[y][x]>brightest:
                    brightest=self.hough[y][x]
                    bestX=x
                    bestY=y
        #Finding a better center by averaging the coords of the brightest pixels
        brightestPixels=[]
        for y in range(0,self.height):
            for x in range(0,self.width):
                if self.hough[y][x]==brightest:
                    newPixel=[x,y]
                    brightestPixels.append(newPixel)
        #print(len(brightestPixels))
        sumX=0
        sumY=0
        for pixel in range(0,len(brightestPixels)):
            sumX+=brightestPixels[pixel][0]
            sumY+=brightestPixels[pixel][1]
        bestX=int(sumX/len(brightestPixels))
        bestY=int(sumY/len(brightestPixels))

        return bestX, bestY

    def tellTime(self,x,y,r):
        #This lines array will store all the x and y coords for points on the edge of the circle at every 6 degrees. Each row is a coord in the form [x,y].
        lines=[]
        #Add points for far right, top, far left, and bottom
        newLine=[]
        newLine=[x+r,y]
        lines.append(newLine)

        newLine=[x,y-r]
        lines.append(newLine)

        newLine=[x-r,y]
        lines.append(newLine)

        newLine=[x,y+r]
        lines.append(newLine)
        
        for degree in range(6,90,6): #Minute marks are six degrees apart, so step size = 6. Reflect points onto other quadrants of circle
            degreeInRadians=math.radians(degree)
            newX=abs(int(round((math.cos(degreeInRadians)*r),0)))
            newY=abs(int(round((math.sin(degreeInRadians)*r),0)))

            newLine=[x+newX,y-newY] #Top right
            lines.append(newLine)

            newLine=[x-newX,y-newY] #Top left
            lines.append(newLine)

            newLine=[x-newX,y+newY] #Bottom left
            lines.append(newLine)

            newLine=[x+newX,y+newY] #Bottom right
            lines.append(newLine)
        
        #Helper function to find the lines that follow the black hands of the clock most closely
        minuteIndex,hourIndex=self.findHands(x,y,r,lines)
        print(minuteIndex,hourIndex)

        #Given how lines is created, we can determine the minute and hour using the index of lines that is retruned from findHands()
        minutes=""
        minuteQuadrant=minuteIndex%4 #These quadrants follow the unit circle with 0 at 3 o'clock, 1 at 12 o'clock and so on
        oclock=False
        if minuteIndex==1: #This is the vertical 12 on minute hand
            oclock=True
            minutes="00"
        elif minuteIndex==3: #This is the vertical 6 minute hand
            minutes="30"
        elif minuteIndex==0:
            minutes="15"
        elif minuteIndex==2:
            minutes=="45"
        elif minuteQuadrant==0: #This is for minutes that are not vertical or horizontal
            minutes=str(int(minuteIndex/4))
        elif minuteQuadrant==1:
            minutes=str(int(minuteIndex/4)+45)
        elif minuteQuadrant==2:
            minutes=str(int(minuteIndex/4)+30)
        elif minuteQuadrant==3:
            minutes=str(int(minuteIndex/4)+15)
        
        hour=""
        hourQuadrant=hourIndex%4
        #The cardinal hours of 3,12,9, and 6 are treated separately
        if hourIndex==0: #This is for 3 on the hour hand
            hour="03"
        elif hourIndex==1: #This is for 12 on the hour hand
            hour="12"
        elif hourIndex==2: #This is for 9 on the hour hand
            hour="09"
        elif hourIndex==3: #This is for 6 hour hand
            hour="06"
        elif hourQuadrant==0: #This is for hours were not treated specially in the building of lines aka not 3,12,9,6
            if hourIndex<=20:
                hour="02"
            elif hourIndex<=40:
                hour="01"
            elif hourIndex<=60:
                hour="12"
        elif hourQuadrant==1:
            if hourIndex<=21:
                hour="09"
            elif hourIndex<=41:
                hour="10"
            elif hourIndex<=60:
                hour="11"
        elif hourQuadrant==2:
            if hourIndex<=22:
                hour="08"
            elif hourIndex<=42:
                hour="07"
            elif hourIndex<=60:
                hour="06"
        elif hourQuadrant==3:
            if hourIndex<=23:
                hour="03"
            elif hourIndex<=43:
                hour="04"
            elif hourIndex<=60:
                hour="05"
        
        #cutOffIndexes=[0,1,2,3,20,40,60,21,41,22,42,23,43]
        #Adjusting for exact hour
        #if oclock:
            #if not hourIndex in cutOffIndexes:
                #if (hourIndex+4) in cutOffIndexes:
                    #hour=str(int(hour)+1)
                #elif (hourIndex-4) in cutOffIndexes:
                    #hour=str(int(hour)+1)

        time = str(hour) + ":" + str(minutes)
        
        return time

    def findHands(self,x,y,r,lines):
        minuteIndex=self.findClockHand(x,y,r,lines)

        lines[minuteIndex][0]=x #Force the findClockHand to ignore the minute hand by setting its coordinates to
        lines[minuteIndex][1]=y

        hourIndex=self.findClockHand(x,y,r,lines)

        return minuteIndex,hourIndex

    def findClockHand(self,x,y,r,lines):
        longestDegree=0
        longestLine=0
        for i in range(0, len(lines)):
            testX=lines[i][0] #This is the x coord of the point on the edge of the circle at that degree
            testY=lines[i][1] #This is the y coord of the point on the edge of the cirlce at that degree

            currLength=0 #Counter for the length of the black pixels

            currX=x #Start at the center
            currY=y
            
            if testX==x and testY==y: #This is making sure that the minute hand is not counted twice
                continue

            dx=abs(testX-x) #Calculating slope at the different degrees
            dy=abs(testY-y)
            steps=max(dx,dy)
            xInc=round((dx/steps),0)
            yInc=round((dy/steps),0)
            
            closeToCardinal=False
            if (not (i==0 or i==1 or i==2 or i==3)) and xInc==0: #Making sure that if the line is not horizontal, then we are moving at least some direction in x and y
                xInc=1
                closeToCardinal=True #This boolean alerts us to check if there was rounding error
            if (not (i==0 or i==1 or i==2 or i==3)) and yInc==0:
                yInc=1
                closeToCardinal=True

            #These loops move the currX and currY markers in the appropriate directions for each quadrant of the circle
            if testX>x and testY<=y: #Top Right and horizontal, not vertical
                while currX<=testX:
                    if self.checkBlackPixel(currX, currY):
                        currLength=currLength+1
                        currX=int(currX+xInc)
                        currY=int(currY-yInc)
                    else:
                        break
            elif testX<x and testY<=y: #Top Left and horizontal, not vertical
                while currX>=testX:
                    if self.checkBlackPixel(currX, currY):
                        currLength=currLength+1
                        currX=int(currX-xInc)
                        currY=int(currY-yInc)
                    else:
                        break
            elif testX<x and testY>y: #Bottom left, not vertical, not horizontal
                while currX>=testX:
                    if self.checkBlackPixel(currX, currY):
                        currLength=currLength+1
                        currX=int(currX-xInc)
                        currY=int(currY+yInc)
                    else:
                        break
            elif testX>x and testY>y: #Bottom right, not vertical, not horizontal
                while currX<=testX:
                    if self.checkBlackPixel(currX, currY):
                        currLength=currLength+1
                        currX=int(currX+xInc)
                        currY=int(currY+yInc)
                    else:
                        break
            else: #Need to account for vertical lines
                if testY<y: #Vertical, top
                    while currY>testY:
                        if self.checkBlackPixel(currX,currY):
                            currLength=currLength+1
                            currY=currY-1
                        else:
                            break
                else: #Vertical, bottom
                    while currY<testY:
                        if self.checkBlackPixel(currX,currY):
                            currLength=currLength+1
                            currY=currY+1
                        else:
                            break
            #Checking to see if this is the longest line of black pixels
            if currLength>longestLine:
                longestLine=currLength
                #print(i)
                #print(longestLine)
                longestDegree=i
        
        #Testing for if slope is really close to 1 or if it was made 1 due to rounding. If so, it adjusts the degree appropriately
        if closeToCardinal and not(longestDegree==0 or longestDegree==3 or longestDegree==1 or longestDegree==2):
            for degree in range(6,30,6):
                degreeInRadians=math.radians(degree)
                newX=abs(int(round((math.cos(degreeInRadians)*longestLine),0)))
                newY=abs(int(round((math.sin(degreeInRadians)*longestLine),0)))
                if not self.checkBlackPixel(x+newX,y+newY) or not self.checkBlackPixel(x-newX,y+newY) or not self.checkBlackPixel(x+newX,y-newY) or not self.checkBlackPixel(x-newX,y-newY):
                    longestDegree=longestDegree+20
                    break
        
        return longestDegree
    
    def checkBlackPixel(self,x,y):
        #Helper function to check if a pixel at a given x,y is black in RGB spcae
        if self.red[y][x]==0 and self.green[y][x]==0 and self.blue[y][x]==0:
            return True
        else:
            return False


        


    def houghTransform(self,radius):

        #print("Hough Transform Started")
        self.hough=[]
        allRows=[]
        for y in range(0,self.height):
              newRow=[]
              for x in range(0,self.width):
                  newRow.append(0)
              allRows.append(newRow)
        self.hough=allRows
        results=[]
        for y in range(1,self.height-1,10):# step size for efficiency
            for x in range(1,self.width-1,10):
                if self.convo[y][x]>30: # This is a threshold value from trial and error
                    self.houghCircle(x,y,radius)

    def houghTransformParallel(self):
        from multiprocessing import Pool
        pool=Pool(8)
        print("Parallel Hough Transform Started")
        self.hough=[]
        allRows=[]
        for y in range(0,self.height):
              newRow=[]
              for x in range(0,self.width):
                  newRow.append(0)
              allRows.append(newRow)
        self.hough=allRows
        results=[]
        for y in range(1,self.height-1,10):# step size for efficiency
            for x in range(1,self.width-1,10):
                if self.convo[y][x]>30:
                    results.append(pool.apply_async(self.houghCircle,x,y,39))
        f=[]
        for a in results:
            f.append(a.get(timeout=60))
        
                
  
        

    def oldHoughCircle(self,x,y,r,color=0,fill=False):
        for v in range(y-r-1,y+r+1):
            for h in range(x-r-1,x+r+1):
                # If this pixel is r away from the center, turn it black
                dx=h-x
                dy=v-y
                distFromCenter=(dx**2+dy**2)**0.5
                if v >= self.height or h >= self.width:
                    continue # outside of image
                if v < 0 or h < 0:
                    continue # also outside
                if fill:
                    if int(distFromCenter)<r:
                        self.hough[v][h]=self.hough[v][h]+1
                else:
                    if int(distFromCenter)==r:
                        self.hough[v][h]=self.hough[v][h]+1

    def onPerimeter(self,h,v,x,y,r):
        dx=x-h
        dy=y-v
        distFromCenter=(dx**2+dy**2)**0.5
        if distFromCenter <= r+1 and distFromCenter >= r-1:
            return True
        return False
        
    def houghCircle(self,x,y,r,color=0):
        my=0
        mx=0
        h=x-r
        v=y
        if v >=0 and v<self.height and h>=0 and h<self.width:
            self.hough[v][h]=self.hough[v][h]+1
        v=v-1
        my=my-1
        while h < x:
            while self.onPerimeter(h,v,x,y,r):
                if v >=0 and v<self.height and h>=0 and h<self.width:
                    self.hough[v][h]=self.hough[v][h]+1
                if y-my >=0 and y-my< self.height   and h >=0 and h < self.width:
                    self.hough[y-my][h]=self.hough[y-my][h]+1
                if y-my >=0 and y-my< self.height and x+r-mx >=0 and x+r-mx < self.width:
                    self.hough[y-my][x+r-mx]=self.hough[y-my][x+r-mx]+1
                if x+r-mx >=0 and x+r-mx < self.width and v >=0 and v < self.height:
                    self.hough[v][x+r-mx]=self.hough[v][x+r-mx]+1
                v=v-1
                my=my-1
            h=h+1
            mx=mx+1
            if v >=0 and v<self.height and h>=0 and h<self.width:
                self.hough[v][h]=self.hough[v][h]+1
            if y-my >=0 and y-my < self.height  and h >=0 and h < self.width:
                self.hough[y-my][h]=self.hough[y-my][h]+1
            if y-my >=0 and y-my< self.height and x+r-mx >=0 and x+r-mx < self.width:
                self.hough[y-my][x+r-mx]=self.hough[y-my][x+r-mx]+1
            if x+r-mx >=0 and x+r-mx < self.width  and v >=0 and v < self.height:    
                self.hough[v][x+r-mx]=self.hough[v][x+r-mx]+1

    def circle(self,x,y,r,color=0):
        my=0
        mx=0
        h=x-r
        v=y
        if v >=0 and v<self.height and h>=0 and h<self.width:
            self.gray[v][h]=color
        v=v-1
        my=my-1
        while h < x:
            while self.onPerimeter(h,v,x,y,r):
                if v >=0 and v<self.height and h>=0 and h<self.width:
                    self.gray[v][h]=color
                if y-my >=0 and y-my< self.height   and h >=0 and h < self.width:
                    self.gray[y-my][h]=color
                if y-my >=0 and y-my< self.height and x+r-mx >=0 and x+r-mx < self.width:
                    self.gray[y-my][x+r-mx]=color
                if x+r-mx >=0 and x+r-mx < self.width and v >=0 and v < self.height:
                    self.gray[v][x+r-mx]=color
                v=v-1
                my=my-1
            h=h+1
            mx=mx+1
            if v >=0 and v<self.height and h>=0 and h<self.width:
                self.gray[v][h]=color
            if y-my >=0 and y-my < self.height  and h >=0 and h < self.width:
                self.gray[y-my][h]=color
            if y-my >=0 and y-my< self.height and x+r-mx >=0 and x+r-mx < self.width:
                self.gray[y-my][x+r-mx]=color
            if x+r-mx >=0 and x+r-mx < self.width  and v >=0 and v < self.height:    
                self.gray[v][x+r-mx]=color

    def redCircle(self,x,y,r,color=127):
        my=0
        mx=0
        h=x-r
        v=y
        if v >=0 and v<self.height and h>=0 and h<self.width:
            self.red[v][h]=color
            self.green[v][h]=0
            self.blue[v][h]=0
        v=v-1
        my=my-1
        while h < x:
            while self.onPerimeter(h,v,x,y,r):
                if v >=0 and v<self.height and h>=0 and h<self.width:
                    self.red[v][h]=color
                    self.green[v][h]=0
                    self.blue[v][h]=0
                if y-my >=0 and y-my< self.height   and h >=0 and h < self.width:
                    self.red[y-my][h]=color
                    self.green[y-my][h]=0
                    self.blue[y-my][h]=0
                if y-my >=0 and y-my< self.height and x+r-mx >=0 and x+r-mx < self.width:
                    self.red[y-my][x+r-mx]=color
                    self.green[y-my][x+r-mx]=0
                    self.blue[y-my][x+r-mx]=0
                if x+r-mx >=0 and x+r-mx < self.width and v >=0 and v < self.height:
                    self.red[v][x+r-mx]=color
                    self.green[v][x+r-mx]=0
                    self.blue[v][x+r-mx]=0
                v=v-1
                my=my-1
            h=h+1
            mx=mx+1
            if v >=0 and v<self.height and h>=0 and h<self.width:
                self.red[v][h]=color
                self.green[v][h]=0
                self.blue[v][h]=0
            if y-my >=0 and y-my < self.height  and h >=0 and h < self.width:
                self.red[y-my][h]=color
                self.green[y-my][h]=0
                self.blue[y-my][h]=0
            if y-my >=0 and y-my< self.height and x+r-mx >=0 and x+r-mx < self.width:
                self.red[y-my][x+r-mx]=color
                self.green[y-my][x+r-mx]=0
                self.blue[y-my][x+r-mx]=0
            if x+r-mx >=0 and x+r-mx < self.width  and v >=0 and v < self.height:    
                self.red[v][x+r-mx]=color
                self.green[v][x+r-mx]=0
                self.blue[v][x+r-mx]=0
        
    def badCircle(self,x,y,r,color=0,fill=False):
        for v in range(y-r-1,y+r+1):
            for h in range(x-r-1,x+r+1):
                # If this pixel is r away from the center, turn it black
                dx=h-x
                dy=v-y
                distFromCenter=(dx**2+dy**2)**0.5
                if fill:
                    if int(distFromCenter)<r:
                        self.gray[v][h]=color 
                else:
                    if int(distFromCenter)==r:
                        self.gray[v][h]=color


    def square(self,x,y,size,color):
        for p in range(x,x+size):
            for q in range(y,y+size):
                 self.gray[q][p]=color

    def line(self,x1,y1,x2,y2,color):
        if x2 < x1:
            xp=x1
            x1=x2
            x2=xp
            yp=y1
            y1=y2
            y2=yp
        xOffset=x2-x1
        yOffset=y2-y1
        if xOffset==0:
            rise=yOffset
        else:
            rise=yOffset/xOffset
        for x in range(x1,x2+1):
            xDist = x-x1
            y=int(y1+rise*xDist)
            targetY=int(y+rise)
            for py in range(min(y,targetY),max(y,targetY+1)): 
                if py >=0 and py < self.height and x >=0 and x < self.width:
                    self.gray[int(py)][x]=color

    def colorLine(self,x1,y1,x2,y2,red,green,blue):
        if x2 < x1:
            xp=x1
            x1=x2
            x2=xp
            yp=y1
            y1=y2
            y2=yp
        xOffset=x2-x1
        yOffset=y2-y1
        if xOffset==0:
            rise=yOffset
        else:
            rise=yOffset/xOffset
        for x in range(x1,x2+1):
            xDist = x-x1
            y=int(y1+rise*xDist)
            targetY=int(y+rise)
            for py in range(min(y,targetY),max(y,targetY+1)): 
                if py >=0 and py < self.height and x >=0 and x < self.width:
                    self.red[int(py)][x]=red
                    self.green[int(py)][x]=green
                    self.blue[int(py)][x]=blue
                    
    def loadMono(self,fileName):
        fileHandler=open(fileName)
        widthString=fileHandler.readline()
        heightString=fileHandler.readline()
        fileFormat=fileHandler.readline()
        pixelString=fileHandler.readline()
        fileHandler.close()
        self.width=int(widthString)        
        self.height=int(heightString)
        row=[]
        gsRow=[]
        pos=0
        for c in pixelString:
            if c == "X":
                row.append(1)
                gsRow.append(0)
            else:
                row.append(0)
                gsRow.append(127)
            pos=pos+1
            if pos % self.width == 0:
                # end of row
                self.mono.append(row)
                self.gray.append(gsRow)
                row=[]
                gsRow=[]

    def loadGrayscale(self,fileName):
        fileHandler=open(fileName, encoding="utf-8")
        widthString=fileHandler.readline()
        heightString=fileHandler.readline()
        fileFormat=fileHandler.readline()
        pixelString=fileHandler.readline()
        fileHandler.close()
        self.width=int(widthString)        
        self.height=int(heightString)
        row=[]
        monoRow=[]
        pos=0
        for c in pixelString:
            pixelValue=ord(c)
            if pixelValue==128:# Adjust for the fact that we are replacing \n and \r in our files
                pixelValue=10
            if pixelValue==129:
                pixelValue=13
            if pixelValue<64:
                monoPixel=1
            else:
                monoPixel=0
            row.append(pixelValue)
            monoRow.append(monoPixel)
            pos=pos+1
            if pos % self.width == 0:
                
                # end of row
                self.gray.append(row)
                self.mono.append(monoRow)
                monoRow=[]
                row=[]
        
    def load(self,fileName):
        fileHandler=open(fileName, encoding='utf-8')
        widthString=fileHandler.readline()
        heightString=fileHandler.readline()
        fileFormat=fileHandler.readline().replace("\n","").replace("\r","")                                                
        pixelString=fileHandler.readline()
        fileHandler.close()
        if fileFormat == "1":
            self.loadMono(fileName)
        elif fileFormat == "2":
            self.loadGrayscale(fileName)
        else:
            print(fileFormat)
            print("...")
            print("Something's wrong with the file type")

    def save(self,fileName):
        of=open(fileName,"w")
        sout=str(self.width)+"\n"+str(self.height)+"\n"+"1\n"
        for row in self.mono:
            for pixel in row:
                if pixel==0:
                    sout=sout+" "
                else:
                    sout=sout+"X"
        of.write(sout)
        of.close()

    def messitup(self):
        from random import randint
        xval=0
        yval=0
        for val in range(10,127):
            yval=yval+1
            for y in range(10,127):
                xval=xval+1
                  
                #self.gray[y][val]=val
                self.red[y][val]=int(xval)
                self.blue[y][val]=int(xval)
                self.green[y][val]=int(yval)
                


    def saveRGB(self,fileName):
        print("Saving")
        of=open(fileName,"wb")
        sout=str(self.width)+"\n"+str(self.height)+"\n"+"3\n"
        of.write(sout.encode('utf8'))

        for theColor in [self.red,self.green,self.blue]:
            sout=""
            for row in theColor:
                for pixel in row:
                    newCharValue=pixel
                    newChar=chr(int(newCharValue//2)).replace("\n",chr(128)).replace("\r",chr(129))
                    sout=sout+newChar
            sout=sout+"\n"
            of.write(sout.encode('utf8'))

        of.close()

        

    def saveGrayscale(self,fileName):
        print("Saving")
        of=open(fileName,"wb")
        sout=str(self.width)+"\n"+str(self.height)+"\n"+"2\n"
        for row in self.gray:
            for pixel in row:
                # Need to get value of pixel (0-127)
                # Convert that to a character
                # append it to sout
                newCharValue=pixel
                if newCharValue <8:
                    newCharValue=0 # TESTING ONLY !!!!!!!!!!!!!!!!
                newChar=chr(newCharValue).replace("\n",chr(128)).replace("\r",chr(129))
                sout=sout+newChar
        print(len(sout))
        print(self.width*self.height)
        of.write(sout.encode('utf8'))
        of.close()

    def saveConvo(self,fileName):
        print("Saving")
        of=open(fileName,"wb")
        sout=str(self.width)+"\n"+str(self.height)+"\n"+"2\n"
        
        for row in self.convo:
            for pixel in row:
                # Need to get value of pixel (0-127)
                # Convert that to a character
                # append it to sout
                newCharValue=pixel
                try:
                    newChar=chr(newCharValue).replace("\n",chr(128)).replace("\r",chr(129))
                except:
                    print(newCharValue)
                sout=sout+newChar
        print(len(sout))
        print(self.width*self.height)
        of.write(sout.encode('utf8'))
        of.close()


    def saveHough(self,fileName):
        print("Saving")
        of=open(fileName,"wb")
        sout=str(self.width)+"\n"+str(self.height)+"\n"+"2\n"
        
        for row in self.hough:
            for pixel in row:
                # Need to get value of pixel (0-127)
                # Convert that to a character
                # append it to sout
                newCharValue=pixel
                try:
                    newChar=chr(newCharValue).replace("\n",chr(128)).replace("\r",chr(129))
                except:
                    print(newCharValue)
                sout=sout+newChar
        print(len(sout))
        print(self.width*self.height)
        of.write(sout.encode('utf8'))
        of.close()




    def loadJPG(self,fileName,colorMode=2):
        from PIL import Image
        self.colorMode=colorMode
        sout=""
        im = Image.open(fileName,"r")
        #pix=im.load()
        w,h=im.size
        self.width=w
        self.height=h
        #sout=str(w)+"\n"+str(h)+"\n"
        pixels=list(im.getdata())
        c=0
        y=0
        x=0
        row=[]
        redrow=[]
        greenrow=[]
        bluerow=[]
        col=[]
        for p in pixels:
            c=c+1
            if colorMode==3:#color
                redrow.append(p[0])
                greenrow.append(p[1])
                bluerow.append(p[2])
                if c%w ==0:
                    self.red.append(redrow)
                    self.green.append(greenrow)
                    self.blue.append(bluerow)
                    redrow=[]
                    greenrow=[]
                    bluerow=[]
                    y=y+1
                    x=0
                else:
                    x=x+1
            else:#not rgb
                if type(p)==type(5): #checking if p is an integer
                    p=[p,p,p]
                pixelValue=(p[0]+p[1]+p[2])//3
                if self.colorMode==1:#monochrome
                    if pixelValue<10: # thresholding
                        row.append(0)
                    else:
                        row.append(255)
                else:#greyscale
                    row.append(pixelValue//2)
                if c%w ==0:
                    self.gray.append(row)
                    row=[]
                    y=y+1
                    x=0
                else:
                    x=x+1





 
               
