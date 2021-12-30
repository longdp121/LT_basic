import cv2 as cv
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# video = cv.VideoCapture(0)

# while True:
#     stream, img = video.read()
#     img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#     h_img, w_img, _ = img.shape
#     my_config = r'--oem 3 --psm 6 outputbase digits'
#     boxes = pytesseract.image_to_data(img, config = my_config)
#     #print(boxes)
#     for x, b in enumerate(boxes.splitlines()):
#         if x != 0:
    #         b = b.split()
    #         #print(b)
    #         if len(b) == 12:
    #             x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
    #             cv.rectangle(img, (x, y), (w + x, h + y), (0, 255, 0), thickness = 1)
    #             cv.putText(img, b[11], (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
    # cv.imshow('My pic', img)
    # w = cv.waitKey(1)
    # if w == ord('q'):
    #     cv.destroyAllWindows()
    #     break

img = cv.imread('pic_vic/test.png')

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)


# Detecting charaters
print(pytesseract.image_to_string(img))

h_img, w_img, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    #print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv.rectangle(img, (x, h_img - y), (w, h_img - h), (0, 255, 0), thickness = 1)
    cv.putText(img, b[0], (x, h_img - y + 30), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))


# Detecting world

h_img, w_img, _ = img.shape
my_config = r'--oem 3 --psm 6 outputbase digits'
boxes = pytesseract.image_to_data(img, config = my_config)
print(boxes)
for x, b in enumerate(boxes.splitlines()):
    if x != 0:
        b = b.split()
        print(b)
        if len(b) == 12:
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
            cv.rectangle(img, (x, y), (w + x, h + y), (0, 255, 0), thickness = 1)
            cv.putText(img, b[11], (x, y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))


cv.imshow('Pic', img)
cv.waitKey(0)
