import cv2
import numpy as np

img = cv2.imread('../data/book1.jpg')
ret, thresh = cv2.threshold(img,20,255,cv2.THRESH_BINARY)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret2, thresh2 = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 99, 1)

mean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 99, 1)

cv2.imshow('img', img)
cv2.imshow('threshold', thresh)
cv2.imshow('threshold2', thresh2)
cv2.imshow('gaus', gaus)
cv2.imshow('mean', mean)
cv2.waitKey(0)
cv2.destroyAllWindows()
