# Starfighter
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
     	 
    
## Règles
### *Rules.py*
Affiche les règles du jeu

## Menu des Scores
### *Leaderboard.py*
Affiche les scores des joueurs

## Jeu
### *Main.py*
#### Initialisation
On initialise les variables suivantes:
- *root* : la fenêtre du jeu
- *canvas* : le canvas sur lequel on va dessiner
- *frame* : la frame qui contient le canvas
#### Fonctions
##### move(event) : permet de déplacer le vaisseau en fonction du mouvement de la souris
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
##### moveLaser() : permet de déplacer le laser en fonction du mouvement du vaisseau
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
##### vaisseauEdgeReached() : permet de vérifier si le vaisseau est au bord de l'écran
```python
 def vaisseauEdgeReached():
        shipBoundary = canvasBase.bbox(Vaisseau)
        shipLeft = shipBoundary[0]
        shipRight = shipBoundary[2]
        shipTop = shipBoundary[1]
        shipBottom = shipBoundary[3]

        if shipLeft < 0:
            canvasBase.move(Vaisseau, 10, 0)
        elif shipTop < 0:
            canvasBase.move(Vaisseau, 0, 10)
```	
