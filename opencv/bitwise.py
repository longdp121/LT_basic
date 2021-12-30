import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype = "uint8")

reg = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
cir = cv.circle(blank.copy(), (blank.shape[0] // 2, blank.shape[1] // 2), 200, 255, -1)

# cv.imshow('Reg', reg)
# cv.imshow('Cir', cir)

#Bitwise AND
#Put 2 pictures onto each other and return intersection
#bit_and = cv.bitwise_and(reg, cir)
bit_and = cv.bitwise_and(cir, reg)
#cv.imshow('Bit and', bit_and)

#Bitwise OR
#Put 2 pictures onto each other and return both intersection and extra 
bit_or = cv.bitwise_or(reg, cir)
#cv.imshow('Bit or', bit_or)

#Bitwise XOR
#Put 2 pictures onto each other and return none intersection part
bit_xor = cv.bitwise_xor(reg, cir)
#cv.imshow('Bit xor', bit_xor)

#Bitwise Not
bit_not = cv.bitwise_not(reg)
#cv.imshow('Bit not', bit_not)


#This below give error because 2 pics have to be same size and type
img = cv.imread('pic_vic/picture_test.jpg')
img_2 = cv.imread('pic_vic/hoa_con_small.jpg')

bit_a = cv.bitwise_and(img, img_2)
cv.imshow('Bit a', bit_a)

cv.waitKey(0)