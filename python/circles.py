# https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
import numpy as np
import cv2
img = cv2.imread('./images/catan-game-board-straight.jpg', 0)

height, width = img.shape
circleRadius = int(width/22/2)
minRadius = circleRadius - 5
maxRadius = circleRadius + 5
cropRadiusX =  int(circleRadius * 0.65)
cropRadiusY =  int(circleRadius * 0.5)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
cv2.imwrite('test.jpg',cimg)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,200,
                            param1=50,param2=30,minRadius=minRadius,maxRadius=maxRadius)
# round
# print(circles)
# if not any(circles):
#   print('no circles');
#   exit();
circles = np.uint16(np.around(circles))

# Sort in to hexes and their rows
circles = sorted(circles[0], key=lambda x: x[1])
row1 = sorted([circles[0], circles[1], circles[2]], key=lambda x: x[0])
row2 = sorted([circles[3], circles[4], circles[5], circles[6]], key=lambda x: x[0])
row3 = sorted([circles[7], circles[8], circles[9], circles[10]], key=lambda x: x[0])
row4 = sorted([circles[11], circles[12], circles[13], circles[14]], key=lambda x: x[0])
row5 = sorted([circles[15], circles[16], circles[17]], key=lambda x: x[0])

# TODO: locate desert based on length of rows
if len(row1) == 2:
  print('The desert is in row1')
if len(row2) == 3:
  print('The desert is in row2')
if len(row3) == 4:
  print('The desert is in row3')
if len(row4) == 3:
  print('The desert is in ro42')
if len(row5) == 2:
  print('The desert is in row5')

# Save segment of hex
for i,circle in enumerate(circles):
  # Crop and save
  smallCircle = cimg[(circles[i][1]-cropRadiusY):(circles[i][1]+cropRadiusY), (circles[i][0]-cropRadiusX):(circles[i][0]+cropRadiusX) ]
  cv2.imwrite('./results/circle' + str(i)  + '.tif', smallCircle)

  # draw the outer circle
  cv2.circle(cimg,(circle[0],circle[1]),circle[2],(0,255,0),2)
  # draw the center of the circle
  cv2.circle(cimg,(circle[0],circle[1]),2,(0,0,255),3)



cv2.imwrite('./results/catan-circles.jpg',cimg)