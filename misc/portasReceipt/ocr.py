import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string("perro.jpeg", config = '--psm 11 --oem 3 dawg')
print(text)

def preprocess_image_for_ocr(image_path, output_path):
    
    image = cv2.imread(r'C:\Users\Lenovo\scannerapp\misc\portasdecente.jpeg')
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    something = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

    cv2.imwrite(output_path, something)
    
    return something
    
preprocess_image_for_ocr("portasdecente.jpeg", "perro.jpeg")