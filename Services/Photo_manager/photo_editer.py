import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


ran_img = np.random.randint(0, 100, (25, 3)).astype(np.float32)
result_img = np.random.randint(0, 2, (25, 1)).astype(np.float32)

red = ran_img[result_img.ravel() == 1]
blue = ran_img[result_img.ravel() == 0]
new = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(red[:, 0], red[:, 1], 100, 'r', 's')
plt.scatter(blue[:, 0], blue[:, 1], 100, 'b', 's')
plt.scatter(new[:, 0], new[:, 1], 100, 'g', 's')

# print(ran_img)
# print(result_img)
# print(red)

knn = cv.ml_KNearest.create()
knn.train(ran_img, 0, result_img)
goal = knn.findNearest(new, 3)

plt.show()
print(goal)


