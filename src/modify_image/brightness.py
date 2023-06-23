import cv2
from PIL import Image

def brightness(filename):
    
    img = cv2.imread(filename, 0)
    blur = cv2.GaussianBlur(img, (5,5), 0)
    contrast_adjusted = cv2.convertScaleAbs(blur, alpha=1.5, beta=25)
    contrast_adjusted =Image.fromarray(contrast_adjusted).resize((200,200))

    return contrast_adjusted
