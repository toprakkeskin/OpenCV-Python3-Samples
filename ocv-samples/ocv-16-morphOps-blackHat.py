import cv2
import numpy as np

origL = cv2.imread('../data/letter-l.jpg',0)
origD = cv2.imread('../data/letter-d.jpg',0)

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((4,4),np.uint8)
kernel3 = np.ones((8,8),np.uint8)

# It's the difference between the closing of the input image and input image. 
blackhatL1 = cv2.morphologyEx(origL,cv2.MORPH_BLACKHAT,kernel1)
blackhatL2 = cv2.morphologyEx(origL,cv2.MORPH_BLACKHAT,kernel2)
blackhatL3 = cv2.morphologyEx(origL,cv2.MORPH_BLACKHAT,kernel3)

blackhatD1 = cv2.morphologyEx(origD,cv2.MORPH_BLACKHAT,kernel1)
blackhatD2 = cv2.morphologyEx(origD,cv2.MORPH_BLACKHAT,kernel2)
blackhatD3 = cv2.morphologyEx(origD,cv2.MORPH_BLACKHAT,kernel3)

cv2.imshow('L-orig',origL)
cv2.imshow('L-bh-k1',blackhatL1)
cv2.imshow('L-bh-k2',blackhatL2)
cv2.imshow('L-bh-k3',blackhatL3)

cv2.imshow('D-orig',origD)
cv2.imshow('D-bh-k1',blackhatD1)
cv2.imshow('D-bh-k2',blackhatD2)
cv2.imshow('D-bh-k3',blackhatD3)


cv2.waitKey(0)
cv2.destroyAllWindows()

