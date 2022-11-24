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
# image = ImageTk.PhotoImage(Image.open('asteroide.png'))
# img = canvas.create_image(0, 120, anchor=NW, image=image)



# Define a function to allow the image to move within the canvas
def move(root, e):
   global image
   imgAsteroide = Image.open('asteroide.png')
   new = imgAsteroide.resize((60, 60), Image.ANTIALIAS)
   image = ImageTk.PhotoImage(new)
   #img = canvas.create_image(e.x, e.y, image=image)
   img = canvas.create_image(e[0], e[1], image=image)
   root.after(50, partial(move, win, (e[0] - 0, e[1] + 2)))

def move2(root, e):
   global image
   imgAsteroide = Image.open('asteroide.png')
   new = imgAsteroide.resize((60, 60), Image.ANTIALIAS)
   image2 = ImageTk.PhotoImage(new)
   #img = canvas.create_image(e.x, e.y, image=image)
   img = canvas.create_image(e[0], e[1], image=image2)
   root.after(50, partial(move, win, (e[0] - 0, e[1] + 2)))
# Bind the move function
#canvas.bind("<B1-Motion>", move)

#win.after(5, partial(move, win, (240, -100)))
def moving():
   win.after(5, partial(move, win, (240, -100)))
   win.after(5, partial(move2, win, (240, -100)))
   
# move(win, (240, -100))
# move2(win, (200, -100))
moving()
win.mainloop()