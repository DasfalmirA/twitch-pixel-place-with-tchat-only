# twitch-pixel-place-with-tchat-only

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


- You can modify the values in config.py for : the length and height ; change the radius of the censor circle

- you can remove the audio part by commenting out the l.26 of process_messages.py, (use a # in front of the line)

- you can write a different text to explain the program in twitch_bot l.26, the sentences in inverted commas.

- you can modify the functions in main.py : loadsave() and save_and_quit() to modify the path and name of the files to save the image (l.29 , l.30, l.33, l.43)
