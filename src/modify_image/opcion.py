from modify_image.grayScale import grayScale

def select_opcion(opc, filename):
    
    if opc == 'Escala de grises':
        return grayScale(filename)
