import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string(r"C:\Users\Lenovo\scannerapp\misc\perro.jpeg", config = '--psm 11 --oem 3 dawg')
print(text)

k_size = 15

image = cv2.imread(r'C:\Users\Lenovo\scannerapp\misc\portasdecente.jpeg')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img_edge = cv2.Canny(grayscale, 150, 200)
something = cv2.adaptiveThreshold(img_edge, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)


cv2.imshow('hi',image)
cv2.imshow('processed', something)
cv2.waitKey(0)