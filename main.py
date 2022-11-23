
import tkinter as tk 
from tkinter import PhotoImage, Label
from PIL import ImageTk, Image  

import sys
print(sys.executable)

root = tk.Tk()

# COULEUR DE FOND       
root.config(background="black")

# AJOUTER UN TITRE A LA FENETRE TKINTER
root.title("Starfighter")

# FIXE LA TAILLE EN PIXEL 
root.geometry("1000x1000")

# CREATION DU CANVAS 
canvasBase = tk.Canvas(root, background="black", width=700, height=500)
canvasBase.pack()

class Vaisseau:
    def __init__(self, master):
        self.master = master

        # Creation d,un widget Canvas (zone graphique)
        self.vaisseauImg = PhotoImage(file = "vaisseau1.png")
        self.labelImg = Label(self.master, i=self.vaisseauImg)
        self.labelImg.pack()

    def start(self):
        self.master.mainloop()


if __name__ == "__main__":
    app = Vaisseau(root)
    app.start()

root.mainloop()
