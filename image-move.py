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
item = []
for i in range(2):
   num = random.randrange(0,34)
   if num <= 10:
      item[i] = ob.Objet.ovni
   elif num >= 11 or num <= 15:
      item[i] = ob.Objet.fuel
   elif num >= 16 or num <= 20:
      item[i] = ob.Objet.bolt
   elif num >= 21 or num <= 30:
      item[i] = ob.Objet.asteroid
   elif num >= 31 or num <= 33:
      item[i] = ob.Objet.aid  

# Define a function to allow the image to move within the canvas
def move(root, e):
   global image
   imgAid = Image.open(item[0])
   new = imgAid.resize((60, 60), Image.ANTIALIAS)
   image = ImageTk.PhotoImage(new)
   #img = canvas.create_image(e.x, e.y, image=image)
   img = canvas.create_image(e[0], e[1], image=image)
   root.after(50, partial(move, win, (e[0] - 0, e[1] + 5))) # oringinal: 2

def move2(root, e):
   global image2
   imgAsteroide = Image.open(item[1])
   new = imgAsteroide.resize((60, 60), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(new)
   #img = canvas.create_image(e.x, e.y, image=image)
   img = canvas.create_image(e[0], e[1], image=image2)
   root.after(50, partial(move2, win, (e[0] - 0, e[1] + 5)))
# Bind the move function
#canvas.bind("<B1-Motion>", move)

#win.after(5, partial(move, win, (240, -100)))
def moving():
   win.after(5, partial(move, win, (240, -100)))
   win.after(5, partial(move2, win, (350, -100)))
   
# move(win, (240, -100))
# move2(win, (200, -100))
moving()
win.mainloop()