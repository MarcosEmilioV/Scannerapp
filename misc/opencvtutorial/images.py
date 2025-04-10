import cv2

k_size = 15

image = cv2.imread('noisy.png')
grayscale = cv2.medianBlur(image, k_size)

cv2.imshow('hi',grayscale)
cv2.waitKey(0)