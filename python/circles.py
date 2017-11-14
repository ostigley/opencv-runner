# https://www.pyimagesearch.com/2014/07/21/detecting-circles-images-using-opencv-hough-circles/
import numpy as np
import cv2
img = cv2.imread('./src/images/catan-board-original.jpg', 0)

img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,200,
                            param1=50,param2=30,minRadius=20,maxRadius=30)
# round
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
circle0 = cimg[(circles[0][1]-30):(circles[0][1]+30), (circles[0][0]-30):(circles[0][0]+30) ]
circle1 = cimg[(circles[1][1]-30):(circles[1][1]+30), (circles[1][0]-30):(circles[1][0]+30) ]
circle2 = cimg[(circles[2][1]-30):(circles[2][1]+30), (circles[2][0]-30):(circles[2][0]+30) ]
circle3 = cimg[(circles[3][1]-30):(circles[3][1]+30), (circles[3][0]-30):(circles[3][0]+30) ]
circle4 = cimg[(circles[4][1]-30):(circles[4][1]+30), (circles[4][0]-30):(circles[4][0]+30) ]
circle5 = cimg[(circles[5][1]-30):(circles[5][1]+30), (circles[5][0]-30):(circles[5][0]+30) ]
circle6 = cimg[(circles[6][1]-30):(circles[6][1]+30), (circles[6][0]-30):(circles[6][0]+30) ]
circle7 = cimg[(circles[7][1]-30):(circles[7][1]+30), (circles[7][0]-30):(circles[7][0]+30) ]
circle8 = cimg[(circles[8][1]-30):(circles[8][1]+30), (circles[8][0]-30):(circles[8][0]+30) ]
circle9 = cimg[(circles[9][1]-30):(circles[9][1]+30), (circles[9][0]-30):(circles[9][0]+30) ]
circle10 = cimg[(circles[10][1]-30):(circles[10][1]+30), (circles[10][0]-30):(circles[10][0]+30) ]
circle11 = cimg[(circles[11][1]-30):(circles[11][1]+30), (circles[11][0]-30):(circles[11][0]+30) ]
circle12 = cimg[(circles[12][1]-30):(circles[12][1]+30), (circles[12][0]-30):(circles[12][0]+30) ]
circle13 = cimg[(circles[13][1]-30):(circles[13][1]+30), (circles[13][0]-30):(circles[13][0]+30) ]
circle14 = cimg[(circles[14][1]-30):(circles[14][1]+30), (circles[14][0]-30):(circles[14][0]+30) ]
circle15 = cimg[(circles[15][1]-30):(circles[15][1]+30), (circles[15][0]-30):(circles[15][0]+30) ]
circle16 = cimg[(circles[16][1]-30):(circles[16][1]+30), (circles[16][0]-30):(circles[16][0]+30) ]
circle17 = cimg[(circles[17][1]-30):(circles[17][1]+30), (circles[17][0]-30):(circles[17][0]+30) ]

cv2.imwrite('./src/results/circle0.jpg', circle0)
cv2.imwrite('./src/results/circle1.jpg', circle1)
cv2.imwrite('./src/results/circle2.jpg', circle2)
cv2.imwrite('./src/results/circle3.jpg', circle3)
cv2.imwrite('./src/results/circle4.jpg', circle4)
cv2.imwrite('./src/results/circle5.jpg', circle5)
cv2.imwrite('./src/results/circle6.jpg', circle6)
cv2.imwrite('./src/results/circle7.jpg', circle7)
cv2.imwrite('./src/results/circle8.jpg', circle8)
cv2.imwrite('./src/results/circle9.jpg', circle9)
cv2.imwrite('./src/results/circle10.jpg', circle10)
cv2.imwrite('./src/results/circle11.jpg', circle11)
cv2.imwrite('./src/results/circle12.jpg', circle12)
cv2.imwrite('./src/results/circle13.jpg', circle13)
cv2.imwrite('./src/results/circle14.jpg', circle14)
cv2.imwrite('./src/results/circle15.jpg', circle15)
cv2.imwrite('./src/results/circle16.jpg', circle16)
cv2.imwrite('./src/results/circle17.jpg', circle17)


count = 0
for i in circles:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    # cv2.imwrite('./src/results/circle'+str(count))
    count


cv2.imwrite('./src/results/catan-circles.jpg',cimg)