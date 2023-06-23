import cv2
from PIL import Image

def laplacian(filename):
    
    imagen = cv2.imread(filename, 0)
    laplacian = cv2.Laplacian(imagen, cv2.CV_64F)
    laplacian =Image.fromarray(laplacian).resize((200,200))

    return laplacian