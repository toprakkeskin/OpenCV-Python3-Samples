import numpy as np
import cv2

img = cv2.imread('../data/owl.jpg', cv2.IMREAD_COLOR)

# Renkler BGR seklinde
cv2.line(img, (10,10), (150,50), (200,255,0), 5)
cv2.rectangle(img, (10,10), (190,80), (0,0,200), 5)
cv2.circle(img, (100,67), 60, (0,200,0), 5)

points = np.array([ 
[65,90],[76,101],[95,111],[123,100],[109,83],[96,94],[82,75]
				 ],np.int32)
cv2.polylines(img,[points], True, (0,255,255), 2)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


