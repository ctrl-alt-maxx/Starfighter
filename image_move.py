# Import the required libraries
from tkinter import *
from PIL import Image, ImageTk
from functools import partial

# Create an instance of tkinter frame
win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Define a Canvas widget
canvas = Canvas(win, width=600, height=400, bg="white")
canvas.pack(pady=20)

# Add Images to Canvas widget
image = ImageTk.PhotoImage(Image.open('logo.png'))
img = canvas.create_image(250, 120, anchor=NW, image=image)

# def left(e):
#    x = -20
#    y = 0
#    canvas.move(img, x, y)

# def right(e):
#    x = 20
#    y = 0
#    canvas.move(img, x, y)

# def w(e):
#    x = 0
#    y = -20
#    canvas.move(img, x, y)

# def down(e):
#    x = 0
#    y = 20
#    canvas.move(img, x, y)

# Define a function to allow the image to move within the canvas
def move(root, e):
   global image
   image = ImageTk.PhotoImage(Image.open('logo.png'))
   #img = canvas.create_image(e.x, e.y, image=image)
   img = canvas.create_image(e[0], e[1], image=image)
   root.after(5, partial(move, win, (e[0] - 0, e[1] - 2)))

# Bind the move function
#canvas.bind("<B1-Motion>", move)

win.after(500, partial(move, win, (240, 120)))

win.mainloop()