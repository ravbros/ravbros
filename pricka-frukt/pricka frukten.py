import pgzrun
from random import randint
apple=Actor("apple")
orange=Actor("orange")
frukt=apple
poäng=0
NOOBS=[]

def draw():
    screen.clear()
    frukt.draw()
    screen.draw.text(str(poäng),topleft =(10,10))
    for n in NOOBS:
            screen.draw.text("NOOB",topleft=n)
                
def placera_frukt():
    frukt.x=randint(10, 800)
    frukt.y=randint(10, 600)
    
def on_mouse_down(pos):
    global poäng,frukt
    if frukt.collidepoint(pos):
        poäng=poäng+1
        if poäng%2==0:
            frukt=orange
        else:
            frukt=apple
        print("Snyggt skott! Du fick ett poäng.")
        placera_frukt()
    else:
        print ("Du är en noob")
        poäng=poäng-1 
        x=0
        while x<1:
                NOOBS.append((randint(10,800),randint (10,600)))
                x=x+1
    if poäng<-10:
        poäng=0
        screen.draw.text("SLUTA!!!!!!!", center=(270,370))
        
                



placera_frukt()



pgzrun.go()
