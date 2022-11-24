import math
import tkinter as tk
from tkinter import ttk ,BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y   
from tkinter import *

class Asteroids:
    def __init__(self, master):
        self.master = master
        self.canvas = Canvas(self.master, width=700, height=800, bg="black")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.onClick)
        self.canvas.bind("<Button-3>", self.onRightClick)
        self.canvas.bind("<Motion>", self.onMouseMove)
        self.canvas.bind("<Key>", self.onKeyPress)
        self.canvas.bind("<KeyRelease>", self.onKeyRelease)
        self.canvas.focus_set()
        self.master.after(100, self.update)
        self.master.mainloop()
        
    def update(self):
        self.master.after(100, self.update)
        
            
if __name__ == "__main__":
    root = tk.Tk()
    app = Asteroids(root)
    root.mainloop()   
    
    