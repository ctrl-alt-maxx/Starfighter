
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
#my_w.bind('<Motion>',my_callback) # Mouse left button pressed move
#my_w.mainloop()
   

root = tk.Tk()
root.geometry("615x400")

def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))
    l1.config(text='Position x : '+ str(event.x) +", y : "+ str(event.y))

l1=tk.Label(root,text='just move',bg='yellow',font=30)
l1.pack(padx=10,pady=10)

root.bind('<Motion>', motion)

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
#from tkinter import *
#from tkinter.tix import IMAGETEXT

#Create an instance of tkinter frame
#win= Tk()

#Define the size of window or frame
#win.geometry("1000x1000")

#Set the Menu initially
#menu= StringVar()
#menu.set("Select Any Language")

#Create a dropdown Menu
#drop= OptionMenu(win, menu,"C++", "Java","Python","JavaScript","Rust","GoLang")
#drop.pack(anchor="sw")

#canvas = tk.Canvas(win, width=400, height=400)
#canvas.pack()

#def move(e):
#    global image
#    image = ImageTk.PhotoImage(Image.open("vaisseau.png"))
        #image.resize((150, 150), Image.ANTIALIAS)
        
#    img = canvas.create_image(e.x, e.y, image = image)

#canvas.bind("<Motion>", move) 

#win.mainloop()


#from os import stat
#from time import time
#from tkinter import *
#from tracemalloc import start
#import time


#def buttonPressed( event ):
#   var.set( "Pressed at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

#def buttonReleased( event ):
#   var.set( "Released at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

#def enteredWindow( event ):
#   var.set( "Mouse in window" )

#def exitedWindow(  event ):
#   var.set( "Mouse outside window" )

#def mouseDragged( event ):
#   var.set( "Dragged at [ " + str( event.x ) + ", " + str( event.y ) + " ]" )

#def timer(mouseDragged) :
#   startTime = time.time()
#   while (mouseDragged) :
#      totalTime = round((time.time() - startTime), 2)
#      print(totalTime)

#base = Tk()
#base.title("Mouse Events")


#frame = Frame(base, width=300, height=300)
#frame.pack()

#var = StringVar()
#var.set("Mouse Events will show here")
#label = Label(base, textvariable=var)
#label.pack(side=BOTTOM)

#frame.bind( "<Button-1>", buttonPressed )
#frame.bind( "<ButtonRelease-1>", buttonReleased )   
#frame.bind( "<Enter>", enteredWindow )
#frame.bind( "<Leave>", exitedWindow )
#frame.bind( "<B1-Motion>", mouseDragged )
#frame.bind("<B1-Motion>", timer)

#if (frame.bind("<ButtonRelease-1>", buttonReleased)) :
#   (frame.bind("<Leave>"), timer)



#base.mainloop()

#import tkinter
#from functools import partial

#window = tkinter.Tk()
#canvas = tkinter.Canvas(width=1000, height=600, bg="black")
#canvas.pack()

#def on_click(item, event=None):
#    print(f"Item id {item} was clicked!")

#def rectangle(x, y):
#    item_id = canvas.create_rectangle(x, y, x + 5, y + 5, fill="white")
#    canvas.tag_bind(item_id, '<Button-1>', partial(on_click, item_id))

#rect1 = rectangle(20, 50)
#rect2 = rectangle(180, 30)
#rect3 = rectangle(698, 322)
#rect4 = rectangle(900, 66)
#rect5 = rectangle(10, 506)
#rect6 = rectangle(208, 455)

#def highlight_nearest(event):
#    canvas = event.widget
#    x = canvas.canvasx(event.x)
#    y = canvas.canvasy(event.y)
#    item = canvas.find_closest(x, y)
#    canvas.itemconfigure(item, fill="red")

#canvas.bind("<1>", highlight_nearest)

#window.mainloop()

#import tkinter as tk

#my_w = tk.Tk()

#width,height=410,210 # set the variables 

#c_width,c_height=width-10,height-45 # canvas width height

#d=str(width)+"x"+str(height)

#my_w.geometry(d) 

#c1 = tk.Canvas(my_w, width=c_width, height=c_height,bg='lightgreen')
#c1.grid(row=1,column=0,padx=5,pady=5)

#step=5 # value of each incremental movment, change this 

#x1,y1=5,int(c_height/2) # starting position 
#x2,y2=x1+15,y1+15      # starting position 

#r1=c1.create_rectangle(x1, y1, x2,y2,fill='red')  # draw rectangle

#def my_draw():        
#    global x1,y1,x2,y2,r1    
#    c1.delete(r1) # delete the rectangle         
#    r1=c1.create_rectangle(x1, y1, x2,y2,fill='red')    
#    if (x2<(c_width-step)): # check for right edge          
#        x1,x2=x1+step,x2+step # new coordinates of rectangle        
#        c1.after(100,my_draw)  # recursive call after delay           
#    else:        
#        return   # stop recursive call and return to main 

#my_draw() # start moving, remove this if not required at beginning 

#def restart():    
#    global x1,y1,x2,y2    
#    x1,y1=5,int(c_height/2) # starting position     
#    x2,y2=x1+15,y1+15      # starting position     
#    my_draw() # start from starting position 
#    b1=tk.Button(my_w,text='Restart',command=lambda:restart())
#    b1.grid(row=2,column=0)

#restart()

#my_w.mainloop()

root.mainloop()