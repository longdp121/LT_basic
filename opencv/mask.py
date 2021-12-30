import cv2 as cv
import numpy as np

img = cv.imread('pic_vic/picture_test.jpg')
#cv.imshow('Pic', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')
#cv.imshow('Blnak', blank)

my_mask = cv.circle(blank, (img.shape[1] //2, img.shape[0] //2), 100, 225, -1)
#cv.imshow('Mask', my_mask)

img_masked = cv.bitwise_and(img, img, mask = my_mask)
cv.imshow('Img masked', img_masked)

cv.waitKey(0)