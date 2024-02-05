import pgzrun
from pgzero.actor import Actor
import random



FONT_COLOR  = (225, 225, 225)

# scren size
WIDTH = 800
HEIGHT = 600
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)



game_over = False

# setup game pieces
# dots = []
# for dot in range(0, 11):
#     actor = Actor("dot")
#     actor.x = randint(20, WIDTH-20)
#     actor.y = randint(20, WIDTH-20)
#     dots.append(actor)
# lines = []
# next_dot = 0

# interaction functions
def on_mouse_down(pos):
    pass

        
    


# setup game loop functions
def draw():
    screen.fill("red")

def update():
    pass

pgzrun.go() # <-- all your games must have this line at the VERY bottom -zacox