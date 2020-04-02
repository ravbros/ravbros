import pgzrun
from random import randint

HOJD=600
BREDD=800
rosa=Actor("apple")
Bitar=[]

def draw():
    screen.clear
    screen.fill("blue")
    for bit in Bitar:
        bit.draw()
 

def ny_bit():
    global rosa
    rosa=Actor("apple")
    rosa.x=randint(200,600)
    rosa.y=20
    Bitar.append(rosa)




def flytta_rosa():                
    if rosa.y<500:
        rosa.y=rosa.y+20
    else:
        ny_bit()
            

def update():
    if keyboard.right:
        rosa.x=rosa.x+10
        screen.fill("blue")
    if keyboard.left:
        rosa.x=rosa.x-10
        screen.fill("black")
    

ny_bit()  
clock.schedule_interval(flytta_rosa,1)




pgzrun.go()






