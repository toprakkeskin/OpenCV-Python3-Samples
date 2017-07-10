import cv2
import numpy as np

origL = cv2.imread('../data/letter-l.jpg',0)
origD = cv2.imread('../data/letter-d.jpg',0)

kernel1 = np.ones((2,2),np.uint8)
kernel2 = np.ones((4,4),np.uint8)
kernel3 = np.ones((8,8),np.uint8)

# Closing is reverse of Opening, Dilation followed by Erosion. 
# It is useful in closing small holes inside the foreground 
# objects, or small black points on the object. 
closingL1 = cv2.morphologyEx(origL,cv2.MORPH_CLOSE,kernel1)
closingL2 = cv2.morphologyEx(origL,cv2.MORPH_CLOSE,kernel2)
closingL3 = cv2.morphologyEx(origL,cv2.MORPH_CLOSE,kernel3)

closingD1 = cv2.morphologyEx(origD,cv2.MORPH_CLOSE,kernel1)
closingD2 = cv2.morphologyEx(origD,cv2.MORPH_CLOSE,kernel2)
closingD3 = cv2.morphologyEx(origD,cv2.MORPH_CLOSE,kernel3)

cv2.imshow('L-orig',origL)
cv2.imshow('L-clo-k1',closingL1)
cv2.imshow('L-clo-k2',closingL2)
cv2.imshow('L-clo-k3',closingL3)

cv2.imshow('D-orig',origD)
cv2.imshow('D-clo-k1',closingD1)
cv2.imshow('D-clo-k2',closingD2)
cv2.imshow('D-clo-k3',closingD3)


cv2.waitKey(0)
cv2.destroyAllWindows()

