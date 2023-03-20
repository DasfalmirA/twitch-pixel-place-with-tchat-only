# twitch-pixel-place-with-tchat-only

[FR]
-------------------------------------
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

[EN]
-------------------------------------
Program that allows to have a 640 x 360 window

Which uses a connection with twitchio to get the messages from the chat to be able to process them and thus put a pixel on the screen.

For censorship you can right click on the window to create a white circle.

An image will be created in the folder where main.py is located. If you wish 

A sound will be played at each pixel according to its brightness (the sum of red, green, blue) the brighter the colour, the higher the note.

For a pixel to be placed on the chat, it is important to write correctly:

#FFFFFF;10;20

-> Here #FFFFFF corresponds to the hexadecimal value of the colour.

-> Here 10 corresponds to the value in X, i.e. the horizontal position (in width)

-> Here 20 corresponds to the Y value, i.e. the vertical position (height)
Note that the X and Y values cannot exceed the length and width of the screen and be below 0.



Other examples:

#FF0000;1;0 -> Places a red pixel at x = 1 and y = 0

#00FF00;1;2 -> Place a green pixel in X = 1 and y = 2



The changes for you :

- [ESSENTIAL] You MUST put your login token and your channel name in myAuthTwitch.py 

- You can modify the values in main.py l.l7 and l.18 for the length and height
- change the radius of the censor circle main.py l.20
- you can remove the audio part by commenting out the l.97 of main.py, (use a # in front of the line)
- you can write a different text to explain the program in l.55, the sentences in inverted commas.
- you can modify the functions in main.py : loadsave() in l.134 and save_and_quit() in l.149 to modify the path and name of the files to save the image
