import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
def imToString(Image_Area):
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    cap = ImageGrab.grab(bbox =Image_Area)
    # Converted the image to monochrome for it to be easily 
    # read by the OCR and obtained the output String.
    tesstr = pytesseract.image_to_string(
    cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),lang ='eng')
    print(tesstr)

if __name__=='__main__':
    imToString((570,389,1275,444))