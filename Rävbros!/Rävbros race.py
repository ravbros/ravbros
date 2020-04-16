import pgzrun
poäng=0
HOJD=600
BREDD=800
räv=Actor("fox")
apelsin=Actor("monster_left")
p=Actor("påle")
räv.x=50
räv.y=550
apelsin.x=750
apelsin.y=570
p.x=750
p.y=300
HOPP=0
speletkör=False
utekott=0

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
    if pp:
        p.draw()
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
        if utekott<10:
            apelsin.x=apelsin.x-5
            if apelsin.x<0:
                apelsin.x=800
                utekott=utekott+1
            if räv.y<550:
                räv.y=räv.y+5
            if räv.y==550 and keyboard.up:
                HOPP=30
            if HOPP>0:
                räv.y=räv.y-15
                HOPP=HOPP-1
    else:
        pp=True
        
                

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
    
