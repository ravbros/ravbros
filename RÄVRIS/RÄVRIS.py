import pgzrun
from random import randint

HOJD=600
BREDD=800
rosa=Actor("spak")
Bitar=[]
endgame=False
def draw():
    global endgame
    screen.clear
    screen.fill("blue")
    for bit in Bitar:
        bit.draw()
    if endgame==True:
        screen.blit("endgame",(0,0))       
         

def ny_bit():
    global rosa
    rosa=Actor("spak")
    rosa.x=randint(200,600)
    rosa.y=20
    Bitar.append(rosa)




def flytta_rosa():
    global endgame
    if not endgame:
        if rosa.y<510:
            rosa.y=rosa.y+20
        else:
            ny_bit()
                

def update():
    global endgame
    if endgame==False:
            krocka=False
            if keyboard.right:
                rosa.x=rosa.x+10
            if keyboard.left:
                rosa.x=rosa.x-10
            if keyboard.down:
                rosa.y=rosa.y+10
            for bit in Bitar:
                if bit==rosa:
                    continue
                krockabit=rosa.colliderect(bit)
                if krockabit:
                    krocka=True
            if krocka:
                if rosa.y<100:
                    endgame=True
                else:
                    ny_bit()
        
        
ny_bit()  
clock.schedule_interval(flytta_rosa,1)





pgzrun.go()






