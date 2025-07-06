import cv2
import pytesseract

def noise_removal(image): 
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations = 1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations = 1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image

def thin_font(image): 
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.bitwise_not(image) ##reinverts the image to white background
    return image

def thick_font(image): 
    import numpy as np
    image = cv2.bitwise_not(image)
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image) ##reinverts the image to white background
    return image

pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string("portastestingall.jpeg", config = '--psm 11 --oem 3 dawg')
print(text)

original = cv2.imread('portasdecente.jpeg')

### Grayscale
grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

###Binarization / Threshold
binarized = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 40)

###Invert
inverted = cv2.bitwise_not(binarized)

###Remove_noise
no_noise = noise_removal(inverted)

###Eroded image
eroded_image = thin_font(no_noise)

###Dilated image
dilated_image = thick_font(no_noise)

cv2.imwrite("portasDILATED.jpeg", dilated_image)
cv2.imwrite("portasERODED.jpeg", eroded_image)
cv2.imwrite("portas_noise.jpeg", no_noise)
cv2.imwrite("portastestingall.jpeg", inverted)
cv2.imshow('hi1',binarized)
cv2.imshow('hellotest',inverted)
cv2.imshow("noise", no_noise)
cv2.imshow("erored", eroded_image)
cv2.imshow("dilated", dilated_image)


cv2.waitKey(0)
