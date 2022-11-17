import tkinter as tk
import game as g
from tkinter import BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y, messagebox


root = tk.Tk()

# Couleur de fond 
root.config(background="black")

# Ajouter un titre à la fenêtre Tk
root.title("STARFIGHTER")

# Fixe la taille de la fenêtre en px
root.geometry("700x800")

class StartScreen: 
    
    def __init__(self, master):
        self.master = master
        
        
        
        # Création d'un widget Canvas (zone graphique)
        self.bgimg= PhotoImage(file = "logo2.png")
        self.limg= Label(self.master, i=self.bgimg, bg="black")
        
        
      
        
                 #self.label = tk.Label(self.master, text="JEU DU CARRÉ ROUGE", font=("Arial", 30), bg="white")
        #self.label.pack()
        
        
        
        self.button2 = tk.Button(self.master, text="Quitter", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button2.place( x= 293, y= 500)
        
        self.button3 = tk.Button(self.master, text="Règles", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button3.place( x= 291, y= 400)
        
        self.button1 = tk.Button(self.master, text="Jouer", font=("Arial", 20), bg="white")
        self.button1.place( x= 300, y= 300)
      
        self.limg.place( x= 230, y= 60)
        
           
        
      
    
  
    def start(self):
        #self.draw()
        self.master.mainloop()
        
# # def startGame(self):
#     self.master.destroy()
#     game = g.GameScreen(root) 
#     game.start()



    
if __name__ == "__main__":
        app = StartScreen(root)
        app.start()
        
        
root.mainloop()
    


