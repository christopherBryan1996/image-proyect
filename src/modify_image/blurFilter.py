import cv2
from PIL import Image

def blurFilter(filename):
    
    image = cv2.imread(filename, 0)
    blur_image =Image.fromarray(cv2.blur(image, (5,5), 0)).resize((200,200))
    
    return blur_image