import pygame as p
import classes
p.init()
width = 700
height = 700
FPS = 30
clock = p.time.Clock()
blue_2 = (0,0,255)
blye = (153,204,255)
white = (255,255,255)
yellow = (255,255,0)
teal = (102,255,255)
green = (0,255,0)
black = (0,0,0)
grey = (153,153,153)
red = (255,0,0)
screen = p.display.set_mode((width,height))
screen.fill(grey)
p.draw.rect(screen,black,(350,350,100,100))
#scene = classes.MainMenuScene()
run = True
while run :
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False
        #elif event.type ==     
    screen.fill(grey)
    #scene.draw()
    p.draw.rect(screen,black,(300,300,100,100))
    p.display.update()
    clock.tick(FPS)
p.quit()