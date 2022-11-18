import tkinter as tk
from tkinter import ttk ,BOTH, Canvas, Label, PhotoImage,BOTTOM,RIGHT,LEFT, TOP, X, Y
from tkinter import *

root = tk.Tk()
# Couleur de fond 
root.config(background="black")
# Ajouter un titre à la fenêtre Tk
root.title("STARFIGHTER")
# Fixe la taille de la fenêtre en px
root.geometry("650x750")

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
        self.limg.borderwidth=0
        self.limg.place( x= 210, y= 40)
           
        self.button2 = tk.Button(self.master, text="Quit", command=self.master.destroy, font=("Terminal", 20),fg="red",bg="black",activebackground="red",activeforeground="black",border=4,relief="ridge",pady=10)
        self.button2.place( x= 277, y= 600)
        
        self.button3 = tk.Button(self.master, text="Rules", command=startRules, font=("Terminal", 20),fg="red",bg="black",activebackground="red",activeforeground="black",border=4,relief="ridge",pady=10)
        self.button3.place( x= 270, y= 400)
        
        self.button1 = tk.Button(self.master, text="Start",command=startGame, font=("Terminal", 20),fg="red",bg="black",activebackground="red",activeforeground="black",border=4,relief="ridge",pady=10)
        self.button1.place( x= 275, y= 300)
        
        self.button1 = tk.Button(self.master, text="Leaderboard",command=startGame, font=("Terminal", 20),fg="red",bg="black",activebackground="red",activeforeground="black",border=4,relief="ridge",pady=10)
        self.button1.place( x= 225, y= 500)
      
        
    
          
    def start(self):
        self.master.mainloop()

        

       

app = StartScreen(root)
app.start()   
    
root.mainloop()   

 


         
    


    

        

        
    
    
        

    
    
    
   



