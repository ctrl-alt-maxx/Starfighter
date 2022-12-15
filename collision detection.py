from tkinter import *
from PIL import Image, ImageTk
from functools import partial
import Objet as ob

win = Tk()

# Set the size of the tkinter window
win.geometry("700x750")
pts = 3
label = Label(win, text="Score: " + str(pts), font=("Arial", 20), bg="black", fg="white")
label.pack()

canvas = Canvas(win, width=700, height=700, bg="blue")
canvas.pack(pady=20)

item = ob.Objet.bolt

imgItem = Image.open(item)
new = imgItem.resize((60, 60), Image.ANTIALIAS)
image = ImageTk.PhotoImage(new)
#img = canvas.create_image(e.x, e.y, image=image)
img = canvas.create_image(300, 400, image=image)
# win.after(50, partial(move, win, (e[0] - 0, e[1] + 5))) # oringinal: 2

# def move(root, e):
#     global image
#     imgItem = Image.open(item)
#     new = imgItem.resize((60, 60), Image.ANTIALIAS)
#     image = ImageTk.PhotoImage(new)
#     #img = canvas.create_image(e.x, e.y, image=image)
#     img = canvas.create_image(e[0], e[1], image=image)
#     root.after(50, partial(move, win, (e[0] - 0, e[1] + 5)))
#     collision(img)

imageVaisseau = Image.open("vaisseau.png")
test = ImageTk.PhotoImage(imageVaisseau)

#Resize the Image using resize method
# resized_image = imageVaisseau.resize((50,50), Image.ANTIALIAS)
# new_image = ImageTk.PhotoImage(resized_image)

# Define a function to allow the image to move within the canvas 
def moveV(e):
    global image2
    new = imageVaisseau.resize((50,50), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(new)
    img = canvas.create_image(e.x, e.y, image = image2)
    collision(img)
    

# Bind the move function 
canvas.bind("<Motion>", moveV)  ## THIS WORKS!! vaisseau follows the cursor

def collision(objet):
    sb = canvas.bbox(objet)
    eb = canvas.bbox(img)
    if eb[0] < sb[2] < eb[2] and eb[1] < sb[1] < eb[3]:
        canvas.move(img, 25, 25)
        print("CONTACT BOTTOM-LEFT")
    elif eb[2] > sb[0] > eb[0] and eb[1] < sb[1] < eb[3]:
        canvas.move(img, -25, -25)
        print("CONTACT BOTTOM-RIGHT")
    # elif eb[1] < sb[1] < eb[3] and eb[0] < sb[0] < eb[3]:
    #     canvas.move(img, 25, -25)
    #     print("CONTACT TOP")
    # elif eb[0] < sb[2] < eb[2] and eb[1] > sb[1] > eb[3]:
    #     canvas.move(img, -25, 25)
    #     print("CONTACT TOM-LEFT")

# win.after(5, partial(move, win, (5, 5)))

win.mainloop()