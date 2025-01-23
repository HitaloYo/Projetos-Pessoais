import tkinter as tk
from tk import *

#criar janela
root = tk.Tk()
titulo = "Excel Reader and Resumer"

#Dimensões da janela
largura = 800
altura = 600

#Dimensões da Tela (user)
tela_altura = root.winfo_screenheight()
tela_largura = root.winfo_screenwidth()

#centralizando janela
posY = (tela_altura // 2 ) - (altura // 2)
posX = (tela_largura // 2) - (largura // 2)

#definindo titulo e dimensões da janela
root.title(f"{titulo}")
root.geometry(f"{largura}x{altura}+{posX}+{posY}")

#loop da janela
root.mainloop()

