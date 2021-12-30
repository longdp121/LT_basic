import cv2 as cv
import numpy as np
import base64
from pymongo import MongoClient

HOST = 'localhost'
PORT = 27017

client = MongoClient(HOST, PORT)
db = client['ocr_database']
collection = db['db']

def get_filename(file_name, method):
    
    pass

def show_img(file, file_name):
    buffer = np.fromfile(file, np.uint8)
    print(type(buffer))
    img_text = str(base64.b64encode(buffer))
    post = {'file_name': file_name, 'data': img_text[2:-1]}
    collection.insert_one(post)
    # img = cv.imdecode(np_img, cv.IMREAD_COLOR)
    # cv.imshow('p', img)
    # cv.waitKey(0)