import cv2 as cv
import numpy as np

img = cv.imread('pic/in 2.JPG')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imwrite('gray.jpg', img_gray)
print('ok')