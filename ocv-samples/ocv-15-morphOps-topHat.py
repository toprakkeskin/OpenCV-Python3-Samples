import cv2
import numpy as np

origL = cv2.imread('../data/letter-l.jpg',0)
origD = cv2.imread('../data/letter-d.jpg',0)

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((4,4),np.uint8)
kernel3 = np.ones((8,8),np.uint8)

# It is the difference between input image and Opening of the image.
tophatL1 = cv2.morphologyEx(origL,cv2.MORPH_TOPHAT,kernel1)
tophatL2 = cv2.morphologyEx(origL,cv2.MORPH_TOPHAT,kernel2)
tophatL3 = cv2.morphologyEx(origL,cv2.MORPH_TOPHAT,kernel3)

tophatD1 = cv2.morphologyEx(origD,cv2.MORPH_TOPHAT,kernel1)
tophatD2 = cv2.morphologyEx(origD,cv2.MORPH_TOPHAT,kernel2)
tophatD3 = cv2.morphologyEx(origD,cv2.MORPH_TOPHAT,kernel3)

cv2.imshow('L-orig',origL)
cv2.imshow('L-th-k1',tophatL1)
cv2.imshow('L-th-k2',tophatL2)
cv2.imshow('L-th-k3',tophatL3)

cv2.imshow('D-orig',origD)
cv2.imshow('D-th-k1',tophatD1)
cv2.imshow('D-th-k2',tophatD2)
cv2.imshow('D-th-k3',tophatD3)


cv2.waitKey(0)
cv2.destroyAllWindows()

