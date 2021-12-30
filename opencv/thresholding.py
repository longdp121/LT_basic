import cv2 as cv
import numpy as np

img = cv.imread('pic_vic/picture_test.jpg')
#cv.imshow('Pic', img)

#Convert to gray
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', img_gray)

#Simple thresholding 
# '''
# THRESH_BINARY mode switch every pixel which has color code above thresh (140) into maxval (255)
# '''
# threshold, thresh = cv.threshold(img_gray, 140, 255, cv.THRESH_BINARY)
# cv.imshow('Threshold', thresh)

# '''
# THRESH_BINARY_INV mode switch every pixel which has color code below thresh (140) into maxval (255)
# '''
# threshold, thresh_inv = cv.threshold(img_gray, 140, 255, cv.THRESH_BINARY_INV)
# cv.imshow('Threshold inv', thresh_inv)

#Adoptive thresholding
adap_thresh = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adap Thresh', adap_thresh)

adap_thresh_inv = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 3)
#cv.imshow('Adap Thresh Inv', adap_thresh_inv)

adap_thresh_gau = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adap Thresh Gau', adap_thresh_gau)

cv.waitKey(0)