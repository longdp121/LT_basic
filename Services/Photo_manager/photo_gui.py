import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.type_check import imag


path = 'pic/picture_test.jpg'

class photos():
    def __init__(self):
        pass
    
    def open_file(self):
        #files_name = ['pic/face.jpg', 'pic/faces.jpg', 'pic/card_game.jpg', 'pic/minion_test.jpg', 'pic/picture_test.jpg']
        files_name = 'pic/minion_test.jpg'
        # temp_dict = {}
        # for file in files_name:
        #     file_name = str(file[4:])
        #     file_name = str(file_name[:-4])
        #     img = cv.imread(file)
        #     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        #     b, g, r = cv.split(img)
        #     temp_dict.update({file_name : (gray, b, g, r)})
        # return temp_dict
        #img = cv.imread(files_name)
        img = cv.imread(files_name)
        b, g, r = cv.split(img)
        return b

    def show_img(self):
        print(self.open_file().shape)
        print(self.open_file().ndim)
        print(self.open_file())
        print(self.open_file().dtype)
        np.savetxt('save-csv.csv', self.open_file())
        cv.imshow('Pic', self.open_file())
        cv.waitKey(0)
    
    def img_back(self, name):
        img = np.loadtxt(name)
        cv.imshow('Pic', img)
        cv.waitKey(0)


    def save_npz(self):
        for file in list(self.open_file().keys()):
            np.savez(f'dataset/{file}', gray = self.open_file().get(file)[0],
            b = self.open_file().get(file)[1],
            g = self.open_file().get(file)[2],
            r = self.open_file().get(file)[3])
            pass

    def open_npz(self, name):
        img = np.load(f'dataset/{name}')
        return (img['gray'], img['b'], img['g'], img['r'])

    def gray_hist(self, name):
        gray_hist = cv.calcHist([self.open_npz(name)[0]], [0], None, [256], [0, 256])
        plt.figure()
        plt.title('Gray histogram')
        plt.xlabel('Bins')
        plt.ylabel('Num of pixel')
        plt.plot(gray_hist)
        plt.show()
        
    def bgr_hist(self, name):
        plank = np.zeros(self.open_npz(name)[0].shape[:2], dtype = np.uint8)
        blue = cv.merge([self.open_npz(name)[1], plank, plank])
        green = cv.merge([plank, self.open_npz(name)[2], plank])
        red = cv.merge([plank, plank, self.open_npz(name)[3]])
        b_hist = cv.calcHist([blue], [0], None, [256], [0, 256])
        g_hist = cv.calcHist([green], [1], None, [256], [0, 256])
        r_hist = cv.calcHist([red], [2], None, [256], [0, 256])
        plt.figure()
        plt.title('BGR histogram')
        plt.xlabel('Bins')
        plt.ylabel('Num of pixel')
        plt.plot(b_hist, color = 'b')
        plt.plot(g_hist, color = 'g')
        plt.plot(r_hist, color = 'r')
        plt.show()
    
    def return_image(self, name):
        origin_image = cv.merge([self.open_npz(name)[1], self.open_npz(name)[2], self.open_npz(name)[3]])
        cv.imshow('Test', origin_image)
        cv.waitKey(0)

    def main(self):
        # self.open_file()
        # self.show_img()
        self.img_back('save-csv.csv')
        #self.open_npz('hoa_con_small.npz')
        #self.arr_to_img()
        #self.save_npz()
        #self.gray_hist('picture_test.npz')
        #self.return_image('picture_test.npz')
        #self.gray_hist('in 2.npz')
        #self.bgr_hist('minion_test.npz')
        #np.savetxt('dataset/save_file.csv', self.split_colors()[2])
        #np.savez_compressed('dataset/save.npz', self.split_colors()[0])
        # dict_data = load('dataset/save.npz')
        # data = dict_data['arr_0']
        #np.savez_compressed('dataset/save.npz', data, self.split_colors()[1])
        # np.savez_compressed('dataset/save.npz', self.split_colors()[1])
        # dict_data = load('dataset/save.npz')
        # data = dict_data['arr_0']
        # print(self.split_colors()[0])
        # print('and')
        # print(data)
        # print(dict_data['array_0'])
        # print(dict_data['array_1'])
        # print(dict_data['array_2'])
        
        # temp_list = []
        # for arr in self.split_colors():
        #     brand_img = Image.fromarray(arr)
        #     temp_list.append(brand_img)
        # temp_list = tuple(temp_list)
        # print(temp_list)
        # comback_img = Image.merge('RGB', temp_list)
        # print(comback_img)
        #comback_img.show()
        # cv.imshow('Test', comback_img)
        # cv.waitKey(0)


        # cols = []
        # for col in self.split_colors():
        #     cols.append(col)
        # cols = tuple(cols)
        # comback_img = Image.merge('RGB', cols)
        # cv.imshow('Tests', comback_img)
        # cv.waitKey(0)
        # color_tuple = self.split_colors()
        # cols = []
        # for col in color_tuple:
        #     cols.append(col)
        # comback_img = cv.merge(cols)

        # cv.imshow('Back', comback_img)
        # cv.imshow('H', self.to_gray())
        # cv.waitKey(0)

        print('Class')

app = photos()

if __name__ == '__main__':
    app.main()