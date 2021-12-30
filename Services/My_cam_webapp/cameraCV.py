import cv2 as cv
import numpy as np
#import matplotlib.pyplot as plt

cam = cv.VideoCapture(0)

my_colors = [[5, 107, 0, 19, 255, 255],
[133, 56, 0, 159, 156, 255],
[57, 76, 0, 100, 255, 255]]


def find_color(img, my_colors):
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    for color in my_colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv.inRange(img_hsv, lower, upper)
        cv.imshow(f'{color[0]}', mask)


while True:
    stream, frame = cam.read()
    find_color(frame, my_colors)
    if stream:
        cv.imshow('Pic', frame)
        w = cv.waitKey(1)
        if w == ord('q'):
            break
    else:
        break

