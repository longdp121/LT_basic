import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('pic_vic/hoa_con_small.jpg')
#cv.imshow('Pic', img)

#Histogram of gray img
#Convert to gray
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', img_gray)

#Creat mask
#blank = np.zeros((img.shape[0], img.shape[1]), dtype = np.uint8)
#cv.imshow('Blank', blank)
#cir = cv.circle(blank.copy(), (blank.shape[1] // 2, blank.shape[0] // 2), 100, 255, -1)
#img_gray_masked = cv.bitwise_and(img_gray, img_gray, mask = cir)
# cv.imshow('Masked Gray', img_gray_masked)


gray_hist = cv.calcHist([img_gray], [0], None, [256], [0, 256])
plt.figure()
plt.title('Gray histogram from youtue')
plt.xlabel('Bins')
plt.ylabel('Num of pixel')
plt.plot(gray_hist)
plt.show()


#Histogram of color img
#Creat mask
img_masked = cv.bitwise_and(img, img, mask = cir)
cv.imshow('Masked', img_masked)

plt.figure()
plt.title('Color img histogram')
plt.xlabel('Bins')
plt.ylabel('Num of pixel')
colors = ('b', 'g', 'r')
for chan, col in enumerate(colors):
    '''
    Mask in calcHist must be binary picture
    Because calcHist draw singe channel each time
    '''
    print(chan)
    img_hist = cv.calcHist([img], [chan], cir, [256], [0, 256])
    plt.plot(img_hist, color = col)

#plt.show()
#cv.waitKey(0)