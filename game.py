import tkinter as tk
from tkinter import BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y, messagebox, filedialog, Menu, Frame, Button, Entry, StringVar, IntVar, END

root = tk.Tk()
root.config(background="black")
root.title("STARFIGHTER")
root.geometry("700x800")

class GameScreen:
    def __init__(self, master):
        self.master = master
        
        
        
        
        self.score = "0"
        
        # self.label = Label(self.master, text="STARFIGHTER", font=("Arial", 20), bg="black", fg="white")
        # self.label.pack()
        
        # self.label2 = tk.Label(self.master, text="Score : " + self.score, font=("Arial", 20), bg="black", fg="white")
        # self.label2.pack()
        
        # self.label3 = tk.Label(self.master, text="Temps : ", font=("Arial", 20), bg="black", fg="white")
        # self.label3.pack()
        
        # self.button = tk.Button(self.master, text="Quitter", command=self.master.destroy, font=("Arial", 20), bg="white")
        # self.button.pack()
        
        
        self.canvas = Canvas(self.master, width=700, height=800, bg="white")
        self.canvas.pack()
        
        # self.canvas.bind("<Button-1>", self.onClick)
        
        self.master.mainloop()
       
        
    def startit(self):
        self.master.mainloop()

if __name__ == "__main__":
    app = GameScreen(root)
    app.startit()   
    
    root.mainloop()          