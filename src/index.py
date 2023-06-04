import tkinter as tk
from componets.menu import menu

window = tk.Tk()

width=600
higt=800

window.title("Mejora tu imagen de imagenes jajaja")
window.iconbitmap('src/img/rubocop.ico')
window.geometry(f'{higt}x{width}')

menu(window)

window.mainloop()