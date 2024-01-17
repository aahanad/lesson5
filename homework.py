import pgzrun
import random
WIDTH=600
HEIGHT=500
flower=Actor("flower")
flower.x=250
flower.y=300
bee=Actor("bee")
bee.x=175
bee.y=400
mouse=Actor("mouse")
mouse.x=360
mouse.y=400
score=0
score2=0
game=True
def draw():
    screen.fill("cornflower blue")
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    mouse.draw()
    screen.draw.text(str(score),color="lime green",topleft=(15,15))
    screen.draw.text(str(score2),color="lime green",topright=(550,15))
    if game==False:
        screen.fill("lightsage")
        screen.draw.text(("GAME OVER!"),color="tomato",center=(250,300))

def update():
    global score
    global score2
    if keyboard.up:
        bee.y-=10
    if keyboard.down:
        bee.y+=10
    if keyboard.left:
        bee.x-=10
    if keyboard.right:
        bee.x+=10
    if bee.colliderect(flower):
        flower.x=random.randint(50,475)
        flower.y=random.randint(50,350)
        score=score+1
    if keyboard.w:
        mouse.y-=10
    if keyboard.s:
        mouse.y+=10
    if keyboard.a:
        mouse.x-=10
    if keyboard.d:
        mouse.x+=10
    if mouse.colliderect(flower):
        flower.x=random.randint(50,475)
        flower.y=random.randint(50,350)
        score2=score2+1
def time_up():
    global game
    game=False
clock.schedule(time_up,60.0) 

pgzrun.go()


