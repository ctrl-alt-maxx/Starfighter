
from functools import partial
from shutil import move
import tkinter as tk 
from tkinter import CENTER, Canvas, Frame, OptionMenu, PhotoImage, Label, StringVar
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
canvasBase = tk.Canvas(root, background="black", width=800, height=1000, highlightthickness=1, highlightbackground="red", relief='ridge')
canvasBase.pack()

class Vaisseau:

    imageVaisseau = Image.open("vaisseau.png")
    test = ImageTk.PhotoImage(imageVaisseau)

    #Resize the Image using resize method
    resized_image = imageVaisseau.resize((50,50), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)

    #img = canvasBase.create_image(40, 40, image=new_image)

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
        new = Vaisseau.imageVaisseau.resize((50,50), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(new)
        
        img = canvasBase.create_image(e.x, e.y, image = image)
        

    # Bind the move function 
    canvasBase.bind("<Motion>", move)       ## THIS WORKS!! vaisseau follows the cursor

# HEADS UP DISPLAY 
class HUD: 
    # Doit etre capable d'afficher les points courants, niveau de jeu, vie restante, etc.
 
    score = 0

    def scoreCounter(): 
       global score
       HUD.score += 1
       print(HUD.score)
    
    
    labelPoints = tk.Label(root, text='Score: ' + str(score), font = 90, padx=10, pady=10)
    labelPoints.place(relx=0.0, rely=0.0, anchor='nw')

    menu = StringVar()
    menu.set("Choississez le niveau de jeu")
    drop = OptionMenu(root, menu, "Facile", "Moyen", "Difficile")
    drop.pack(anchor="e")

    def vieRestante():
        vie = Image.open("lives.png")
        vie.resize((10,10), Image.ANTIALIAS)



imgOvni = Image.open("ovnii.png")



new = imgOvni.resize((50,50), Image.ANTIALIAS)
image = ImageTk.PhotoImage(new)

img = canvasBase.create_image(50, 50, image = image)





root.mainloop()
