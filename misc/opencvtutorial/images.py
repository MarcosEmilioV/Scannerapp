import cv2

k_size = 15

image = cv2.imread(r'C:\Users\Lenovo\scannerapp\misc\portasdecente.jpeg')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
something = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)


cv2.imshow('hi',image)
cv2.imshow('processed', something)
cv2.waitKey(0)