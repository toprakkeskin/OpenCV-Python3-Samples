import cv2
import numpy as np

img = cv2.imread('../data/owl.jpg')
# Preferable interpolation methods are cv2.INTER_AREA for shrinking 
# and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming. 
# By default, interpolation method used is cv2.INTER_LINEAR 
# for all resizing purposes.
res = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

#OR
#height, width = img.shape[:2]
#res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('img',img)
cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
