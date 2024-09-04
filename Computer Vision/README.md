# Computer Vision Projects
*What I have learned about displaying and analyzing a continuous world in a discrete space!*

## Propriertery Image Format
### The .pcimg Image Format
This image format was used in my Computer Vision coursework as a way to help us understand basic Computer Vision concepts and to enforce original work. The goal of this
format was not efficiency and I acknowledge that it is not efficient or optimized.

**Basic Format of a .pcimg File**
line #1: length
line #2: width
line #3: either '1' for black and white, '2' for grayscale, and '3' for color
line #4: ASCII characters (color images have 3 lines: one for reds, one for greens, and one for blues)

The format can load black and white, grayscale, and color (RGB) images. The format uses ASCII characters to represent color values from 0-127, where 0 is black and 127 is white.
An HTML file called imageViewer.html (see Computer Vision Folder) is used to display the .pcimg files onto a canvas on a webpage (color images are encoded using utf8 because it is backwards
compatible with the 7-bit ASCII characters).

**Example:**
![Screenshot 2024-09-04 151605](https://github.com/user-attachments/assets/93cb322a-bf13-4b70-ab05-31769e8f8739)

**Storing a .pcimg File**
To manipulate our .pcimg file, it is stored in lists of lists where image[1][2] returns the pixel value (0-127) of the pixel at (2,3).

## Edge Detection
Part of our work was implementing an edge detection algorithm by performing a convolution.

Our convolution matrices or kernels were:

**Vertical:**
[[-2,-1,0,1,2],
 [-2,-1,0,1,2],
 [-2,-1,0,1,2],
 [-2,-1,0,1,2],
 [-2,-1,0,1,2]]

 **Horizontal:**
 [[-2,-2,-2,-2,-2],
  [-1,-1,-1,-1,-1],
  [0,0,0,0,0],
  [1,1,1,1,1],
  [2,2,2,2,2]]

The **findEdges()** function runs the image through these two matrices and creates a vertical convolution and a horizontal convolution. While ignoring the edges of the
image itself, this function then combines these convolutions by finding the max of the abosolute value of each convultion at each (x,y) coordinate of the image and
stores the result in the self.convo instance variable. For reference, the strongest edges have greater pixel values.

The **compressConvo()** function then finds the range of values in self.convo, adds an offset equal to 0-lowest pixel value, and adjusts the values proportionally
using a ratio of 127/imageRange. The final step is using the inputted compression threshold (which we mostly determined by trial and error) to use as a cutoff for
weak edges. In other words, this threshold reduces the noise. A higher value restricts more values and vice versa with a lower value.

**Example:**
Before:
![Screenshot 2024-09-04 155037](https://github.com/user-attachments/assets/0f7c802e-4f51-4f00-8c02-6beec5cd9161)
After:
![Screenshot 2024-09-04 155135](https://github.com/user-attachments/assets/1015ab21-9539-4fbb-9009-9157e976869e)

## Hough Transform

After a convolution, we then performed a Hough transform on the images to try to detect circles. A Hough transform was performed by starting with some radius value (ours was 10), iterating through our
self.convo list of lists by stepping (10) pixels in both the x and y directions, and then checking if the pixel value was above some threshold (ours was 30). If it was above the treshold, then a circle was draw with
the current radius. This process was repeated after every radius+=5 and went until the theoretical maximum radius of min(image.height,image.width)//2.

**Our Results**
![Screenshot 2024-09-04 161355](https://github.com/user-attachments/assets/f76c9478-6079-4c53-8566-f43af4295fb5)

Then, using the same logic and algorithm from compressConvo(), we made a **compressHough()** function to act on the self.hough instance variable.

**After Compression**
![Screenshot 2024-09-04 162123](https://github.com/user-attachments/assets/1790b7f2-cfb9-4bbe-87a1-65140ed2476c)

Then, we made a **findBlob()** function that convolutes the above image with this matrix:
[[5,5,5,5,5],
 [5,3,3,3,5],
 [5,3,0,3,5],
 [5,3,3,3,5],
 [5,5,5,5,5]]
 Finally, this image is compressed for a final time:

 **After findBlob() and second compression**
![Screenshot 2024-09-04 161926](https://github.com/user-attachments/assets/34bbd82a-3a22-4a69-85e8-973e7af90f42)

