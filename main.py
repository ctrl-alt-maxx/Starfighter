
import tkinter as tk 
from tkinter import Frame, PhotoImage, Label
from PIL import ImageTk, Image  


#import sys
#print(sys.executable)

root = tk.Tk()



# COULEUR DE FOND       
root.config(background="black")

# AJOUTER UN TITRE A LA FENETRE TKINTER
root.title("Starfighter")

# FIXE LA TAILLE EN PIXEL 
root.geometry("1000x1000")

frame = Frame(root)
frame.pack()

# CREATION DU CANVAS 
canvasBase = tk.Canvas(root, background="black", width=400, height=400)
canvasBase.pack()

class Vaisseau:
    #def __init__(self, master):
    #    self.master = master

        # Creation d,un widget Canvas (zone graphique)
    #    self.vaisseauImg = PhotoImage(file = "vaisseau1.png")
    #    self.labelImg = Label(self.master, i=self.vaisseauImg)
    #    self.labelImg.pack()

    #def start(self):
    #    self.master.mainloop()

    imageVaisseau = Image.open("vaisseau.png")
    test = ImageTk.PhotoImage(imageVaisseau)

    #Resize the Image using resize method
    #resized_image = imageVaisseau.resize((300,220), Image.ANTIALIAS)
    #new_image = ImageTk.PhotoImage(resized_image)


    label1 = tk.Label(image=test)
    label1.image = test

    #canvasBase.create_image(0, 0, image=imageVaisseau)

    # Position image
    label1.place(x=4, y=4)

  


#if __name__ == "__main__":
#    app = Vaisseau(root)
#    app.start()

root.mainloop()
