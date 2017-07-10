import cv2
import numpy as np

origL = cv2.imread('../data/letter-l.jpg',0)
origD = cv2.imread('../data/letter-d.jpg',0)

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((4,4),np.uint8)
kernel3 = np.ones((8,8),np.uint8)

# Opening is just another name of erosion followed by dilation. 
# It is useful in removing noise,
openingL1 = cv2.morphologyEx(origL,cv2.MORPH_OPEN,kernel1)
openingL2 = cv2.morphologyEx(origL,cv2.MORPH_OPEN,kernel2)
openingL3 = cv2.morphologyEx(origL,cv2.MORPH_OPEN,kernel3)

openingD1 = cv2.morphologyEx(origD,cv2.MORPH_OPEN,kernel1)
openingD2 = cv2.morphologyEx(origD,cv2.MORPH_OPEN,kernel2)
openingD3 = cv2.morphologyEx(origD,cv2.MORPH_OPEN,kernel3)

cv2.imshow('L-orig',origL)
cv2.imshow('L-op-k1',openingL1)
cv2.imshow('L-op-k2',openingL2)
cv2.imshow('L-op-k3',openingL3)

cv2.imshow('D-orig',origD)
cv2.imshow('D-op-k1',openingD1)
cv2.imshow('D-op-k2',openingD2)
cv2.imshow('D-op-k3',openingD3)


cv2.waitKey(0)
cv2.destroyAllWindows()

