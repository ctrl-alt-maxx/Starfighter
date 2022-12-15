# Starfighter
>## Auteurs
>life
## Description
Starfighter est un jeu de tir dans l'espace. Le joueur contrôle un vaisseau qui doit tirer sur des astéroïdes qui apparaissent aléatoirement. Le joueur a 3 vies. Le jeu se termine quand le joueur n'a plus de vie. Le score du joueur est le nombre d'astéroïdes qu'il a détruit. Le joueur peut sauvegarder son score dans un fichier csv.


---
### Avant l'ouverte du jeu
#### Installation de PILLOW
si le jeu ne s'ouvre pas,
la commande suivante dans le terminal permet d'installer PILLOW qui est une librairie pour python qui permet de gérer les images

> **répertoire** -m pip install pillow

---
## Page d'accueil
### *Menu.py*
    
### Commencer une partie
on appelle la méthode *startGame()* qui va détruire la fenêtre actuelle et ouvrir la fenêtre du jeu

```python
def startGame():
    root.destroy()
    import main
```

### Ouvrir les Règles
on appelle la méthode *startRules()* qui va détruire la fenêtre actuelle et ouvrir la fenêtre des règles
```python
def startRules():
     root.destroy()
     import rules
``` 
### Ouvrir le Menu des Scores
on appelle la méthode *startLeaderboard()* qui va détruire la fenêtre actuelle et ouvrir la fenêtre des scores
``` python
def startLeaderboard():
    root.destroy()
    import leaderboard
```       
### Quitter le jeu
on appelle la méthode *quitGame()* qui va détruire la fenêtre actuelle et fermer le jeu
```python
def quitGame():
    root.destroy()
```     	  
---    	 
    
## Règles
### *Rules.py*
Affiche les règles du jeu

a un bouton qui permet de revenir au menu principal
```python
def returnBack():
    root.destroy()
    import menu
```
---
## Menu des Scores
### *Leaderboard.py*
Affiche les scores des joueurs

a un bouton qui permet de revenir au menu principal

a un bouton qui permet de classer les scores


---
## Jeu
### *Main.py*
#### Initialisation
On initialise les variables suivantes:
- *root* : la fenêtre du jeu
- *canvas* : le canvas sur lequel on va dessiner
- *frame* : la frame qui contient le canvas
- *image* : l'image du vaisseau
### Classe Vaisseau
#### Attributs
- *imageVaisseau* : l'image du vaisseau
- *new_image* : l'image du vaisseau redimensionnée
#### Fonctions
left(e) : permet de déplacer le vaisseau vers la gauche
right(e) : permet de déplacer le vaisseau vers la droite
upe() : permet de déplacer le vaisseau vers le haut
down(e) : permet de déplacer le vaisseau vers le bas

move(event) : permet de déplacer le vaisseau en fonction du mouvement de la souris
```python
 def move(e):
        global image
        new = Vaisseau.imageVaisseau.resize((50,50), Image ANTIALIAS)
        image = ImageTk.PhotoImage(new)
        
        img = canvasBase.create_image(e.x, e.y, image = image)
        Vaisseau.vaisseauEdgeReached()

# Bind the move function 
canvasBase.bind("<Motion>", move) 
```
### Collision
collision() : permet de détecter la collision entre le vaisseau et un astéroïde
```python
def collision(objet):
        sb = canvasBase.bbox(Vaisseau.new_image)
        eb = canvasBase.bbox(objet)
        if eb[0] < sb[2] < eb[2] and eb[1] < sb[1] < eb[3]:
            canvasBase.move(objet, 25, -25)
            print("CONTACT BOTTOM-LEFT")
        elif eb[2] > sb[0] > eb[0] and eb[1] < sb[1] < eb[3]:
            canvasBase.move(objet, -25, -25)
            print("CONTACT BOTTOM-RIGHT")
        elif sb[1] < eb[1] < sb[3] and eb[0] < sb[2] < eb[2]:
            canvasBase.move(objet, 25, 25)
            print("CONTACT TOP-RIGHT")
        elif sb[1] < eb[1] < sb[3] and sb[0] < eb[2] < sb[2]:
            canvasBase.move(objet, -25, 25)
            print("CONTACT TOP-LEFT")
```	
### Classe Laser
moveLaser() : permet de déplacer le laser en fonction du mouvement du vaisseau
```python
  def moveLaser():
        global laser, laserLoop
        canvasBase.move(laser, 0, -10);
        laserLoop = root.after(10, Vaisseau.moveLaser)
```
##### shoot() : permet de tirer un laser
```python
 def shoot(event):
        global laser, laserLoop
        try:
            root.after_cancel(laserLoop)
            canvasBase.delete(laser)
            laser = canvasBase.create_image(event.x, event.y, image=Vaisseau.new_imgLaser);
            Vaisseau.moveLaser()
        except NameError:
            laser = canvasBase.create_image(event.x, event.y, image=Vaisseau.new_imgLaser);
            Vaisseau.moveLaser()

    canvasBase.bind_all("<1>", shoot);
```
### Classe HUD
le HUD est la barre de vie du vaisseau
#### Attributs
- *life* : la vie du vaisseau
- *score* : le score du joueur
#### Fonctions
scoreCounter() : permet d'incrémenter le score du joueur
```python
    def scoreCounter(): 
       global score
       HUD.score += 1
       print(HUD.score)
```	
### Classe HealthBar
la barre de vie du vaisseau
#### Attributs 
- *health* : la vie du vaisseau
### Classe Ovni
la classe Ovni permet de créer un ovni
#### Attributs
- *imgOvni* : l'image de l'ovni
- canvasBase : le canvas sur lequel on va dessiner
### Classe Astéroïde
la classe Astéroïde permet de créer un astéroïde
#### Attributs
- *imgAsteroide* : l'image de l'astéroïde
- canvasBase : le canvas sur lequel on va dessiner
### Classe Flash
la classe Flash permet de créer un objet flash
ce dernier permet d'accéléré le vaisseau
#### Attributs
- *imgBolt* : l'image du flash
- cansvasBase : le canvas sur lequel on va dessiner
### Classe Aid
la classe Aid permet de créer un objet aid
ce dernier permet de réparer le vaisseau
#### Attributs
- *imgAid* : l'image de l'aid
- canvasBase : le canvas sur lequel on va dessiner

