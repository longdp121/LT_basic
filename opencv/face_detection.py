import cv2 as cv
import numpy as np


# img = cv.imread('pic_vic/faces.jpg')
# #cv.imshow('Face', img)

# img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# #cv.imshow('Gray', img_gray)

haar_cas = cv.CascadeClassifier('haar_face.xml')
# face_detect = haar_cas.detectMultiScale(img_gray, scaleFactor = 1.1, minNeighbors = 9)
# #print(face_detect)
# #print(len(face_detect))

cam = cv.VideoCapture(0)
while True:
    ret, frame = cam.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_detect = haar_cas.detectMultiScale(frame_gray, scaleFactor = 1.1, minNeighbors = 1)
    print(len(face_detect))
    for (x, y, w, h) in face_detect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv.imshow('Frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# for (x, y, w, h) in face_detect:
#     print(face_detect)
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
# cv.imshow('Found', img)

# cv.waitKey(0)