import pgzrun
poäng=0
HOJD=600
BREDD=800
räv=Actor("fox")
apelsin=Actor("monster_left")
räv.x=50
räv.y=550
apelsin.x=750
apelsin.y=570
HOPP=0
speletkör=False

def draw():
    screen.clear
    screen.blit("bakgrund",(0,0))
    if speletkör:
        screen.blit("mark",(0,570))
        räv.draw()
        apelsin.draw()
        
    else:
        screen.draw.text("TRYCK PÅ MELLANSLAG FÖR EN ÖVERRASKNING",
                         center=(400,500),fontsize=30)
def börja():
    global räv,apelsin, speletkör,HOPP
    speletkör=True
    räv.x=50
    räv.y=550
    apelsin.x=750
    apelsin.y=550
    HOPP=0
    
    
def update():
    global räv,apelsin, speletkör,HOPP
    if speletkör:
        apelsin.x=apelsin.x-5
        if apelsin.x<0:
            apelsin.x=800
        if räv.y<550:
            räv.y=räv.y+5
        if räv.y==550 and keyboard.up:
            HOPP=30
        if HOPP>0:
            räv.y=räv.y-15
            HOPP=HOPP-1
            

        döden=apelsin.colliderect(räv)
        if döden:
            sounds.död.play()
            speletkör=False
        räv.x=max(10,min (räv.x, BREDD-30))
        räv.y=max(10,min (räv.y, HOJD-30))
    else:
        if keyboard.space:
            börja()
        

pgzrun.go()   
    
