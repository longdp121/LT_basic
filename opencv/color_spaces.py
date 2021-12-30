import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('pic_vic/hoa_con_small.jpg')
cv.imshow('My pic', img)

# plt.imshow(img)
# plt.show()

# #BGR to gray
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_gray_2_bgr = cv.cvtColor(img_gray, cv.COLOR_GRAY2BGR)
'''
Will not work
'''
#cv.imshow('Gray', img_gray)
#cv.imshow('Gray -> BRG', img_gray_2_bgr)
plt.imshow(img_gray_2_bgr)
plt.show()

#BGR to HSV
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
img_hsv_2_bgr = cv.cvtColor(img_hsv, cv.COLOR_HSV2BGR)
#cv.imshow('HSV', img_hsv)
#cv.imshow('HSV -> BGR', img_hsv_2_bgr)


#BGR to L A B
img_lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
img_lab_2_bgr = cv.cvtColor(img_lab, cv.COLOR_LAB2BGR)
#cv.imshow('LAB', img_lab)
#cv.imshow('LAB -> BGR', img_lab_2_bgr)

#BGR to RGB
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_rgb_2_bgr = cv.cvtColor(img_rgb, cv.COLOR_RGB2BGR)
#cv.imshow('RGB', img_rgb)
cv.imshow('RGB -> BGR', img_rgb_2_bgr)

# plt.imshow(img_rgb)
# plt.show()

cv.waitKey(0)