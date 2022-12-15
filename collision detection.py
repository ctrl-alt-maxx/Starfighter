from msilib.schema import File
from tkinter import *
from turtle import left
from PIL import Image, ImageTk
from functools import partial
import Objet as ob

win = Tk()

# Set the size of the tkinter window
win.geometry("700x750")
lives = 10
#life = []
pts = ob.Objet.lives
imgLife = Image.open(pts)
new = imgLife.resize((60, 60), Image.ANTIALIAS)
life = ImageTk.PhotoImage(new)

label = Label(win, text="Life: " + str(lives), font=("Terminal", 20), bg="black", fg="red")
label.pack(anchor=W)


label2 = Label(win, image=life, height=50, width=50)
label2.pack(anchor=N)


canvas = Canvas(win, width=700, height=700, bg="blue")
canvas.pack(pady=20)

item = ob.Objet.bolt

# imgItem = Image.open(item)
# new = imgItem.resize((60, 60), Image.ANTIALIAS)
# image = ImageTk.PhotoImage(new)
# #img = canvas.create_image(e.x, e.y, image=image)
# img = canvas.create_image(300, 400, image=image)
# win.after(50, partial(move, win, (e[0] - 0, e[1] + 5))) # oringinal: 2

def move(root, e):
    global image
    imgItem = Image.open(item)
    new = imgItem.resize((60, 60), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(new)
    img = canvas.create_image(e[0], e[1], image=image)
    root.after(50, partial(move, win, (e[0] - 0, e[1] + 8)))
    collision(img)

imageVaisseau = Image.open("vaisseau.png")
test = ImageTk.PhotoImage(imageVaisseau)


#Resize the Image using resize method
resized_image = imageVaisseau.resize((50,50), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
vai = canvas.create_image(500, 400, image=new_image)

# Define a function to allow the image to move within the canvas 
def moveV(e):
    global image2
    # new = imageVaisseau.resize((50,50), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(resized_image)
    img = canvas.create_image(e.x, e.y, image = image2)
    # return img
    # collision(img)
    

# Bind the move function 
canvas.bind("<Motion>", moveV)  ## THIS WORKS!! vaisseau follows the cursor

#v = moveV

def collision(objet):
    global lives
    sb = canvas.bbox(vai)
    eb = canvas.bbox(objet)
    if eb[0] < sb[2] < eb[2] and eb[1] < sb[1] < eb[3]:
        canvas.move(objet, 25, -25)
        print("CONTACT BOTTOM-LEFT")
        lives -= 1
    elif eb[2] > sb[0] > eb[0] and eb[1] < sb[1] < eb[3]:
        canvas.move(objet, -25, -25)
        print("CONTACT BOTTOM-RIGHT")
        lives -= 1
    elif sb[1] < eb[1] < sb[3] and eb[0] < sb[2] < eb[2]:
        canvas.move(objet, 25, 25)
        print("CONTACT TOP-RIGHT")
        lives -= 1
    elif sb[1] < eb[1] < sb[3] and sb[0] < eb[2] < sb[2]:
        canvas.move(objet, -25, 25)
        print("CONTACT TOP-LEFT")
        lives -= 1
    label.config(text="Score: " + str(lives))
    # print(pts)
    if lives <= 0:
        label.config(text="Score: " + str(lives) + " GAME OVER")
        lives = 0
        # game_over.pack()
        
        # win.destroy()

def moving():
    win.after(0, partial(move, win, (500, -20)))
    
moving()
win.mainloop()