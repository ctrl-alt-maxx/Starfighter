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
    
def trier(score):
    pts = 10000 - int(score[1])
    # battu = 500 - int(score[2])
    return (pts)    
    
Scoreslist = sorted(data, key=trier)

scoreslist = []
for i, row in enumerate(Scoreslist):
    scoreslist.append(row[0])
    for col in range(0, 5):
        tk.Label(root, text=row[col]).grid(row=i+1, column=col, padx=100)  
    

# print(scoreslist, end='\n\n')

root.mainloop()