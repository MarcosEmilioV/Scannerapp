import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files/Tesseract-OCR/tesseract.exe'
text = pytesseract.image_to_string("perro.jpeg", config = '--psm 11 --oem 3 dawg')
print(text)

def preprocess_image_for_ocr(image_path, output_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    clahe = cv2.createCLAHE(clipLimit =2.5, tileGridSize = (8,8))
    contrast_enhanced = clahe.apply(gray)

    kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    sharpened = cv2.filter2D(contrast_enhanced, -2, kernel)

    

    cv2.imwrite(output_path, sharpened)
    return sharpened
    
preprocess_image_for_ocr("portasdecente.jpeg", "perro.jpeg")