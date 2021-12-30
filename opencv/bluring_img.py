import cv2 as cv
import numpy as np

img = cv.imread('pic_vic/hoa_con_small.jpg')
cv.imshow('Pic', img)

# # Averiging
# img_ave = cv.blur(img, (7, 7))
# cv.imshow('Blur', img_ave)

# # Gausslan blur
# img_gau = cv.GaussianBlur(img, (7, 7), 0)
# cv.imshow('Gau blur', img_gau)

# #Median blur
# #Blur and look like painting
# img_med = cv.medianBlur(img, 7)
# cv.imshow('Med blur', img_med)

#Bilateral lur
#Very good at reduce noise. d == 5 is recommend
img_bi = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bi img', img_bi)

cv.waitKey(0)