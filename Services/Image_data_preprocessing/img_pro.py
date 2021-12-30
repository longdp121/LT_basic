import cv2 as cv
import numpy as np
import csv
from numpy.core.fromnumeric import reshape
import base64
import json

class photo_pro:
    def __init__(self):
        pass

    def open_img(self):
        data_dict = {}
        path_list = ['pic/IMG_0669.JPG', 'pic/picture_test.jpg', 'pic/balls.png', 'pic/card_game.jpg', 'pic/face.jpg', 'pic/faces.jpg', 'pic/hoa_con_small.jpg']
        for path in path_list:
            img = cv.imread(path)
            _, buffer = cv.imencode(f'{path[-4:]}', img)
            img_text = str(base64.b64encode(buffer))
            data_dict[path[4:-4]] = img_text[2:-1]
        
        return data_dict

    def save_img(self):
        for path in self.open_img().keys():
            with open(f'dataset/{path}.csv', 'w', newline = '') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([path, self.open_img()[path]])
  
    def decode_img(self, name):
        csv.field_size_limit(100000000)
        with open(f'dataset/{name}.csv', 'r', newline = '') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                row = row
        img_bytes = bytes(row[1], 'utf8')
        buffer = base64.b64decode(img_bytes)
        img_arr = np.frombuffer(buffer, dtype = np.uint8)
        img = cv.imdecode(img_arr, cv.IMREAD_COLOR)
        cv.imshow(f'{name}', img)
        cv.waitKey(0)      
        

    def main(self):
        #self.open_img()
        #self.save_img()
        self.decode_img('IMG_0669')
        print('Class')

app = photo_pro()

if __name__ == '__main__':
    app.main()