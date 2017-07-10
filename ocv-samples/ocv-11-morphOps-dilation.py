import cv2
import numpy as np

origL = cv2.imread('../data/letter-l.jpg',0)
origD = cv2.imread('../data/letter-d.jpg',0)

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((4,4),np.uint8)
kernel3 = np.ones((8,8),np.uint8)

dilationL1 = cv2.dilate(origL,kernel1,iterations = 1)
dilationL2 = cv2.dilate(origL,kernel2,iterations = 1)
dilationL3 = cv2.dilate(origL,kernel3,iterations = 1)

dilationD1 = cv2.dilate(origD,kernel1,iterations = 1)
dilationD2 = cv2.dilate(origD,kernel2,iterations = 1)
dilationD3 = cv2.dilate(origD,kernel3,iterations = 1)

cv2.imshow('L-orig',origL)
cv2.imshow('L-dil-k1',dilationL1)
cv2.imshow('L-dil-k2',dilationL2)
cv2.imshow('L-dil-k3',dilationL3)

cv2.imshow('D-orig',origD)
cv2.imshow('D-dil-k1',dilationD1)
cv2.imshow('D-dil-k2',dilationD2)
cv2.imshow('D-dil-k3',dilationD3)


cv2.waitKey(0)
cv2.destroyAllWindows()

