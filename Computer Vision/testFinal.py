from pcImage import pcImage
image=pcImage()
image.load("ferrisWheel3.pcimg")
print("Finding Edges")
image.findEdges()
image.compressConvo(15)

# Covolution Results
#image.saveConvo("convoClockat15past7.pcimg")

#Hough Transform Results
print("Hough Transform Started")
#Run this with different radii
maxRadius=min(image.height,image.width)//2
bestRadius=10
highestPixel=0
for r in range(10,maxRadius,5):
    image.houghTransform(r)
    currBrightestPixel = image.brightestHoughPixelValue()
    #print("Brightest Pixel a radius %d: %d"%(r,image.brightestHoughPixelValue()))
    if currBrightestPixel > highestPixel:
        highestPixel=currBrightestPixel
        bestRadius=r
print("The best radius is %d"%bestRadius)
image.houghTransform(bestRadius)
#image.saveHough("ferrisWheel3HoughExample.pcimg")

# Determine the highest pixel value in each iteration
# Print that value for each iteration
#DEFAULT COMPRESSION = 40 for BELOW TWO COMPRESSIONS
image.compressHough(40)
#image.saveHough("ferrisWheel3HoughExample.pcimg")


image.findBlob()
image.compressHough(70)

#image.saveHough("ferrisWheel3HoughExample.pcimg")

print("Marking in RGB")
image.grayToRGB()

#Remove 4 lines below after done
x,y=image.brightestHoughPixelCoords()
image.redCircle(x,y,bestRadius)
image.markHoughRed()
image.saveRGB("ferrisWheel3MarkedRed.pcimg")

'''
x,y=image.brightestHoughPixelCoords()
time=image.tellTime(x,y,bestRadius)
print("The time on the clock is about: " + time)
image.redCircle(x,y,bestRadius)
image.markHoughRed()
image.saveRGB("clockat15past7Test.pcimg")
'''



