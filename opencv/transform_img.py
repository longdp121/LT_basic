import cv2 as cv
import numpy as np

img = cv.imread('pic_vic/picture_test.jpg')

#cv.imshow('My pic', img)

#Translating image
def trans_pic(img, x, y):
    trans_matrix = np.float32([[1, 0, x], [0, 1, y]])
    pic_size = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_matrix, pic_size)

# -x --> left
# x --> right
# -y --> up
# y --> down

img_trans = trans_pic(img, -100, 100)
#cv.imshow('Trans img', img_trans)

#Rotation image
def rotate_img(img, ange, point = None):
    (h, w) = img.shape[:2]
    if point == None:
        '''
        If point is none, center of imgage is default
        '''
        point = (w // 2, h // 2)
    else:
        pass

    rotate_matrix = cv.getRotationMatrix2D(point, ange, 1)
    pic_size = (w, h)
    return cv.warpAffine(img, rotate_matrix, pic_size)

# ange -- > Rotate counterclockwise
# -ang --> Rotate clockwise

img_rotate = rotate_img(img, 45)
#cv.imshow('Rotate img', img_rotate)

#Resizing image
img_resize = cv.resize(img, (1000, 300), interpolation = cv.INTER_CUBIC)
#cv.imshow('Resize img', img_resize)

#Flipping image
# 0 --> Flip upside down around ox
# 1 --> Flip left to right/right to left around oy
#-1 --> Flip upside down around ox and left to right/right to left around oy at same time
img_flip = cv.flip(img, 0)
img_flip_2 = cv.flip(img, -1)
cv.imshow('Flip image', img_flip)
cv.imshow('Flip image2', img_flip_2)


cv.waitKey(0)