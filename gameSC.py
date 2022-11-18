import tkinter as tk
from tkinter import ttk ,BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y
from tkinter import *

root = tk.Tk()
# Couleur de fond 
root.config(background="black")
# Ajouter un titre à la fenêtre Tk
root.title("STARFIGHTER")
# Fixe la taille de la fenêtre en px
root.geometry("700x800")

def startGame():
    root.destroy()
    import game

def startRules():
    root.destroy()
    import rules

class StartScreen: 
    
    def __init__(self, master):
        self.master = master
        
        
        """Chargement de l'image"""
        self.bgimg= PhotoImage(master=self.master,file = 'logo2.png') 
        
        """Création d'un widget Canvas (zone graphique)"""
        self.limg= Label(master=self.master, image=self.bgimg)
        self.limg.place( x= 230, y= 60)
           
        self.button2 = tk.Button(self.master, text="Quitter", command=self.master.destroy, font=("Arial", 20), bg="white")
        self.button2.place( x= 293, y= 500)
        
        self.button3 = tk.Button(self.master, text="Règles", command=startRules, font=("Arial", 20), bg="white")
        self.button3.place( x= 291, y= 400)
        
        self.button1 = tk.Button(self.master, text="Jouer",command=startGame, font=("Arial", 20), bg="white")
        self.button1.place( x= 300, y= 300)
      
        
    
          
    def start(self):
        self.master.mainloop()

        

       

app = StartScreen(root)
app.start()   
    
root.mainloop()   

 


         
    


    

        

        
    
    
        

    
    
    
   



