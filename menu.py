import tkinter as tk
from tkinter import ttk ,BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y   
from tkinter import *
import sys
print(sys.executable)
#from PIL import ImageTk, Image

root = tk.Tk()
"""Couleur de fond"""
root.config(background="black")

"""Ajouter un titre à la fenêtre Tk"""
root.title("STARFIGHTER")

"""Fixe la taille de la fenêtre en px"""
root.geometry("650x750")

def startGame():
    """_summary_ : Cette fonction permet de lancer le jeu
    """
    root.destroy()
    #import game
    import main
    # import main instead of game to access Usha - main.py file 


def startRules():
    """_summary_ : Cette fonction permet d'afficher les règles du jeu
    """
    root.destroy()
    import rules
    
def startLeaderboard():
    """_summary_ : Cette fonction permet d'afficher le leaderboard"""
    root.destroy()
    import leaderboard

class StartScreen: 
    """_summary_ : Cette classe permet d'afficher le menu principal
    """
    def __init__(self, master):
        self.master = master
        
        
        """Chargement de l'image"""
        self.bgimg= PhotoImage(master=self.master,file = 'logo2.png')
        
        """Création d'un widget Canvas (zone graphique)"""
        self.limg= Label(master=self.master, image=self.bgimg)
        self.limg.borderwidth=0
        self.limg.place( x= 210, y= 40)
           
        self.button2 = tk.Button(self.master, text="Quit", command=self.master.destroy, font=("Terminal", 20),fg="red",bg="black",activebackground="red",activeforeground="black",border=4,relief="ridge",pady=10)
        self.button2.place( x= 277, y= 600)
        
        self.button3 = tk.Button(self.master, text="Rules", command=startRules, font=("Terminal", 20),fg="red",bg="black",activebackground="red",activeforeground="black",border=4,relief="ridge",pady=10)
        self.button3.place( x= 270, y= 400)
        
        self.button1 = tk.Button(self.master, text="Start",command=startGame, font=("Terminal", 20),fg="red",bg="black",activebackground="red",activeforeground="black",border=4,relief="ridge",pady=10)
        self.button1.place( x= 275, y= 300)
        
        self.button1 = tk.Button(self.master, text="Leaderboard",command=startLeaderboard, font=("Terminal", 20),fg="red",bg="black",activebackground="red",activeforeground="black",border=4,relief="ridge",pady=10)
        self.button1.place( x= 225, y= 500)
      
        
    
          
    def start(self):
        """_summary_ : Cette fonction permet de lancer le menu principal
        """
        self.master.mainloop()

        

       

app = StartScreen(root)
app.start()   
    
root.mainloop()   

 


         
    


    

        

        
    
    
        

    
    
    
   



