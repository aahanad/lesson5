import pgzrun
WIDTH=600
HEIGHT=500
flower=Actor("flower")
flower.x=250
flower.y=300
bee=Actor("bee")
bee.x=175
bee.y=400
def draw():
    screen.fill("cornflower blue")
    screen.blit("grass",(0,0))
    bee.draw()
    flower.draw()
    
pgzrun.go()


#Complete the methods to place the flower bee and on the screen , refer lesson 3 to view how to make actors