import cv2
import numpy as np

origL = cv2.imread('../data/letter-l.jpg',0)
origD = cv2.imread('../data/letter-d.jpg',0)

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((4,4),np.uint8)
kernel3 = np.ones((8,8),np.uint8)

erosionL1 = cv2.erode(origL,kernel1,iterations = 1)
erosionL2 = cv2.erode(origL,kernel2,iterations = 1)
erosionL3 = cv2.erode(origL,kernel3,iterations = 1)

erosionD1 = cv2.erode(origD,kernel1,iterations = 1)
erosionD2 = cv2.erode(origD,kernel2,iterations = 1)
erosionD3 = cv2.erode(origD,kernel3,iterations = 1)

cv2.imshow('L-orig',origL)
cv2.imshow('L-er-k1',erosionL1)
cv2.imshow('L-er-k2',erosionL2)
cv2.imshow('L-er-k3',erosionL3)

cv2.imshow('D-orig',origD)
cv2.imshow('D-er-k1',erosionD1)
cv2.imshow('D-er-k2',erosionD2)
cv2.imshow('D-er-k3',erosionD3)


cv2.waitKey(0)
cv2.destroyAllWindows()

