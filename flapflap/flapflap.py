
import pgzrun
from random import randint 

WIDTH=800
HEIGHT=600

b=Actor("balloon")
b.pos=400,300

f=Actor("bird-up")
f.pos= randint(800,1600),randint(10,200)

h=Actor("house")
h.pos=randint(800,1600),460

t=Actor("tree")
t.pos=randint(800,1600),450

f_upp=True
upp=False
spelet_slut=False
summa=0
ant_upp=0

summor=[]

def upp_rek():
    global summa, summor
    filnamn=r"rek.txt"
    summor=[]
    with open (filnamn,"r")as fil:
        rad=fil.readline()
        rekorden=rad.split()
        for rekord in rekorden:
            if(summa>int(rekord)):
                summor.append(str(summa)+" ")
                summa=int(rekord)
            else:summor.append(str(rekord+" "))

    with open(filnamn,"w") as fil:
        for rek in summor:
            fil.write(rek)


def vis_rek():
    screen.draw.text("REKORD pog",(350,200),color="black")
    y=125
    position=1
    for rek in summor:
        screen.draw.text(str(position)+"."+ rek,(350,y),color="black")
        y+=25
        position+=1
        

    
def draw():
    screen.blit("background",(0,0))
    if not spelet_slut:
        b.draw()
        f.draw()
        h.draw()
        t.draw()
        screen.draw.text("Epic gamer summa:"+str(summa),(600,5),color="black")

    else:
        vis_rek()

def on_mouse_down ():
    global upp
    upp=True
    b.y-=50

def on_mouse_up():
    global upp
    upp=False

def flaxa():
    global f_upp
    if f_upp:
        f.image="bird-down"
        f_upp=False
    else:
        f.image="bird-up"
        f_upp=True

def update():
    global spelet_slut,summa,ant_upp
    if not spelet_slut:
        if not upp:
            b.y+=1
        if f.x>0:
            f.x-=4
            if ant_upp==9:
                flaxa()
                ant_upp=0
            else:
                ant_upp+=1

        else:
            f.x=randint(800,1600)
            f.y=randint(10,200)
            summa+=1
            ant_upp=0
        if h.right>0:
            h.x-=2
        else:
            h.x=randint(800,1600)
            summa+=1
        if t.right>0:
            t.x-=2
        else:
            t.x=randint(800,1600)
            summa+=1
   
   
    if b.top<0 or b.bottom>560:
            spelet_slut=True
            upp_rek()
    if not spelet_slut:
        if b.collidepoint(f.x,f.y)or b.collidepoint(h.x,h.y)or b.collidepoint(t.x,t.y):
            upp_rek()
            spelet_slut=True
           
        
        

pgzrun.go()
