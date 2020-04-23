import pgzrun
f=Actor("fox-kopia")
f.y=300
f.x=400





def draw():
    screen.blit("bg",(0,0))
    f.draw()

def update():
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
           






























pgzrun.go()
