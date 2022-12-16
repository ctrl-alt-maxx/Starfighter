from functools import partial
from hashlib import new
import random
from shutil import move
import tkinter as tk 
from tkinter import ANCHOR, CENTER, Canvas, Frame, OptionMenu, PhotoImage, Label, StringVar
from PIL import ImageTk, Image
import c31Geometry2 as c31
import Objet as ob      

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

    # Re-dimensioné
    resized_image = imageVaisseau.resize((50,50), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(resized_image)

    # Define a function to allow the image to move within the canvas 
    def move(e):
        global image
        new = Vaisseau.imageVaisseau.resize((50,50), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(new)
        
        img = canvasBase.create_image(e.x, e.y, image = image)

    canvasBase.bind("<Motion>", move)       
        

class Laser:
    # SOOTING LASER IN PROJECTILES 
    imageLaser = Image.open("laser1.png");
    testLaser = ImageTk.PhotoImage(imageLaser);

    # Resize the image using resized method 
    resized_imgLaser = imageLaser.resize((10, 50), Image.ANTIALIAS);
    new_imgLaser = ImageTk.PhotoImage(resized_imgLaser);

    def moveLaser():
        global laser, laserLoop
        canvasBase.move(laser, 0, -10);
        laserLoop = root.after(10, Laser.moveLaser)
        
    def shoot(event):
        global laser, laserLoop
        try:
            root.after_cancel(laserLoop)
            canvasBase.delete(laser)
            laser = canvasBase.create_image(event.x, event.y, image=Laser.new_imgLaser);
            Laser.moveLaser()
        except NameError:
            laser = canvasBase.create_image(event.x, event.y, image=Laser.new_imgLaser);
            Laser.moveLaser()

    canvasBase.bind_all("<1>", shoot);

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

def collision(objet):
    sb = canvasBase.bbox(Vaisseau)
    eb = canvasBase.bbox(objet)
    if eb[0] < sb[2] < eb[2] and eb[1] < sb[1] < eb[3]:
        canvasBase.move(objet, 25, -25)
    elif eb[2] > sb[0] > eb[0] and eb[1] < sb[1] < eb[3]:
        canvasBase.move(objet, -25, -25)
    elif sb[1] < eb[1] < sb[3] and eb[0] < sb[2] < eb[2]:
        canvasBase.move(objet, 25, 25)
    elif sb[1] < eb[1] < sb[3] and sb[0] < eb[2] < sb[2]:
        canvasBase.move(objet, -25, 25)

# CREATION DU TABLEAU DE COLONNE
column = [""] * 7
column[0] = random.randrange(0, 101)
column[1] = random.randrange(100, 201)
column[2] = random.randrange(200, 301)
column[3] = random.randrange(300, 401)
column[4] = random.randrange(400, 501)
column[5] = random.randrange(500, 601)

# CREATION DU TABLEAU DE DEPART
start = [""] * 10
for i in range(7):
   start[i] = random.randrange(0, 100)

# CREATION DU TABLEAU DE VITESSE (TOMBE VITE OU LENTEMENT)
speed = [""] * 10
for i in range(7):
   speed[i] = random.randrange(5, 11)

# CREATION DU TABLEAU D'IMAGE
item = [""] * 5

# 5 OBJETS RANDOM VONT TOMBER 
for i in range(5):
   num = random.randrange(0,41)
   if num <= 25:
      item[i] = ob.Objet.ovni
   elif num >= 26 and num <= 30:
      item[i] = ob.Objet.bolt
   elif num >= 31 and num <= 37:
      item[i] = ob.Objet.asteroid
   elif num >= 38 and num <= 40:
      item[i] = ob.Objet.aid

# Define a function to allow the image to move within the canvas
def move(root, e):
   global image1
   imgItem = Image.open(item[0])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image1 = ImageTk.PhotoImage(new)
   img = canvasBase.create_image(e[0], e[1], image=image1)
   root.after(50, partial(move, root, (e[0] - 0, e[1] + speed[0])))
   collision(img)


def move2(root, e):
   global image2
   imgItem = Image.open(item[1])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(new)
   img = canvasBase.create_image(e[0], e[1], image=image2)
   root.after(50, partial(move2, root, (e[0] - 0, e[1] + speed[1])))
   collision(img)

def move3(root, e):
   global image3
   imgItem = Image.open(item[2])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image3 = ImageTk.PhotoImage(new)
   img = canvasBase.create_image(e[0], e[1], image=image3)
   root.after(50, partial(move3, root, (e[0] - 0, e[1] + speed[2])))
   collision(img)

def move4(root, e):
   global image4
   imgItem = Image.open(item[3])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image4 = ImageTk.PhotoImage(new)
   img = canvasBase.create_image(e[0], e[1], image=image4)
   root.after(50, partial(move4, root, (e[0] - 0, e[1] + speed[3])))
   collision(img)

def move5(root, e):
   global image5
   imgItem = Image.open(item[4])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image5 = ImageTk.PhotoImage(new)
   img = canvasBase.create_image(e[0], e[1], image=image5)
   root.after(50, partial(move5, root, (e[0] - 0, e[1] + speed[4])))
   collision(img)

def moving():
   root.after(5, partial(move, root, (column[0], -start[0])))
   root.after(5, partial(move2, root, (column[1], -start[1])))
   root.after(5, partial(move3, root, (column[2], -start[2])))
   root.after(5, partial(move4, root, (column[3], -start[3])))
   root.after(5, partial(move5, root, (column[4], -start[4])))

moving()


root.mainloop()
