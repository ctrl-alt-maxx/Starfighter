import tkinter as tk
from tkinter import BOTH, Canvas, Label, PhotoImage

root = tk.Tk()


class GameScreen:
    def __init__(self, master):
        self.master = master
        self.master.config(background="black")
        self.master.title("STARFIGHTER")
        self.master.geometry("700x800")
        self.score = "0"
        
        self.label = tk.Label(self.master, text="STARFIGHTER", font=("Arial", 20), bg="black", fg="white")
        self.label.pack()
        
        self.label = tk.Label(self.master, text="Score : " + self.score, font=("Arial", 20), bg="black", fg="white")
        self.label.pack()
        
        self.label = tk.Label(self.master, text="Temps : ", font=("Arial", 20), bg="black", fg="white")
        self.label.pack()
        
        self.button = tk.Button(self.master, text="Quitter", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button.pack()
        
        
        self.canvas = Canvas(self.master, width=700, height=800, bg="white")
        self.canvas.pack()
        
        # self.canvas.bind("<Button-1>", self.onClick)
        
        
       
        
    def startit(self):
        self.master.mainloop()

if __name__ == "__main__":
    app = GameScreen(root)
    app.startit()   
    
    root.mainloop()          