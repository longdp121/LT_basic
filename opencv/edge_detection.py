import cv2 as cv
import numpy as np

img = cv.imread('pic_vic/picture_test.jpg')
#cv.imshow('Pic', img)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', img_gray)

# #Laplacian
# #Look like pencil panting
# img_lap = cv.Laplacian(img_gray, cv.CV_64F)
# '''
# Because img cannot hold negative (-) pixel vallue
# Need to put img_lap inside absolute()
# '''
# img_lap = np.uint8(np.absolute(img_lap))
# cv.imshow('Lap', img_lap)

#Sobel
#Sobel use for advance task
img_sobel_x = cv.Sobel(img_gray, cv.CV_64F, 1, 0)
img_sobel_y = cv.Sobel(img_gray, cv.CV_64F, 0, 1)
img_combine = cv.bitwise_or(img_sobel_x, img_sobel_y)

cv.imshow('Sobel x', img_sobel_x)
cv.imshow('Sobel y', img_sobel_y)
cv.imshow('Combine img', img_combine)

cv.waitKey(0)