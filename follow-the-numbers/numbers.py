import pgzrun
from pgzero.actor import Actor
from random import randint

# scren size
WIDTH = 400
HEIGHT = 400
game_over = False
# setup game pieces
dots = []
for dot in range(0, 11):
    actor = Actor("dot")
    actor.x = randint(20, WIDTH-20)
    actor.y = randint(20, WIDTH-20)
    dots.append(actor)


lines = []


next_dot = 0

# interaction functions
def on_mouse_down(pos):
    global next_dot
    global lines
    global game_over

    if next_dot < len(dots) and dots[next_dot].collidepoint(pos):
        if next_dot > 0: # we don't want to have a negative number for the line starting point!
            lines.append( (dots[next_dot - 1].pos, dots[next_dot].pos) )
        next_dot = next_dot + 1
        if next_dot == 11:
            game_over = True
    else:
        lines = []
        next_dot = 0

        
    


# setup game loop functions
def draw():
    screen.fill("yellow")
    number = 1
    for dot in dots:
        dot.draw()
        screen.draw.text(str(number), color="red", center=(dot.x + 15,dot.y + 15))
        number = number + 1

    for line in lines:
        screen.draw.line(line[0],line[1], (0,0,100))
        
    if game_over:
        screen.fill("pink")
        screen.draw.text("YOU WIN!! ", topleft=(10, 10), fontsize=60)



def update():
    pass

pgzrun.go() # <-- all your games must have this line at the VERY bottom -zacox