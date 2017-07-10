import numpy as np
import cv2

img = cv2.imread('../data/b2.jpg',cv2.IMREAD_COLOR)


img[55,55] = [255,255,255]
px1 = img[55,55]
print('px1=')
print(px1)

#ROI = Region of Image
roi = img[100:103, 85:88]
print('roi=')
print(roi)

# region change
img[50:100, 50:100] = [255,255,255]

# copy same size region
#[100:200,40:115]
face1 = img[40:115,100:200]
print (face1.shape[0])
print (face1.shape[1])
img[20:face1.shape[0]+20,270:face1.shape[1]+270] = face1


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
