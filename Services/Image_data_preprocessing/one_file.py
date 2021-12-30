import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import reshape
import base64
from pymongo import MongoClient

HOST = 'localhost'
PORT = 27017

client = MongoClient(HOST, PORT)
db = client['local']
collection = db['image_data']

class photo_pro:
    def __init__(self):
        pass

    def open_img(self):
        data_dict = {}
        # path_list = ['pic/IMG_0669.JPG', 'pic/picture_test.jpg', 'pic/balls.png', 'pic/card_game.jpg', 'pic/face.jpg', 'pic/faces.jpg', 'pic/hoa_con_small.jpg']
        path_list = ['pic/IMG_0669.JPG']
        for path in path_list:
            img = cv.imread(path)
            _, buffer = cv.imencode(f'{path[-4:]}', img)
            print(type(buffer))
            img_text = str(base64.b64encode(buffer))
            data_dict[path[4:-4]] = img_text[2:-1]
        return data_dict

    def save_img(self):
        post_list = []
        for key in self.open_img().keys():
            post = {'_id': key, 'img_data': self.open_img()[key]}
            post_list.append(post)
        collection.insert_many(post_list)
  
    def decode_img(self, name):
        result = collection.find_one({'_id': f'{name}'})
        found = result['img_data']
        img_bytes = bytes(found, 'utf8')
        buffer = base64.b64decode(img_bytes)
        img_arr = np.frombuffer(buffer, dtype = np.uint8)
        img = cv.imdecode(img_arr, cv.IMREAD_COLOR)
        cv.imshow(f'{name}', img)
        cv.waitKey(0)      
        

    def main(self):
        self.open_img()
        #self.save_img()
        #self.decode_img('hoa_con_small')
        print('Class')

app = photo_pro()

if __name__ == '__main__':
    app.main()