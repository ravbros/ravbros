import pgzrun
BREDD=400
HOJD=400
prickar=[]
linjer=[]

kommande_prick=0

for prick in range(0,10):
    aktor=Actor("hedgehog")
    aktor.pos=randint(20,BREDD-20),randint(20, HOJD-20)
    prickar.append(aktor)

def draw():
    screen.fill("lawn green")
    siffra=1
    for prick in prickar:
            screen.draw.text(str(siffra),(prick.pos[0],prick.pos[1]+12))
    







pgzrun.go()
