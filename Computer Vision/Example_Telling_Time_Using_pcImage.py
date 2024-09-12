from pcImage import pcImage
image=pcImage()
image.load("clockat15past7.pcimg")
print("Finding Edges")
image.findEdges()
image.compressConvo(15)

#Hough Transform Results
print("Hough Transform Started")
#Run this with different radii
maxRadius=min(image.height,image.width)//2
bestRadius=10
highestPixel=0
for r in range(10,maxRadius,5):
    image.houghTransform(r)
    currBrightestPixel = image.brightestHoughPixelValue()
    #print("Brightest Pixel at radius %d: %d"%(r,image.brightestHoughPixelValue()))
    if currBrightestPixel > highestPixel:
        highestPixel=currBrightestPixel
        bestRadius=r
print("The best radius is %d"%bestRadius)
image.houghTransform(bestRadius)
#DEFAULT COMPRESSION = 40 for BELOW TWO COMPRESSIONS
image.compressHough(40)

image.findBlob()
image.compressHough(40)

print("Marking in RGB")
image.grayToRGB()

x,y=image.brightestHoughPixelCoords()
time=image.tellTime(x,y,bestRadius)
print("The time on the clock is about: " + time)
image.redCircle(x,y,bestRadius)
image.markHoughRed()
image.saveRGB("clockat15past7Test.pcimg")




