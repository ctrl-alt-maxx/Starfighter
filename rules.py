import tkinter as tk
from tkinter import *
from tkinter import BOTTOM, font


root = tk.Tk()
root.config(background="black")
root.title("STARFIGHTER")
root.geometry("700x800")

font.families()

def callback(e):
   """ _summary_ : Cette fonction permet de récupérer les coordonnées de la souris"""
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))
   
root.bind('<Motion>',callback)

def returnBack():
    """_summary_ : Cette fonction permet de retourner au menu principal
    """
    root.destroy()
    import menu
# label = Label(root, text="STARFIGHTER", font=("Arial", 20), bg="black", fg="white")
# label.place( x= 250, y= 60)

    
class RulesScreen:
    """_summary_ : Cette classe permet d'afficher les règles du jeu
    """
    def __init__(self, master):
        self.master = master
        self.score = "0"
        self.master.geometry("700x800")
        
        self.label = Label(self.master, text="STARFIGHTER", font=("Terminal", 22), bg="black", fg="white")
        self.label.place( x= 250, y= 60)
        
        self.label2 = tk.Label(self.master, text="Règle 1 : quand tu sera de retour au menu tu ne", font=("Terminal", 13), bg="black", fg="white")
        self.label4 = tk.Label(self.master, text="peux plus afficher les règles sorry -__-", font=("Terminal", 13), bg="black", fg="white")
        self.label2.place( x= 50, y= 100)
        self.label4.place( x= 50, y= 120)
        
        self.label3 = tk.Label(self.master, text="Règle 2 : Seulement tirer un laser à la fois !!", font=("Terminal", 13), bg="black", fg="white")
        self.label3.place( x= 50, y= 160)
        
        self.button = tk.Button(self.master, text="Retour", command=returnBack, font=("Terminal",20), bg="white")
        self.button.place( x= 285, y= 700)
        
      
            
      
        
        # self.mousePosition = StringVar() # displays mouse position
        # self.mousePosition.set( "Mouse outside window" )
        # self.positionLabel = Label( self.master,textvariable =  )
        # self.positionLabel.pack( side = BOTTOM )

    
    
        
    def startit(self):
        self.master.mainloop()


app = RulesScreen(root)
app.startit()   
    
root.mainloop()          