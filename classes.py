from random import randint
import pygame
import sprite
import time
#TODO надо сделать класс платформы и хилки
class Hero:
    def __init__(self):
        #self.name = ""
        self.punch_damage = 20
        self.HP = 150
    def atack(self,target):
        ataka = input("")
        target.HP -= self.punch_damage
        if target.HP > 0 :
            return True
        else:
            return False
class Hero_swordsman(pygame.sprite.Sprite):
    def __init__(self,game,sprite_w,sprite_h,filename,x,y):
        self.HP = 150
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        #print(self.rect)
        self.rect.height = sprite_h
        self.rect.width = sprite_w
        #print(self.rect)
        self.image = pygame.transform.scale(
            self.image, (self.rect.width,self.rect.height))
        self.game = game
        self.damage = 41
        #self.sprite = sprite.Sprite(100,320,200,200,"лупа(спрайт).png")
    def atack(self, target):
        target.HP -= self.damage
        if target.HP > 0 :
            return True
        else:
            return False
    def draw(self):
        #pygame.draw.rect(self.game.screen,(255,255,255),(50,300,100,100))
        self.game.screen.blit(self.image,self.rect)
    def fight(self,target):
        target.name = "Донгминяшь"
        while self.HP > 0 and target.HP > 0:
            rzlt=self.atack(target)
            if rzlt == True:
                target.atack(self)
            print(target.HP)
            time.sleep(1)
        print("НКЕНЕ")
        if target.HP <= 0:
            target.__del__()
    def check_collision(self,object):
        if self.rect.colliderect(object.rect):
            return True
        return False
    def __del__(self):
      print ("Object gets destroyed")
class platform(pygame.sprite.Sprite):
    def __init__(self,game,sprite_w,sprite_h,filename,x,y,hero):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        #print(self.rect)
        self.rect.height = sprite_h
        self.rect.width = sprite_w
        #print(self.rect)
        self.image = pygame.transform.scale(
            self.image, (self.rect.width,self.rect.height))
        self.game = game
        self.hero = hero
    def draw(self):
        #pygame.draw.rect(self.game.screen,(255,255,255),(50,300,100,100))
        self.game.screen.blit(self.image,self.rect)
    def heal_you(self):
        self.hero.HP += 50
    def poison_you(self):
        self.hero.HP -= 50
class Enemy:
    def __init__(self):
        #self.name = ""
        self.LVL =  0
        self.damage = 20 + 5*self.LVL
        self.HP = 150 + 25*self.LVL
        self.sprite = sprite.Sprite(1000,550,200,200,"пупа(тоже спрайт).jpg")
    def atack(self,target):
        target.HP -= self.damage
        if target.HP > 0 :
            return True
        else:
            #target.damage = 0
            return False
class granizza:
    def __init__(self):
        self.rect = pygame.Rect(690,0,10,700)