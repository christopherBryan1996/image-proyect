import cv2
from PIL import Image

def threshold(filename):
    
    image = cv2.imread(filename, 0)
    blur = cv2.GaussianBlur(image, (5,5), 0)
    #gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    closed =Image.fromarray(closed).resize((200,200))
    
    return closed


