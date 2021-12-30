import cv2 as cv
import numpy as np

img = cv.imread('pic_vic/hoa_con_small.jpg')

#cv.imshow('My pic', img)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Turn pic into gray

#cv.imshow('Gray img', img_gray)

img_canny = cv.Canny(img, 150, 255)  # Turn pic into binary

#cv.imshow('Canny img', img_canny)

contours, hierarchies = cv.findContours(img_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#Contours: Tập các điểm-liên-tục tạo thành một đường cong, trả về dưới dang list
#Hierarchy: Danh sách các vector chứa mối quan hệ giữa các contours

cv.drawContours(img, contours, -1, (0, 255, 0), 1)  #Draw contours onto original piture
cv.imshow('My pick', img)

cv.waitKey(0)
'''
https://www.phamduytung.com/blog/2019-05-26-contours/
'''