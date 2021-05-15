import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('1.jpg',0)
cv2.namedWindow('inputPic', cv2.WINDOW_NORMAL)
cv2.imwrite('3.png',img)
cv2.imshow('inputPic',img)
cv2.imwrite('2.png',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
