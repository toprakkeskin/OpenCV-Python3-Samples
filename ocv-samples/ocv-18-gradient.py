import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../data/newspaper-sudoku.jpg',0)

#Laplacian Derivative
laplacian = cv2.Laplacian(img, cv2.CV_64F)

# Sobel operators is a joint Gausssian smoothing
# plus differentiation operation, 
# so it is more resistant to noise. 
sobelx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
plt.title('sobel x'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
plt.title('sobel y'), plt.xticks([]), plt.yticks([])

plt.show()
