# Add your imports up here!

import pgzrun
from pgzero.actor import Actor
from random import randint
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("score: "+str(score),color="black", topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final score: " + str(score), topleft=(10, 10), fontsize=60)


def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))



def time_up():
    global game_over
    game_over = True

def update():
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2

clock.schedule(time_up, 7.0)
place_coin()





pgzrun.go() # <-- all your games must have this line at the VERY bottom -zacox