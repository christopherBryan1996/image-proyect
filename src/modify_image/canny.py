import cv2
from PIL import Image

def canny(filename):
    
    imagen = cv2.imread(filename, 0)
    canny = cv2.Canny(imagen, 100, 200)
    canny =Image.fromarray(canny).resize((200,200))

    return canny