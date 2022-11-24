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

class Asteroids:
   
    
    def __init__(self,master):
        
        self.master = master
        
        imgAsteroide = Image.open("asteroide.png")
        new = imgAsteroide.resize((60, 60), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(new)
     
        
        self.x = 100
        self.y = 100
        self.label = Label(master=self.master, image=self.image)
        #self.label.create_image(self.x, self.y, image = self.image)
        self.label.place( x= self.x, y= self.y)
        
    def move(self):
        self.label.move(100,150)
       
        
    def start(self):
        self.master.mainloop()




app = Asteroids(canvasBase)
app.start()
root.mainloop()
 

    

        
            

    
    