import cv2
import numpy as np

img1 = cv2.imread('../data/3D-Matplotlib.png')
img2 = cv2.imread('../data/mainlogo.png')

rows,cols,channels = img2.shape
roi = img1[100:rows+100,:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

img3_bg = cv2.bitwise_and(roi, roi, mask=mask)
img3 = cv2.bitwise_and(img2, img3_bg, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[100:rows+100,:cols] = dst

cv2.imshow('img',img1)
cv2.imshow('mask',mask)
cv2.imshow('m_inv',mask_inv)
cv2.imshow('im1bg',img1_bg)
cv2.imshow('im2fg',img2_fg)
cv2.imshow('im3bg',img3_bg)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
