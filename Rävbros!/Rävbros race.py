import pgzrun
poäng=0
HOJD=600
BREDD=800
räv=Actor("fox")
apelsin=Actor("orange")
räv.x=50
räv.y=550
apelsin.x=750
apelsin.y=550
HOPP=0

def draw():
    
    

    screen.clear
    screen.fill("green")
    räv.draw()
    apelsin.draw()
    

    
    
def update():
    global räv,apelsin, spelet_slut,HOPP
    apelsin.x=apelsin.x-5
    if apelsin.x<0:
        apelsin.x=800
    if räv.y<550:
        räv.y=räv.y+5
    if räv.y==550 and keyboard.space:
        HOPP=30
    if HOPP>0:
        räv.y=räv.y-15
        HOPP=HOPP-1
        

    döden=apelsin.colliderect(räv)
    if döden:
        sounds.död.play()
        spelet_slut=True
            
        
    
    räv.x=max(10,min (räv.x, BREDD-30))
    räv.y=max(10,min (räv.y, HOJD-30))

pgzrun.go()   
    
