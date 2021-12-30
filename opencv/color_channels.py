import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img = cv.imread('pic_vic/picture_test.jpg')
cv.imshow('Pic', img)
plank = np.zeros(img.shape[:2], np.uint8)

b, g, r = cv.split(img)  #slipt img into 3 different color channels
blue = cv.merge([b, plank, plank])
green = cv.merge([plank, g, plank])
red = cv.merge([plank, plank, r])
# cv.imshow('b', blue)
# cv.imshow('g', green)
cv.imshow('r', red)
plt.imshow(blue)
plt.show()
# img_merge = cv.merge([b, g, r])
# cv.imshow('Merge', img_merge)

cv.waitKey(0)