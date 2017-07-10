#!/usr/bin/python3
import cv2
import numpy as np

img = cv2.imread('../data/puff-low.png')
img2 = cv2.imread('../data/ducky-low.jpg')

gaussian = cv2.GaussianBlur(img,(19,19),0)
median = cv2.medianBlur(img2,5)

cv2.imshow('img',img)
cv2.imshow('gaussian',gaussian)
cv2.imshow('img2',img2)
cv2.imshow('median',median)

cv2.waitKey(0)
cv2.destroyAllWindows()

