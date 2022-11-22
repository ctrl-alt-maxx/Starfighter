import tkinter as tk
import csv
import random
import datetime as dt

root = tk.Tk()
root.config(background="black")
root.title("Leaderboard")
root.geometry("1500x1500")

def returnBack():
    root.destroy()
    import gameSC

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

# ACCÈS AU FICHIER
with open("StarFighter.csv", "r", newline="\n") as scorefile:
    reader = csv.reader(scorefile)
    data = list(reader)

class Trier:
    
    scoreslist = []
    def trierPointsDecroissant(self):
        """Effectue le tri pour le nombre de point en ordre décroissant

        :param self: Description du paramètre
        :type self: Trier
        """
        def Points(score):
            pts = 10000 - int(score[1])
            battu = 500 - int(score[2])
            tir = 1000 + int(score[3])
            return (pts, tir, battu)
        
        self.Scoreslist = sorted(data, key=Points)
        self.Show()
                
    def trierPointsCroissant(self):
        """Effectue le tri pour le nombre de point en ordre croissant

        :param self: Description du paramètre
        :type self: Trier
        """
        def Point(score):
            pts = 10000 + int(score[1])
            battu = 500 + int(score[2])
            tir = 1000 - int(score[3])
            return (pts, tir, battu)
        
        self.Scoreslist = sorted(data, key=Point)
        self.Show()            
    
    def trierBattuDecroissant(self):
        """Effectue le tri pour le nombre d'ennemi battu en ordre décroissant

        :param self: Description du paramètre
        :type self: Trier
        """
        def Battu(score):
            battu = 500 - int(score[2])
            tir = 1000 + int(score[3])
            return (battu, tir)
        
        self.Scoreslist = sorted(data, key=Battu)
        self.Show()

    def trierBattuCroissant(self):
        """Effectue le tri pour le nombre d'ennemi battu en ordre croissant

        :param self: Description du paramètre
        :type self: Trier
        """
        def Battu(score):
            battu = 500 + int(score[2])
            tir = 1000 - int(score[3])
            return (battu, tir)
        
        self.Scoreslist = sorted(data, key=Battu)
        self.Show()

    def trierNbTirCroissant(self):
        """Effectue le tri pour le nombre de tir en ordre croissant

        :param self: Description du paramètre
        :type self: Trier
        """
        def Tir(score):
            tir = 1000 + int(score[3])
            battu = 500 - int(score[2])
            return (tir, battu)
        self.Scoreslist = sorted(data, key=Tir)
        self.Show()
    
    def trierNbTirDecroissant(self):
        """Effectue le tri pour le nombre de tir en ordre décroissant

        :param self: Description du paramètre
        :type self: Trier
        """
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
        """Effectue le tri dans le nom des joueurs de A à Z

        :param self: Description du paramètre
        :type self: Trier
        """
        self.Scoreslist = sorted(data)
        self.Show()
                
    def trierNomZA(self):
        """Effectue le tri dans le nom des joueurs de Z à A

        :param self: Description du paramètre
        :type self: Trier
        """
        self.Scoreslist = sorted(data, reverse=True)
        self.Show()
                     
    def Show(self):
        """Montre le tri sur la fenêtre tkinter

        :param self: Description du paramètre
        :type self: Trier
        """
        for i, row in enumerate(self.Scoreslist):
            self.scoreslist.append(row[0])
            for col in range(0, 5):
                tk.Label(root, text=row[col], font=("Terminal", 11),fg="yellow",bg="black").grid(row=i+1, column=col, padx=100)
                                        
t = Trier()
# NOM DES BOUTONS SUR LE TKINTER
bouton_nom_AZ = tk.Button(root, text="Nom(A-Z)", command=t.trierNomAZ, font=("Terminal", 12),fg="red",bg="black",activebackground="red",activeforeground="black",border=3,relief="ridge")
bouton_nom_ZA = tk.Button(root, text="Nom(Z-A)", command=t.trierNomZA, font=("Terminal", 12),fg="red",bg="black",activebackground="red",activeforeground="black",border=3,relief="ridge")

bouton_pts_D = tk.Button(root, text="Points(Haut)", command=t.trierPointsDecroissant, font=("Terminal", 12),fg="red",bg="black",activebackground="red",activeforeground="black",border=3,relief="ridge")
bouton_pts_C = tk.Button(root, text="Points(Bas)", command=t.trierPointsCroissant, font=("Terminal", 12),fg="red",bg="black",activebackground="red",activeforeground="black",border=3,relief="ridge")

bouton_bat_D = tk.Button(root, text="Ennemis Détruits(Haut)", command=t.trierBattuDecroissant, font=("Terminal", 12),fg="red",bg="black",activebackground="red",activeforeground="black",border=3,relief="ridge")
bouton_bat_C = tk.Button(root, text="Ennemis Détruits(Bas)", command=t.trierBattuCroissant, font=("Terminal", 12),fg="red",bg="black",activebackground="red",activeforeground="black",border=3,relief="ridge")

bouton_tir_C = tk.Button(root, text="Nombre de Tir(Bas)", command=t.trierNbTirCroissant, font=("Terminal", 12),fg="red",bg="black",activebackground="red",activeforeground="black",border=3,relief="ridge")
bouton_tir_D = tk.Button(root, text="Nombre de Tir(Haut)", command=t.trierNbTirDecroissant, font=("Terminal", 12),fg="red",bg="black",activebackground="red",activeforeground="black",border=3,relief="ridge")
boutonRetour = tk.Button(root, text="Retour", command=returnBack, font=("Terminal", 12), fg="red",bg="black",activebackground="red",activeforeground="black",border=2,relief="ridge")

# PLACE DES BOUTONS SUR LE TKINTER
bouton_nom_AZ.place(x=10, y=550)
bouton_nom_ZA.place(x=10, y=600)

bouton_pts_D.place(x=150, y=550)
bouton_pts_C.place(x=150, y=600)

bouton_bat_D.place(x=350, y=550)
bouton_bat_C.place(x=350, y=600)

bouton_tir_C.place(x=650, y=550)
bouton_tir_D.place(x=650, y=600)
boutonRetour.place(x=0, y=0)


col_names = ("Joueur", "Points", "Ennemis Battus", "Nombre de Tir", "Date Joué")
for i, col_name in enumerate(col_names, start=0):
    tk.Label(root, text=col_name, font=("Terminal", 14),fg="red",bg="black",activeforeground="black",border=4,relief="ridge").grid(row=0, column=i, padx=80, pady=5)

t.trierPointsDecroissant()

root.mainloop()