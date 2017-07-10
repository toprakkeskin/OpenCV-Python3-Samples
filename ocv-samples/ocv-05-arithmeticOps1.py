import cv2
import numpy as np

img1 = cv2.imread('../data/3D-Matplotlib.png')
img2 = cv2.imread('../data/mainsvmimage.png')


add = img1 + img2

# pixel degelerini birbirine ekler
# renk degerleri cok yuksek olacagindan
# beyaza yaklasiyor.(255,255,255)
add2 = cv2.add(img1,img2)

#
weighted = cv2.addWeighted(img1,0.6, img2, 0.4, 0)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
cv2.imshow('add',add)
cv2.imshow('add2',add2) 
cv2.imshow('weighted',weighted) 
cv2.waitKey(0)
cv2.destroyAllWindows()
