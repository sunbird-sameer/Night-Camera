import cv2
import numpy as np

image = cv2.imread('dark.png')
cv2.imshow("Image",image)

alpha_beta = 3.5

added_image = cv2.addWeighted(image,alpha_beta,image,alpha_beta,0)

cv2.imshow("Brightend Image", added_image)

