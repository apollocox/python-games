# Apollo's first apple game.
# date: january 13, 2024
# charles.apollo.cox@gmail.com


# Notes from zac!

# remember to save!

# remember to "cd" to the folder (sometimes called a "directory") of your game! 
# This will normally be "C:\Users\charl\OneDrive\Documents\python-games\shoot-the-fruit". 
# If you are in just "python-games" you will need to type "cd shoot-the-fruit" in the terminal. 
# That should fix it!

# If the terminal starts writing any wacky stuff, just type "Ctrl + c"

# If you need to get to the python prompts (they look like >>> ), just type "python" in the terminal.
# If you need to quit, you can type "ctrl+z, then enter". You can also type "exit()" and click enter.

# Add your imports up here!
import pgzrun
from pgzero.actor import Actor
from random import randint


# set up your game elements here!

winfruit = Actor("pineapple")

fruits = [
    Actor("pineapple"),
    Actor("pineapple"),
    Actor("pineapple"),
    Actor("orange"), 
    Actor("apple"),
    winfruit 
    ]

#nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

def draw():
    screen.clear()
    for f in fruits:
        f.draw()

def place_fruits():
    for f in fruits:
        f.x = randint(20,800)
        f.y = randint(20,600)

def on_mouse_down(pos):
    if winfruit.collidepoint(pos):
        print("Good shot!")
        place_fruits()
    else:
        print("Oh no! You missed!")
        # quit()

        # we missed the winfruit. 
        # find the fruit that we did click on 
        for f in fruits:
            if f.collidepoint(pos):
                # if we get here, then we knew the mouse position, "pos" collided with the "f" fruit.
                # that means the user clicked on f!
                fruits.remove(f)
                break


# setup
place_fruits()
pgzrun.go() # <-- all your games must have this line at the VERY bottom -zacox