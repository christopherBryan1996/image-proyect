from modify_image.grayScale import grayScale
from modify_image.blurFilter import blurFilter
from modify_image.threshold import threshold
from modify_image.brightness import brightness
from modify_image.canny import canny
from modify_image.laplacian import laplacian
from modify_image.borders import borders

def select_opcion(opc, filename):
    
    if opc == 'Escala de grises':
        return grayScale(filename)
    if opc == 'Filtrado suavizado':
        return blurFilter(filename)
    if opc == 'Umbralización':
        return threshold(filename)
    if opc == 'Brillo':
        return brightness(filename)
    if opc == 'Canny':
        return canny(filename)
    if opc == 'Laplaciano':
        return laplacian(filename)
    if opc == 'Contornos':
        return borders(filename)