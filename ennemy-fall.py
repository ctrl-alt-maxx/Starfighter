# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk
from functools import partial
import Objet as ob
import random

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a Canvas widget
canvas = Canvas(win, width=600, height=400, bg="black")
canvas.pack(pady=20)

# CREATION DU TABLEAU DE COLONNE
column = [""] * 7
column[0] = random.randrange(0, 101)
column[1] = random.randrange(100, 201)
column[2] = random.randrange(200, 301)
column[3] = random.randrange(300, 401)
column[4] = random.randrange(400, 501)
column[5] = random.randrange(500, 601)
# for i in range(7):
#    column[i] = random.randrange(0, 601)

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
   num = random.randrange(0,34)
   if num <= 10:
      item[i] = ob.Objet.ovni
   elif num >= 11 and num <= 15:
      item[i] = ob.Objet.fuel
   elif num >= 16 and num <= 20:
      item[i] = ob.Objet.bolt
   elif num >= 21 and num <= 30:
      item[i] = ob.Objet.asteroid
   elif num >= 31 and num <= 33:
      item[i] = ob.Objet.aid


# wave = 3
# Define a function to allow the image to move within the canvas
def move(root, e):
   global image
   imgItem = Image.open(item[0])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image = ImageTk.PhotoImage(new)
   #img = canvas.create_image(e.x, e.y, image=image)
   img = canvas.create_image(e[0], e[1], image=image)
   root.after(50, partial(move, win, (e[0] - 0, e[1] + speed[0]))) # oringinal: 2


def move2(root, e):
   global image2
   imgItem = Image.open(item[1])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(new)
   img = canvas.create_image(e[0], e[1], image=image2)
   root.after(50, partial(move2, win, (e[0] - 0, e[1] + speed[1])))

def move3(root, e):
   global image3
   imgItem = Image.open(item[2])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image3 = ImageTk.PhotoImage(new)
   img = canvas.create_image(e[0], e[1], image=image3)
   root.after(50, partial(move3, win, (e[0] - 0, e[1] + speed[2])))

def move4(root, e):
   global image4
   imgItem = Image.open(item[3])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image4 = ImageTk.PhotoImage(new)
   img = canvas.create_image(e[0], e[1], image=image4)
   root.after(50, partial(move4, win, (e[0] - 0, e[1] + speed[3])))

def move5(root, e):
   global image5
   imgItem = Image.open(item[4])
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   image5 = ImageTk.PhotoImage(new)
   img = canvas.create_image(e[0], e[1], image=image5)
   root.after(50, partial(move5, win, (e[0] - 0, e[1] + speed[4])))
# Bind the move function
#canvas.bind("<B1-Motion>", move)

def moving():
   win.after(5, partial(move, win, (column[0], -start[0])))
   win.after(5, partial(move2, win, (column[1], -start[1])))
   win.after(5, partial(move3, win, (column[2], -start[2])))
   win.after(5, partial(move4, win, (column[3], -start[3])))
   win.after(5, partial(move5, win, (column[4], -start[4])))

# count = 0
# for i in range(3):
#    for x in range(5):
      # column = random.randrange(0, 601)
      # move(win, (column, -100))
   # count += 1
   # win.mainloop()
# move2(win, (200, -100))
moving()
win.mainloop()