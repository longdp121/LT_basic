import cv2 as cv
import numpy as np

def rescale_frame(frame,scale = 1):
    '''
    This func resize frame of image, video and live video
    '''
    new_h = int(frame.shape[0] * scale)
    new_w = int(frame.shape[1] * scale)

    return cv.resize(frame, (new_w, new_h))

img = cv.imread('pic_vic/hoa_con_small.jpg')
img_resize = rescale_frame(img, 0.8)
cv.imshow('My Pic Resize', img_resize)


video = cv.VideoCapture('pic_vic/video_test.mp4')

while True:
    or_vid_run, or_frame = video.read()
    video_resize = rescale_frame(or_frame, 2)
    if or_vid_run == True:
        cv.imshow('My Orignal vid', or_frame)
        cv.imshow('My new size vid', video_resize)
        if cv.waitKey(1) == ord('q'):
            break
    else:
        break


cv.waitKey(0)