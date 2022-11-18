import tkinter as tk
import csv
import random
import datetime as dt

root = tk.Tk()
root.title("Score Table")
root.geometry("1000x1000")

# name = "Marc"
# pts = random.randrange(100,1000)
# detruit = random.randrange(25, 80)
# nbTir = random.randrange(10, 500)
# d = dt.datetime.now()

# # FICHIER CONTENANT LES TEMPS DES PARTIES PRÉCEDENTES
# f = open("StarFighter.csv", "a")
# with f:
#     fnames = ['Nom', 'Points', 'Ennemis Battus', 'Nombre de Tir', 'Date']
#     csvwriter = csv.DictWriter(f, fieldnames=fnames)
#     csvwriter.writerow( {'Nom' : name, 'Points' : pts, 'Ennemis Battus' : detruit, 'Nombre de Tir' : nbTir, 'Date' : d} ) 
# f.close()

col_names = ("Joueur", "Points", "Ennemis Battus", "Nombre de Tir", "Date Joué")
for i, col_name in enumerate(col_names, start=0):
    tk.Label(root, text=col_name).grid(row=0, column=i, padx=40)

# ACCÈS AU FICHIER
with open("StarFighter.csv", "r", newline="\n") as scorefile:
    reader = csv.reader(scorefile)
    data = list(reader)


class Trier:
    
    scoreslist = []
    col_names = ("Joueur", "Points", "Ennemis Battus", "Nombre de Tir", "Date Joué")
    for i, col_name in enumerate(col_names, start=0):
        tk.Label(root, text=col_name).grid(row=0, column=i, padx=40)
    
    def trierPointsDecroissant(self):
        def Points(score):
            pts = 10000 - int(score[1])
            battu = 500 - int(score[2])
            tir = 1000 + int(score[3])
            return (pts, tir, battu)
        
        self.Scoreslist = sorted(data, key=Points)
        self.Show()
                
    def trierPointsCroissant(self):
        def Points(score):
            pts = 10000 + int(score[1])
            battu = 500 + int(score[2])
            tir = 1000 - int(score[3])
            return (pts, tir, battu)
        
        self.Scoreslist = sorted(data, key=Points)
        self.Show()            
    
    def trierBattuDecroissant(self):
        def Battu(score):
            battu = 500 - int(score[2])
            tir = 1000 + int(score[3])
            return (battu, tir)
        
        self.Scoreslist = sorted(data, key=Battu)
        self.Show()

    def trierBattuCroissant(self):
        def Battu(score):
            battu = 500 + int(score[2])
            tir = 1000 - int(score[3])
            return (battu, tir)
        
        self.Scoreslist = sorted(data, key=Battu)
        self.Show()

    def trierNbTirCroissant(self):
        def Tir(score):
            tir = 1000 + int(score[3])
            battu = 500 - int(score[2])
            return (tir, battu)
        self.Scoreslist = sorted(data, key=Tir)
        self.Show()
    
    def trierNbTirDecroissant(self):
        def Tir(score):
            tir = 1000 - int(score[3])
            battu = 500 + int(score[2])
            return (tir, battu)
        self.Scoreslist = sorted(data, key=Tir)
        self.Show()
        
    # def Tir(score):
    #     tir = 1000 + int(score[3])
    #     battu = 500 - int(score[2])
    #     return (tir, battu)       
        
    def trierNomAZ(self):
        self.Scoreslist = sorted(data)
        self.Show()
                
    def trierNomZA(self):
        self.Scoreslist = sorted(data, reverse=True)
        self.Show()
                     
    def Show(self):
        for i, row in enumerate(self.Scoreslist):
            scoreslist.append(row[0])
            for col in range(0, 5):
                tk.Label(root, text=row[col]).grid(row=i+1, column=col, padx=100)
                                        
t = Trier()

bouton_nom_AZ = tk.Button(root, text="Nom (A-Z)", command=t.trierNomAZ)
bouton_nom_ZA = tk.Button(root, text="Nom (Z-A)", command=t.trierNomZA)

bouton_pts_D = tk.Button(root, text="Points (Décroissant)", command=t.trierPointsDecroissant)
bouton_pts_C = tk.Button(root, text="Points (Croissant)", command=t.trierPointsCroissant)

bouton_bat_D = tk.Button(root, text="Ennemis Détruits (Décroissant)", command=t.trierBattuDecroissant)
bouton_bat_C = tk.Button(root, text="Ennemis Détruits (Croissant)", command=t.trierBattuCroissant)

bouton_tir_C = tk.Button(root, text="Nombre de Tir (Croissant)", command=t.trierNbTirCroissant)
bouton_tir_D = tk.Button(root, text="Nombre de Tir (Décroissant)", command=t.trierNbTirDecroissant)


bouton_nom_AZ.place(x=10, y=850)
bouton_nom_ZA.place(x=10, y=900)

bouton_pts_D.place(x=200, y=850)
bouton_pts_C.place(x=200, y=900)

bouton_bat_D.place(x=400, y=850)
bouton_bat_C.place(x=400, y=900)

bouton_tir_C.place(x=600, y=850)
bouton_tir_D.place(x=600, y=900)
    

scoreslist = []
for i, row in enumerate(data):
    scoreslist.append(row[0])
    for col in range(0, 5):
        tk.Label(root, text=row[col]).grid(row=i+1, column=col, padx=100)      

root.mainloop()