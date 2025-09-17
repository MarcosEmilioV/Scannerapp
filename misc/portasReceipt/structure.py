import cv2
import numpy as np
import pytesseract

def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    print (len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("temp/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle
# Rotate the image around its center
def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage

def deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)

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
    ##originally there was a bitwise not here
    kernel = np.ones((2,2), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    image = cv2.bitwise_not(image) ##reinverts the image to white background
    return image

def remove_borders(image):
    contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y+h, x:x+w]
    return (crop)




pytesseract.pytesseract.tesseract_cmd= 'C:/Program Files/Tesseract-OCR/tesseract.exe'
data = pytesseract.image_to_data("finished_portasimage.jpeg", config = '--psm 11 --oem 3 ', output_type = pytesseract.Output.DICT)




for i, word in enumerate(data['text']):
    if word.strip():  # ignore empty OCR hits
        print(f"{word} (conf={data['conf'][i]}, x={data['left'][i]}, y={data['top'][i]})")

original = cv2.imread('portasdecente.jpeg')
testDeskew = cv2.imread("testDESKEW.png")

### Grayscale
grayscale = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

###Binarization / Threshold
binarized = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 25, 40)

###No Borders
no_borders = remove_borders(binarized) ##seems like it can only use a white backgroud image thats why binarized althought inverted better

##inverted 
inverted = cv2.bitwise_not(no_borders)

###Remove_noise
no_noise = noise_removal(inverted)

###Eroded image
eroded_image = thin_font(no_noise)

###Dilated image
dilated_image = thick_font(no_noise)

###Inverted-Dilation
inverted_dilation = thick_font(inverted) ##Here, neither erotion nor noise removal has been applied.


##Targeted Dilation Bottom Part
height = inverted_dilation.shape[0]
bottom_start = int(height * 0.66) 
invertioncheck = cv2.bitwise_not(inverted_dilation)
top_zone = inverted_dilation[:bottom_start, :] ##image here is in white background
bottom_zone = invertioncheck[bottom_start: , :] ##image here is in black background 
kernel = np.ones((2,2), np.uint8)

targeted_dilation = cv2.dilate(bottom_zone, kernel, iterations = 1) ##takes black background white letters to dilate them
reversedilation = cv2.bitwise_not(targeted_dilation) ##reverse dilation again cause i think it makes more sense to have all the joined image in white background
finished_image = np.concatenate((top_zone, reversedilation), axis = 0) ##now with the finished image i should make more things to it, probably quiet down noise since there are a lot of pixels

##Detecting Contours 
blur = cv2.GaussianBlur(grayscale, (5,5), 0)
edges = cv2.Canny(blur, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)
for cnt in contours:
    # Approximate contour shape
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

    # If it's a quadrilateral (4 points), we may have found the receipt
    if len(approx) == 4:
        receipt_contour = approx
        break

# Apply perspective transform to "flatten" the receipt
pts = receipt_contour.reshape(4,2)
# Order points (top-left, top-right, bottom-right, bottom-left)
rect = np.zeros((4,2), dtype="float32")
s = pts.sum(axis=1)
rect[0] = pts[np.argmin(s)]   # top-left
rect[2] = pts[np.argmax(s)]   # bottom-right
diff = np.diff(pts, axis=1)
rect[1] = pts[np.argmin(diff)] # top-right
rect[3] = pts[np.argmax(diff)] # bottom-left

# Compute width & height
(widthA, widthB) = [np.linalg.norm(rect[2]-rect[3]), np.linalg.norm(rect[1]-rect[0])]
(heightA, heightB) = [np.linalg.norm(rect[1]-rect[2]), np.linalg.norm(rect[0]-rect[3])]
maxWidth, maxHeight = int(max(widthA, widthB)), int(max(heightA, heightB))

dst = np.array([[0,0],[maxWidth-1,0],[maxWidth-1,maxHeight-1],[0,maxHeight-1]], dtype="float32")
M = cv2.getPerspectiveTransform(rect, dst)
warped = cv2.warpPerspective(original, M, (maxWidth, maxHeight))

# Save the cropped/warped receipt

###DESKEWED image
fixed = deskew(testDeskew)
cv2.imwrite("receipt_cropped.jpg", warped)
cv2.imwrite("portasEDGES.jpeg", edges)
cv2.imwrite("finished_portasimage.jpeg", finished_image)
cv2.imwrite("testDESKEW.jpeg", fixed)
cv2.imwrite("portasDILATED.jpeg", dilated_image)
cv2.imwrite("portasERODED.jpeg", eroded_image)
cv2.imwrite("portas_binarized.jpeg", binarized)
cv2.imwrite("portas_inverted.jpeg", inverted)
cv2.imwrite("portas_noise.jpeg", no_noise)
cv2.imwrite("portasNOBORDERS.jpeg", no_borders)
cv2.imwrite("portasInverted_Dilated.jpeg", inverted_dilation)
cv2.imwrite("portas_Targeted_Dilated.jpeg", targeted_dilation)


cv2.waitKey(0)
