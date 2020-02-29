import pgzrun
from random import randint
börjat=False
BREDD=800
HOJD=600
summa=0
spelet_slut=False
mynt=Actor("coin")
rav=Actor("fox")

maxpoäng=0
def placera_grej(grej):
    while True:
        grej.x=randint(20,(BREDD-20))
        grej.y=randint(20,(HOJD-20))
        if not grej.colliderect(rav):
            break


def skapa_igelkott():
    igel=Actor("hedgehog")
    igel.riktning=1
    placera_grej(igel)
    return igel
igelkott=[skapa_igelkott()]
def flytta_igelkott():
    for i in igelkott:
        i.riktning=randint(1,5)

     

          
     
    

def draw():
    if not börjat:
        screen.fill("blue")
        screen.draw.text(
            "Rävbros: 1.0 ",topleft=(270,100),fontsize=60)
        screen.draw.text("Design&Programming Tage Ekman, Lead testing Harry Ekman\n"
                         "Assistant programming Carl Ekman, Technical Expertise Erik Ekman", topleft=(200, 500))
        screen.draw.text(
            "Tryck på mellanslag för att starta!",center=(400,400),
            fontsize=60)
        
        rav.draw() 
        
    elif spelet_slut:
        screen.fill("red")
        screen.draw.text("Spelet är slut! Slutsumma: "+str(summa), topleft=(10,10),fontsize=60)
        screen.draw.text("BÄSTA POÄNGEN:"+str(maxpoäng), topleft=(10,510),fontsize=60)
    else:
        screen.blit("p",(0,0))
        rav.draw()
        mynt.draw()
                 
        
        for i in igelkott:
            i.draw()
        screen.draw.text("summa: " + str(summa), color="blue", topleft=(10,10))
        


def börja_om():
    global rav,spelet_slut,summa,börjat,igelkott
    rav.pos=100,100
    summa=0
    spelet_slut=False
    placera_grej(mynt)
    igelkott=igelkott[:1]
    placera_grej(igelkott[0])
    music.play("mario")
    börjat=True
                     


def update():
    global summa,spelet_slut,igelkott,börjat,maxpoäng
    if keyboard.left:
        rav.x=rav.x-2
        rav.image="fox_left"
    if keyboard.right:
        rav.x=rav.x+2
        rav.image="fox"
    if keyboard.up:
        rav.y=rav.y-2
    if keyboard.down:
        rav.y=rav.y+2
    rav.x=max(10,min (rav.x, BREDD-30))
    rav.y=max(10,min (rav.y, HOJD-30))
   
    for i in igelkott:
        if i.riktning==1:
            i.x=max(0,min (i.x+3, BREDD-20) )
            i.image="hedgehog"
        if i.riktning==2:
             i.x=max(0,min (i.x-3, BREDD-20) )
             i.image="hedgehog_left"
        if i.riktning==3:
            i.y=max(0,min (i.y+3, HOJD-20) )
        if i.riktning==4:
             i.y=max(0,min (i.y-3, HOJD-20) )
        if i.riktning==5:
             i.y=max(0,i.y)
                     
        farlig_igelkott=i.colliderect(rav)
        if farlig_igelkott and not spelet_slut and börjat:
            music.stop()
            sounds.död.play()
            spelet_slut=True
        if summa>maxpoäng:
            maxpoäng=summa
       
            
            
        
    insamlade_mynt=rav.colliderect(mynt) 
    

    if insamlade_mynt and not spelet_slut and börjat:
            summa=summa+10
            if summa > 0 and summa %100 == 0:

        
        
                
               sounds.level.play()
               igelkott.append(skapa_igelkott())
            else:
               sounds.mynt.play()
            placera_grej(mynt)
    if spelet_slut and keyboard.space:
        börja_om()
    if not börjat and keyboard.space:   
        börja_om()

    
    

sounds.start.play()
rav.pos=400,250
clock.schedule_interval(flytta_igelkott,0.25)





















pgzrun.go()

