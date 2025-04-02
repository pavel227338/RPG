from random import randint
import pygame
import sprite
# class Scene:
#     def __init__(self):
#         pass
#     def onEnter(self):
#         pass
#     def onExit(self):
#         pass
#     def input(self, sm, inputStream):
#         pass
#     def update(self, sm, inputStream):
#         pass
#     def draw(self, sm, screen):
#         pass

# class MainMenuScene(Scene):
#     def __init__(self):
#         self.enter = ui.ButtonUI(pygame.K_RETURN, '[Enter=next]', 50, 200)
#         self.esc = ui.ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 250)
#     def onEnter(self):
#         globals.soundManager.playMusicFade('solace')
#     #def input(self, sm, inputStream):
#         # if inputStream.keyboard.isKeyPressed(pygame.K_RETURN):
#         #     sm.push(FadeTransitionScene([self], [PlayerSelectScene()]))
#         # if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
#         #     sm.pop()
#     def update(self, sm, inputStream):
#         self.enter.update(inputStream)
#         self.esc.update(inputStream)
#     def draw(self, sm, screen):
#         # background
#         screen.fill(globals.DARK_GREY)
#         utils.drawText(screen, 'Main Menu', 50, 50, globals.WHITE, 255)
#         self.enter.draw(screen)
#         self.esc.draw(screen)
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
class Hero_swordsman(Hero):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.sword_damage = 31
        self.big_sword_damage = 41
        #self.sprite = sprite.Sprite(100,320,200,200,"лупа(спрайт).png")
    def atack(self, target):
        target.HP -= self.punch_damage
        if target.HP > 0 :
            return True
        else:
            return False
    def draw(self):
        pygame.draw.rect(self.game.screen,(255,255,255),(300,300,100,100))
    def fight(self,target):
        print ("f")
        target.name = "Донгминяшь"
        while self.HP > 0 and target.HP > 0:
            rzlt=self.atack(target)
            if rzlt == True:
                target.atack(self)

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
# hero = Hero_swordsman()
# eey = Enemy()
# width = 700
# height = 700
# screen = pygame.display.set_mode((width,height))
# run = True
# while run :
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#         #elif event.type ==
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 hero.sprite.rect.x += 20
#                 print(hero.sprite.rect.x)
#                 if hero.sprite.rect.x >= 360:
#                     # hero.fight(eey)
#                     print ("f")
#                     eey.name = "Донгминяшь"
#                     while hero.HP > 0 and eey.HP > 0:
#                         rzlt=hero.atack(eey)
#                         print(eey.HP)
#                         if rzlt == True:
#                             eey.atack(hero)
#                             print(hero.HP)
#                         else:
#                              eey.sprite.image = 