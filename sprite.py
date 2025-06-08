import pygame
import globals
from random import randint
clock = pygame.time.Clock()
grey = (153,153,153)
class Player(pygame.sprite.Sprite):
    def __init__(self,game, x, y,sprite_w,sprite_h, filename):
        self.game = game
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        print(self.rect)
        self.rect.height = sprite_h
        self.rect.width = sprite_w
        print(self.rect)
        self.image = pygame.transform.scale(
            self.image, (self.rect.width,self.rect.height))
    def update(self):
        pass
# width = 700
# height = 700
# screen = pygame.display.set_mode((width,height))
# run = True
# nedo_hero = Sprite(100,320,200,200,"лупа(спрайт).png")
# Enemy = Sprite(1000,550,200,200,"пупа(тоже спрайт).jpg")
# while run :
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         #elif event.type ==
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 nedo_hero.rect.x += 20
#     screen.fill(grey)
#     #scene.draw()
#     #pygame.draw.rect(screen,black,(300,300,100,100))
#     screen.blit(nedo_hero.image,nedo_hero.rect)
#     screen.blit(Enemy.image,Enemy.rect)
#     pygame.display.update()
#     clock.tick(30)