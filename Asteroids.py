import math
import tkinter as tk
from tkinter import ttk ,BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y   
from tkinter import *
from PIL import Image, ImageTk


root = tk.Tk()

# COULEUR DE FOND       
root.config(background="black")

# AJOUTER UN TITRE A LA FENETRE TKINTER
root.title("Starfighter")

# FIXE LA TAILLE EN PIXEL 
root.geometry("5000x5000")

frame = Frame(root)
frame.pack()

canvasBase = tk.Canvas(root, background="black", width=800, height=1000, highlightthickness=1, highlightbackground="red", relief='ridge')
canvasBase.pack()

class Asteroide:
    imgAsteroide = Image.open("asteroide.png")
    new = imgAsteroide.resize((60, 60), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(new)
    canvasBase.create_image(160, 160, image = image)
    
    def __init__(self, x, y, canvas):
        
        self.x = x
        self.y = y
        self.canvas = canvas
        self.canvas.create_image(self.x, self.y, image = self.image)
    

        
            
if __name__ == "__main__":
    root = tk.Tk()
    app = Asteroids(root)
    root.mainloop()   
    
    