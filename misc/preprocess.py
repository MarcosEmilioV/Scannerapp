import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string("portastestingall.jpeg", config = '--psm 11 --oem 3 dawg')
print(text)

original = cv2.imread('portasdecente.jpeg')

### Grayscale
grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

###Binarization / Threshold
binarized = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 40)

###Invert
inverted = cv2.bitwise_not(binarized)

cv2.imwrite("portastestingall.jpeg", inverted)
cv2.imshow('hi1',binarized)
cv2.imshow('hellotest',inverted)





cv2.waitKey(0)