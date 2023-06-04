import cv2
from PIL import Image

def grayScale(filename):
    
    image = cv2.imread(filename)
    gray_image =Image.fromarray( cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)).resize((200,200))
    
    return gray_image