import tkinter as tk
from tkinter import BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y, messagebox


root = tk.Tk()

# Couleur de fond 
root.config(background="black")

# Ajouter un titre à la fenêtre Tk
root.title("Jeu du carré rouge")

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
        
        self.button1 = tk.Button(self.master, text="Jouer", command=startGame(), font=("Arial", 20), bg="white")
        self.button1.place( x= 300, y= 300)
      
        self.limg.place( x= 230, y= 60)
        
        def startGame(self):
            self.master.destroy()
            GameScreen(self.master)    
        
      
    
        #self.button1.pack(side=tk.BOTTOM
         
        
   
    
    def start(self):
        #self.draw()
        self.master.mainloop()

class GameScreen: 
    def __init__(self,master):
        self.master = master
        self.master.config(background="black")
        self.master.title("Starfighter")
        self.master.geometry("700x800")
        self.canvas = Canvas(self.master, width=700, height=800, bg="black")
        self.canvas.pack(fill=BOTH, expand=1)
        self.label = tk.Label(self.master, text="STARFIGHTER", font=("Arial", 30), bg="white")
        self.label.pack()
        self.button1 = tk.Button(self.master, text="Quitter", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button1.pack(side=tk.BOTTOM)
        self.button2 = tk.Button(self.master, text="Rejouer", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button2.pack(side=tk.BOTTOM)
        
        
        
         
        
        
    
    # if __name__ == "__main__":
    #     app = StartScreen(root)
    #     app.start()
    
    
   

   
root.mainloop()