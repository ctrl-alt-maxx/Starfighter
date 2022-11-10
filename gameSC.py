import tkinter as tk
from tkinter import BOTH, Canvas, Label, PhotoImage


root = tk.Tk()

# Couleur de fond 
root.config(background="black")

# Ajouter un titre à la fenêtre Tk
root.title("Jeu du carré rouge")

# Fixe la taille de la fenêtre en px
root.geometry("700x1000")

class StartScreen: 
    
    def __init__(self, master):
        self.master = master
        
        
        
        # Création d'un widget Canvas (zone graphique)
        self.bgimg= PhotoImage(file = "logo2.png")
        self.limg= Label(self.master, i=self.bgimg)
        
        
      
        
                 #self.label = tk.Label(self.master, text="JEU DU CARRÉ ROUGE", font=("Arial", 30), bg="white")
        #self.label.pack()
        
        
        
        self.button2 = tk.Button(self.master, text="Quitter", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button2.pack()
        
        self.button3 = tk.Button(self.master, text="Règles", font=("Arial", 20), bg="white")
        self.button3.pack()
        
        self.button1 = tk.Button(self.master, text="Jouer", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button1.pack()
      
        self.limg.pack()
        
      
    
        #self.button1.pack(side=tk.BOTTOM)
         
        
    # def startGame(self):
    #     self.master.destroy()
    #     GameScreen(self.master)    
    
    def start(self):
        #self.draw()
        self.master.mainloop()

#class GameScreen: 
    
if __name__ == "__main__":
    app = StartScreen(root)
    app.start()
    
    
   

   
root.mainloop()