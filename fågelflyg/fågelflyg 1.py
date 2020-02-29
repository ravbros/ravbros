import pgzrun
WIDTH=800
HEIHT=600
fågel=Actor("bird-up")
fågel.pos=(10,300)

träd=Actor("tree")
träd.pos=(800,600)

def draw():
    screen.clear()
    fågel.draw()
    träd.draw


