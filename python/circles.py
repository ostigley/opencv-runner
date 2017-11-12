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
hex_s = None
hex_h = None
hex_i = None
hex_r = None
hex_b = None
hex_c = None
hex_j = None
hex_q = None
hex_g = None
hex_a = None
hex_d = None
hex_k = None
hex_p = None
hex_f = None
hex_e = None
hex_l = None
hex_o = None
hex_n = None
hex_m = None

for i in circles:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imwrite('./src/results/catan-circles.jpg',cimg)