
from functools import partial
import tkinter as tk 
from PIL import ImageTk, Image
from pygame import image


#my_w = tk.Tk()
#my_w.geometry("615x400")  # width and height 
#def my_callback(event):
#     l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))

#l1=tk.Label(my_w,text='to Display',bg='yellow',font=30)
#l1.pack(padx=10,pady=10)
#my_w.bind('<B1-Motion>',my_callback) # Mouse left button pressed move
#my_w.mainloop()
   

#root = tk.Tk()
#root.geometry("615x400")

#def motion(event):
    #x, y = event.x, event.y
    #print('{}, {}'.format(x, y))
#    l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))

#l1=tk.Label(root,text='just move',bg='yellow',font=30)
#l1.pack(padx=10,pady=10)

#root.bind('<Motion>', motion)

#score = 0



#labelPoints = tk.Label(root, text="Points: " + str(score), font = 30, padx=10, pady=10)
#labelPoints.place(relx=0.0, rely=0.0, anchor='nw')

   


#def foo(texte, event):
#    print(texte)

#count = 0  
  
#def add(): 
#    global count  
#    count += 1 
#    print (count) 
#button = tk.Button(text = 'add 1',command = add ).pack() 

#root.mainloop()

#Import the required libraries
from tkinter import *
from tkinter.tix import IMAGETEXT

#Create an instance of tkinter frame
win= Tk()

#Define the size of window or frame
win.geometry("1000x1000")

#Set the Menu initially
#menu= StringVar()
#menu.set("Select Any Language")

#Create a dropdown Menu
#drop= OptionMenu(win, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
#drop.pack(anchor="sw")

canvas = tk.Canvas(win, width=400, height=400)
canvas.pack()

def move(e):
    global image
    image = ImageTk.PhotoImage(Image.open("vaisseau.png"))
        #image.resize((150, 150), Image.ANTIALIAS)
        
    img = canvas.create_image(e.x, e.y, image = image)

canvas.bind("<Motion>", move) 

win.mainloop()
