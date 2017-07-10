import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/b2.jpg')
rows,cols,ch = img.shape

p1 = np.float32([[50,50],[200,50],[50,200]])
p2 = np.float32([[60,150],[200,50],[100,250]])

M = cv2.getAffineTransform(p1,p2)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title('img')
plt.subplot(122),plt.imshow(dst),plt.title('dst')
plt.show()
