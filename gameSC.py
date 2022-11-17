import tkinter as tk
from tkinter import BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y
import game as g

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
        
        
        """Chargement de l'image"""
        self.bgimg= PhotoImage(master=self.master,file = 'logo2.png') 
        
        """Création d'un widget Canvas (zone graphique)"""
        self.limg= Label(master=self.master, image=self.bgimg)
        
           
        self.button2 = tk.Button(self.master, text="Quitter", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button2.place( x= 293, y= 500)
        
        self.button3 = tk.Button(self.master, text="Règles", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button3.place( x= 291, y= 400)
        
        self.button1 = tk.Button(self.master, text="Jouer",command=startGame(self), font=("Arial", 20), bg="white")
        self.button1.place( x= 300, y= 300)
      
        self.limg.place( x= 230, y= 60)
    
        self.master.mainloop()   
    def start(self):
        self.master.mainloop()

def startGame(self):
        self.master.destroy()
        g.GameScreen(root).startit()

       
if __name__ == "__main__":
    app = StartScreen(root)
    app.start()   
    
root.mainloop()   

 


         
    


    

        

        
    
    
        

    
    
    
   



