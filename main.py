
from functools import partial
from shutil import move
import tkinter as tk 
from tkinter import ANCHOR, CENTER, Canvas, Frame, OptionMenu, PhotoImage, Label, StringVar
from PIL import ImageTk, Image
from pygame import image  
import c31Geometry2 as c31

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
        Vaisseau.vaisseauEdgeReached()

    # Bind the move function 
    canvasBase.bind("<Motion>", move)       ## THIS WORKS!! vaisseau follows the cursor
        

    # SOOTING LASER IN PROJECTILES 
    imageLaser = Image.open("laser1.png");
    testLaser = ImageTk.PhotoImage(imageLaser);

    # Resize the image using resized method 
    resized_imgLaser = imageLaser.resize((10, 50), Image.ANTIALIAS);
    new_imgLaser = ImageTk.PhotoImage(resized_imgLaser);

    def moveLaser():
        global laser, laserLoop
        canvasBase.move(laser, 0, -10);
        laserLoop = root.after(10, Vaisseau.moveLaser)

    def shoot(event):
        global laser, laserLoop
        try:
            root.after_cancel(laserLoop)
            canvasBase.delete(laser)
            laser = canvasBase.create_image(event.x, event.y, image=Vaisseau.new_imgLaser);
            Vaisseau.moveLaser()
        except NameError:
            laser = canvasBase.create_image(event.x, event.y, image=Vaisseau.new_imgLaser);
            Vaisseau.moveLaser()

    canvasBase.bind_all("<1>", shoot);

    def vaisseauEdgeReached():
        shipBoundary = canvasBase.bbox(Vaisseau)
        shipLeft = shipBoundary[0]
        shipRight = shipBoundary[2]
        shipTop = shipBoundary[1]
        shipBottom = shipBoundary[3]

        if shipLeft < 0:
            canvasBase.move(Vaisseau, 10, 0)
        elif shipTop < 0:
            canvasBase.move(Vaisseau, 0, 10)
        
    # Detecting collision between the ship and the enemies 
    def collisionDetection():
        # Ship boundary
        shipB = canvasBase.bbox(Vaisseau)

        # Enemy boundary (Ovni)
        ovB = canvasBase.bbox(Ovni)
        if ovB[0] < shipB[2] < ovB[2] and ovB[1] < shipB[1] < ovB[3]:
            canvasBase.move(Ovni, 50, 50)


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


class Ovni:

    imgOvni = Image.open("ovnii.png")
    new = imgOvni.resize((60,60), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(new)

    canvasBase.create_image(100, 200, anchor="nw", image=image)


class Asteroide:
    imgAsteroide = Image.open("asteroide.png")
    new = imgAsteroide.resize((60, 60), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(new)
    canvasBase.create_image(160, 160, image = image)


class Flash:
    imgBolt = Image.open("bolt.jpeg")
    new = imgBolt.resize((80,80), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(new)
    canvasBase.create_image(250,250, image=image)

class Fuel:
    imgFuel = Image.open("fuel.png")
    new = imgFuel.resize((70,70), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(new)
    canvasBase.create_image(500,500, image = image)

class Aid:
    imgAid = Image.open("aid.png")
    new = imgAid.resize((60,60), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(new)
    canvasBase.create_image(600,600, image = image)


root.mainloop()
