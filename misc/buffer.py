import pytesseract
from PIL import Image, ImageFilter, ImageEnhance

pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files/Tesseract-OCR/tesseract.exe'

text = pytesseract.image_to_string("grayscale_image.jpeg", config = '--psm 11 --oem 3 dawg')
print(text)

image = Image.open('portasdecente.jpeg')
grayscale = image.convert('L')
enhancer = ImageEnhance.Contrast(grayscale)
grayscale = enhancer.enhance(2.0)
grayscale = grayscale.filter(ImageFilter.SHARPEN)

grayscale.save('grayscale_image.jpeg')



