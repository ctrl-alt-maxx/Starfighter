
import tkinter as tk 
from PIL import Image

root = tk.Tk()

# COULEUR DE FOND
root.config(background="white")

# AJOUTER UN TITRE A LA FENETRE TKINTER
root.title("Starfighter")

# FIXE LA TAILLE EN PIXEL 
root.geometry("1000x1000")

# CREATION DU CANVAS 
canvasBase = tk.Canvas(root, background="black", width=700, height=500)
canvasBase.pack()

# Vaisseau 
vaisseau = Image.open("./images/Vaisseau.jpg")
vaisseau.PIL.Image.show()

