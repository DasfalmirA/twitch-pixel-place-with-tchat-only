# twitch-pixel-place-with-tchat-only

Programme qui permet d'avoir une fenêtre de 640 x 360

Qui utilise une connexion avec twitchio pour récupérer les messages du tchat pour pouvoir les traiter et ainsi poser un pixel sur l'écran.

Pour la censure vous pouvez faire un click droit sur la fenêtre pour créer un cercle blanc.

Une image sera créée dans le dossier où se trouve le main.py. Si vous souhaitez

Un son sera joué à chaque pixel en fonction de son intensité lumineuse (la somme du rouge, vert, bleu) plus la couleur est claire, plus la note sera aigue.

Pour qu'un pixel soit posé sur le tchat, il est important d'écrire correctement :

#FFFFFF;10;20

-> Ici #FFFFFF correspond à la valeur hexadécimale de la couleur.

-> Ici 10 correspond à la valeur en X, c'est-à-dire la position horizontale (en largeur)

-> Ici 20 correspond à la valeur en Y, c'est-à-dire la position verticale (en hauteur)
Il est à noter que les valeurs X et Y ne peuvent dépasser la longueur et largeur de l'écran et être en dessous de 0.

Autres exemples:

#FF0000;1;0 -> Place un pixel rouge en x = 1 et y = 0

#00FF00;1;2 -> Place un pixel vert en X = 1 et y = 2

Les modifications pour vous :

- [IMPORTANT] Vous DEVEZ mettre votre token d'identification et votre nom de chaîne dans myAuthTwitch.py

- Vous pouvez modifier les valeurs dans main.py l.l7 et l.18 pour la longueur et hauteur
- modifier le radius du cercle de la censure main.py l.20
- vous pouvez enlever la partie audio en mettant en commentaire la l.97 du main.py, (utilisez un # devant la ligne)
- vous pouvez écrire un texte différent pour expliquer le programme en l.55 , les phrases entre guillemets.
- vous pouvez modifier les fonctions dans main.py : loadsave() en l.134 et save_and_quit() en l.149 pour modifier le chemin et nom des fichiers de sauvegardes de l'image
