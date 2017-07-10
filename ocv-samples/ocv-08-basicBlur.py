#!/usr/bin/python3
import cv2
import numpy as np


img = cv2.imread('../data/puff-low.png')
img2 = cv2.imread('../data/ducky-low.jpg')

blured = cv2.blur(img,(20,20))
blured2 = cv2.blur(img2,(7,7))


cv2.imshow('img',img)
cv2.imshow('blured',blured)
cv2.imshow('img2',img2)
cv2.imshow('blured2',blured2)
cv2.waitKey(0)
cv2.destroyAllWindows()


