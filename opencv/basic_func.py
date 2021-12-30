import cv2 as cv
import numpy as np

img = cv.imread('pic_vic/picture_test.jpg')
cv.imshow('My pic', img)

# Converting to grayclor
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray pic', img_gray)

#Blur
img_blur = cv.GaussianBlur(img, (1, 19), cv.BORDER_DEFAULT)
#cv.imshow('Blur img', img_blur)

#Edge cascade xác định các cạnh của vật thể
img_canny = cv.Canny(img, 250, 250)
#cv.imshow('Canny img', img_canny)

#Dilating image  #Làm dày đường viền của vật thể
# iterations == sự lặp lại
img_dilated = cv.dilate(img_canny, (3, 3), iterations = 1)
#cv.imshow('Dilated img', img_dilated)

#Eroding image  #Làm mỏng đường viền của vật thể
img_ero = cv.erode(img_canny, (3, 3), iterations = 1)
#cv.imshow('Eroding img', img_ero)

#Resize img
img_resize = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
#cv.imshow('Resize', img_resize)

#Cropping img
img_crop = img[50:250, 180:320]
cv.imshow('Crop', img_crop)


cv.waitKey(0)