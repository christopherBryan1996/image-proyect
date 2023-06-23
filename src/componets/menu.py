from tkinter import ttk, Menu, messagebox, Canvas
import sys # para salir de la aplicacion
from tkinter import filedialog as fd
from PIL import Image,ImageTk
import os
from modify_image.opcion import select_opcion


this_window_global=''
control_tab=""
count_modify=0
filename = ""
lbl_image= ""
lbl_image2=""
combo=""
canvas=""

def modify_image():
    global filename
    global canvas
    global lbl_image2

    if combo.get()=="":
        messagebox.showerror("No selecciono", "Por favor selecciona algo de la lista")
    else:
        imageModify = select_opcion(combo.get(), filename)
        imageModify = ImageTk.PhotoImage(imageModify)
        lbl_image2.config(image=imageModify)
        print(pws)
        print(imageModify)
        

def file_open():
    global filename
    global this_window_global
    global lbl_image
    #solo tomamos estos tipos de archivos 
    filetype=(
        ("png", "*.png"),
        ("jpg", "*.jpg")
    )
    #tomamos la ruta 
    filename = fd.askopenfilename( title="Seleccione archivo", filetypes=filetype)
    image = ImageTk.PhotoImage(Image.open(filename).resize((200,200)))
    lbl_image.config(image=image)
    print(filename)
    print(pws)


def tab_modify():
    global control_tab
    global count_modify
    global lbl_image
    global lbl_image2
    global filename
    global combo
    global canvas

    if control_tab == "":
        control_tab = ttk.Notebook(this_window_global)
        tab = ttk.Frame(control_tab)
        control_tab.add(tab, text="Modificar imagen")
        control_tab.pack(fill='both') #rellena todo el espacio

        txt_inf = ttk.Label(tab,text='Vamos a cargar lo necesario para modificar tu imagen')
        txt_inf.grid(row=0,column=0, pady=10)

        txt_img = ttk.Label(tab,text='Inserte su imagen')
        txt_img.grid(row=1,column=0)

        btn_insert = ttk.Button(tab,text="Abrir archivo", command=file_open)
        btn_insert.grid(row=3, column=0)

        pwd=os.getcwd()
        filename=f'{pwd}\src\Img\descarga (2).jfif'
        image = Image.open(filename)
        image = ImageTk.PhotoImage(image)

        lbl_image = ttk.Label(tab, image=image)
        lbl_image.grid(row=4,column=0)

        txt_img = ttk.Label(tab,text='Seleccione su metodo')
        txt_img.grid(row=5,column=0)

        combo = ttk.Combobox(tab,
            state="readonly",
            values=["Escala de grises", "Filtrado suavizado", "Umbralización", "Brillo", "Canny", "Laplaciano", "Contornos"]#Aqui se agregan lo que estara en la lista
        )
        combo.grid(row=6,column=0)

        btn_modify = ttk.Button(tab,text="Enchulame la imagen", command=modify_image)
        btn_modify.grid(row=7, column=0)

        lbl_image2 = ttk.Label(tab)
        lbl_image2.grid(row=8,column=0)

        print(pws)
        
    else:
        control_tab.destroy()
        control_tab=""
        tab_modify()
 

def exit():
    this_window_global.quit()
    this_window_global.destroy()
    sys.exit()

def menu(window):
    menu_global= Menu(window)
    global this_window_global
    this_window_global= window
    #agregamos el menu de modificar al global 
    #tearoff  quita una linea q se ve añ principio de este menu
    menu_modify = Menu(menu_global, tearoff=0)
    menu_modify.add_command(label='Modificar Imagen', command=tab_modify)
    menu_modify.add_separator()
    menu_modify.add_command(label='Salir', command=exit)

    menu_global.add_cascade(menu=menu_modify,label='Archivo')

    window.config(menu=menu_global)