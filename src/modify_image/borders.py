import cv2
from PIL import Image

def borders(filename):
    
    imagen = cv2.imread(filename, 0)
    _, threshold = cv2.threshold(imagen, 100, 1, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_with_contours = cv2.drawContours(imagen.copy(), contours, -1, (0, 255, 0), 2)
    

    
    #borders = cv2.Laplacian(image_with_contours, cv2.CV_64F)
    borders =Image.fromarray(cv2.cvtColor(image_with_contours, cv2.COLOR_BGR2RGB)).resize((200,200))

    return borders