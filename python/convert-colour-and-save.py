import cv2
img1 = cv2.imread('./images/catan-game-board.jpg', 1)
img1gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imwrite('./results/catan-board-bgr2gray.jpg',img1gray)
