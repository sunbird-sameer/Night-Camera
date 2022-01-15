import cv2
import numpy as np

image = cv2.imread('dark.png')
cv2.imshow("Image",image)

alpha_beta = 3.5

added_image = cv2.addWeighted(image,alpha_beta,image,alpha_beta,0)
added_image = cv2.GaussianBlur(added_image,(5,5),cv2.BORDER_DEFAULT)
added_image = cv2.detailEnhance(added_image, sigma_s=1, sigma_r=10000)

cv2.imshow("Brightend Image", added_image)
cv2.imwrite("Brightend Image.png", added_image)

