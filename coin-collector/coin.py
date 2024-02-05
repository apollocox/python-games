# Add your imports up here!

import pgzrun
from pgzero.actor import Actor
from random import randint

# setup the size of the screen and the game controls
WIDTH = 400
HEIGHT = 400
game_over = False
score = 0

# create fox
fox = Actor("fox")
fox.x = 100
fox.y = 100

# create coins
coin = Actor("coin")
coin.pos = 200, 200


# ---------------------------------------
# These are the special functions that only exist for the coin-collector game
# ---------------------------------------
def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

    # todo: keep the coin from being spawned on the fox! -zacox
    
    # todo: keep the fox from leaving the screen!

def restart():
    """
    reset the game
    """
    global score
    global game_over

    score = 0
    game_over = False

    # todo: put the fox back at the start!
    fox.x = 100
    fox.y = 100

    # todo: create a "speed" variable and set it back to the default!

    place_coin()

    # the game should end after a few seconds!
    clock.schedule(time_up, 10.0) 

def time_up():
    global game_over
    game_over = True

    # restart the game after a few seconds!
    clock.schedule(restart, 4.0) 


# ---------------------------------------
# These are the built-in functions. They are called by the pygameszero game engine!
# ---------------------------------------
def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score),color="black", topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final score: " + str(score), topleft=(10, 10), fontsize=60)


def update():
    global score
    global game_over

    speed = 7
    if game_over == False:
        if keyboard.left:
           fox.x = fox.x - speed
        elif keyboard.right:
            fox.x = fox.x + speed

        if keyboard.up:
            fox.y = fox.y - speed
        elif keyboard.down:
            fox.y = fox.y + speed   

    # check if the fox is touching a coin
    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 1
        place_coin()


restart()
pgzrun.go() # <-- all your games must have this line at the VERY bottom -zacox