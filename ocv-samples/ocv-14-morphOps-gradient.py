import cv2
import numpy as np

origL = cv2.imread('../data/letter-l.jpg',0)
origD = cv2.imread('../data/letter-d.jpg',0)

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((4,4),np.uint8)
kernel3 = np.ones((8,8),np.uint8)

# It is the difference between dilation and erosion of an image.
gradientL1 = cv2.morphologyEx(origL,cv2.MORPH_GRADIENT,kernel1)
gradientL2 = cv2.morphologyEx(origL,cv2.MORPH_GRADIENT,kernel2)
gradientL3 = cv2.morphologyEx(origL,cv2.MORPH_GRADIENT,kernel3)

gradientD1 = cv2.morphologyEx(origD,cv2.MORPH_GRADIENT,kernel1)
gradientD2 = cv2.morphologyEx(origD,cv2.MORPH_GRADIENT,kernel2)
gradientD3 = cv2.morphologyEx(origD,cv2.MORPH_GRADIENT,kernel3)

cv2.imshow('L-orig',origL)
cv2.imshow('L-gra-k1',gradientL1)
cv2.imshow('L-gra-k2',gradientL2)
cv2.imshow('L-gra-k3',gradientL3)

cv2.imshow('D-orig',origD)
cv2.imshow('D-gra-k1',gradientD1)
cv2.imshow('D-gra-k2',gradientD2)
cv2.imshow('D-gra-k3',gradientD3)


cv2.waitKey(0)
cv2.destroyAllWindows()

