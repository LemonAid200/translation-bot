import pytesseract
import cv2
from os import remove
# import matplotlib.pyplot as plt
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'D:/pytesseract/tesseract.exe'



# печатаем
def extractText (img):
	image = cv2.imread(img)
	string = pytesseract.image_to_string(image)
	remove(img)
	return string