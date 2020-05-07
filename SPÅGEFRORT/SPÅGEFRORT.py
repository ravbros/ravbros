import pgzrun
WIDTH=1280
HEIGHT=720

huvudruta=Rect(0,0,820,240)
timerruta=Rect(0,0,240,240)
svarsruta1=Rect(0,0,495,165)
svarsruta2=Rect(0,0,495,165)
svarsruta3=Rect(0,0,495,165)
svarsruta4=Rect(0,0,495,165)

huvudruta.move_ip(50,40)
timerruta.move_ip(990,40)
svarsruta1.move_ip(50,358)
svarsruta2.move_ip(735,358)
svarsruta3.move_ip(50,538)
svarsruta4.move_ip(738,538)
svarsrutor=[svarsruta1,svarsruta2,svarsruta3,svarsruta4]

def draw():
    screen.fill("dim grey")
    screen.draw.filled_Rect(huvudruta, "sky blue")
    screen.draw.filled_Rect(timerruta, "sky blue")

    for ruta in svarsrutor:
        screen.draw.filled_Rect(ruta,"orange")

def spelet_slut():
    pass

def ratt_svar():
    pass

def on_mouse_down(pos):
    pass

def uppdatera_tid_kvar():











    pgzrun.go
