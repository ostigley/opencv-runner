import cv2
img1 = cv2.imread('./src/images/catan-board-original.jpg', 1)

img1gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imwrite('./src/results/catan-board-bgr2gray.jpg',img1gray)
