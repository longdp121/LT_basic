import cv2 as cv
import numpy as np

#Numpy array come with row_num and collumn_num
blank = np.zeros((500, 500, 3), dtype = np.uint8)

# Change the whole blank into other color. Note that need to add 3 as color channel to the matrix
#blank[100 : 200, 250 : 300] = 0, 0, 225
#cv.imshow('My pic', blank)

# Draw retangle on image
cv.rectangle(blank, (250, 0), (350, 250), (0, 255, 0), cv.FILLED)
cv.imshow('My pic new', blank)

# Draw circle on image
cv.circle(blank, (100, 100), 100, (0, 255, 0))
cv.imshow('Circle', blank)

# Draw a line on image
cv.line(blank, (0, 0), (blank.shape[1], blank.shape[1]), (0, 255, 0), thickness = 3)
cv.imshow('Line', blank)

#Write text on image
cv.putText(blank, 'Hello', 
            (150, 150), 
            cv.FONT_HERSHEY_COMPLEX, 
            1.0, 
            (0, 244, 0), 
            thickness = 2)
cv.imshow('Text', blank)

cv.waitKey(0)