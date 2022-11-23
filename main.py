
import tkinter as tk 
from tkinter import Frame, PhotoImage, Label
from PIL import ImageTk, Image
from pygame import image  


root = tk.Tk()

# COULEUR DE FOND       
root.config(background="black")

# AJOUTER UN TITRE A LA FENETRE TKINTER
root.title("Starfighter")

# FIXE LA TAILLE EN PIXEL 
root.geometry("5000x5000")

frame = Frame(root)
frame.pack()

# CREATION DU CANVAS 
canvasBase = tk.Canvas(root, background="black", width=800, height=1000, highlightthickness=0, relief='ridge')
canvasBase.pack()

class Vaisseau:

    imageVaisseau = Image.open("vaisseau.png")
    test = ImageTk.PhotoImage(imageVaisseau)

    #Resize the Image using resize method
    resized_image = imageVaisseau.resize((50,50), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)

    img = canvasBase.create_image(40, 40, image=new_image)

    def left(e) :
        x = -20
        y = 0
        canvasBase.move(Vaisseau.img, x, y)

    def right(e):
        x = 20
        y = 0
        canvasBase.move(Vaisseau.img, x, y)

    def up(e):
        x = 0
        y = -20
        canvasBase.move(Vaisseau.img, x, y)
    
    def down(e):
        x = 0
        y = 20
        canvasBase.move(Vaisseau.img, x, y)

    # Define a function to allow the image to move within the canvas 
    def move(e):
        global image
        image = ImageTk.PhotoImage(Image.open("vaisseau.png"))
        
        img = canvasBase.create_image(e.x, e.y, image = image)

    # Bind the move function 
    canvasBase.bind("<Motion>", move)       ## THIS WORKS!! vaisseau allows to move with the cursor 

# HEADS UP DISPLAY 
class HUD: 
    






root.mainloop()
