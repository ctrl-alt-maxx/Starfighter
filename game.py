import tkinter as tk
from tkinter import BOTH, Canvas, Label, PhotoImage

root = tk.Tk()


class GameScreen:  
  
    def __init__(self, master):
        self.master = master
        
        self.score = 0
        
        self.canvas = tk.Canvas(self.master, width=700, height=800, bg="black")
        self.canvas.pack()
        
        self.button2 = tk.Button(self.master, text="Quitter", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button2.place( x= 293, y= 500)
        
        self.label = tk.Label(self.master, text="Score : ", font=("Arial", 20), bg="white")
        self.label.pack()
        
        self.label = tk.Label(self.master, text="Temps : ", font=("Arial", 20), bg="white")
        self.label.pack()
        
        self.label = tk.Label(self.master, text="Niveau : ", font=("Arial", 20), bg="white")
        self.label.pack()
        
        self.label = tk.Label(self.master, text="Vie : ", font=("Arial", 20), bg="white")
        self.label.pack()
        
        self.label = tk.Label(self.master, text="STARFIGHTER", font=("Arial", 30), bg="white")
        self.label.pack()
        
    def start(self):
        #self.draw()
        self.master.mainloop()
            
        
if __name__ == "__main__":
        app = GameScreen(root)
        app.start()
        
