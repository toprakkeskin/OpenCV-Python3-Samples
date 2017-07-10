import cv2
import numpy as np

img = cv2.imread('../data/owl.jpg',0)
rows,cols = img.shape

M = np.float32([[1,0,50],[0,1,60]])
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows(0)


