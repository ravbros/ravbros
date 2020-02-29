import pgzrun

mario=Actor("mario")
stjarna=Actor("stjärna")

def draw():
    screen.fill("sky blue")
    mario.draw()
def placera_mario():
    mario.x=100
    mario.y=100
    

if  keyboard.up:
    mario.x=mario.x+4
    
    



















pgzrun.go()
