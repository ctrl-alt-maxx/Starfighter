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

# Add Images to Canvas widget
# image = ImageTk.PhotoImage(Image.open('asteroide.png'))
# img = canvas.create_image(0, 120, anchor=NW, image=image)

# column = [""] * 7
# for i in range(7):
#    column[i] = random.randrange(0, 601)


# CREATION DU TABLEAU
item = [""] * 5
# 2 OBJETS RANDOM VONT TOMBER 
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


wave = 3
# Define a function to allow the image to move within the canvas
def move(root, e):
   global image
   global image2
   global image3
   global image4
   global image5
   imgItem = Image.open(item[count])
   # count += 1
   new = imgItem.resize((60, 60), Image.ANTIALIAS)
   if count == 0:
      image = ImageTk.PhotoImage(new)
   #img = canvas.create_image(e.x, e.y, image=image)
      img = canvas.create_image(e[0], e[1], image=image)
      root.after(50, partial(move, win, (e[0] - 0, e[1] + 5))) # oringinal: 2
   elif count == 1:
      image2 = ImageTk.PhotoImage(new)
      img = canvas.create_image(e[0], e[1], image=image2)
      root.after(50, partial(move, win, (e[0] - 0, e[1] + 5)))
   elif count == 2:
      image3 = ImageTk.PhotoImage(new)
      img = canvas.create_image(e[0], e[1], image=image3)
      root.after(50, partial(move, win, (e[0] - 0, e[1] + 5)))
   elif count == 3:
      image4 = ImageTk.PhotoImage(new)
      img = canvas.create_image(e[0], e[1], image=image4)
      root.after(50, partial(move, win, (e[0] - 0, e[1] + 5)))
   elif count == 4:
      image5 = ImageTk.PhotoImage(new)
      img = canvas.create_image(e[0], e[1], image=image5)
      root.after(50, partial(move, win, (e[0] - 0, e[1] + 5)))


# def move2(root, e):
#    global image2
#    imgAsteroide = Image.open(item[1])
#    new = imgAsteroide.resize((60, 60), Image.ANTIALIAS)
#    image2 = ImageTk.PhotoImage(new)
#    #img = canvas.create_image(e.x, e.y, image=image)
#    img = canvas.create_image(e[0], e[1], image=image2)
#    root.after(50, partial(move2, win, (e[0] - 0, e[1] + 5)))
# Bind the move function
#canvas.bind("<B1-Motion>", move)

#win.after(5, partial(move, win, (240, -100)))
def moving():
   win.after(5, partial(move, win, (column[0], -100)))
   # win.after(5, partial(move2, win, (column[1], -50)))

count = 0
for i in range(3):
   for x in range(5):
      column = random.randrange(0, 601)
      move(win, (column, -100))
   count += 1
   win.mainloop()
# win.mainloop()
# move2(win, (200, -100))
# moving()
