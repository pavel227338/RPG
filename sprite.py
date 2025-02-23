import pygame
from random import randint
clock = pygame.time.Clock()
grey = (153,153,153)
class Hero_sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
width = 700
height = 700
screen = pygame.display.set_mode((width,height))
run = True
nedo_hero = Hero_sprite(200,200,"HKEHE.png")
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        #elif event.type ==     
    screen.fill(grey)
    #scene.draw()
    #pygame.draw.rect(screen,black,(300,300,100,100))
    screen.blit(nedo_hero.image,nedo_hero.rect)
    pygame.display.update()
    clock.tick(30)