from random import randint
import pygame
# import ui
# import utils
class Scene:
    def __init__(self):
        pass
    def onEnter(self):
        pass
    def onExit(self):
        pass
    def input(self, sm, inputStream):
        pass
    def update(self, sm, inputStream):
        pass
    def draw(self, sm, screen):
        pass

class MainMenuScene(Scene):
    def __init__(self):
        self.enter = ui.ButtonUI(pygame.K_RETURN, '[Enter=next]', 50, 200)
        self.esc = ui.ButtonUI(pygame.K_ESCAPE, '[Esc=quit]', 50, 250)
    def onEnter(self):
        globals.soundManager.playMusicFade('solace')
    #def input(self, sm, inputStream):
        # if inputStream.keyboard.isKeyPressed(pygame.K_RETURN):
        #     sm.push(FadeTransitionScene([self], [PlayerSelectScene()]))
        # if inputStream.keyboard.isKeyPressed(pygame.K_ESCAPE):
        #     sm.pop()
    def update(self, sm, inputStream):
        self.enter.update(inputStream)
        self.esc.update(inputStream)
    def draw(self, sm, screen):
        # background
        screen.fill(globals.DARK_GREY)
        utils.drawText(screen, 'Main Menu', 50, 50, globals.WHITE, 255)
        self.enter.draw(screen)
        self.esc.draw(screen)
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
    def __init__(self):
        super().__init__()
        self.sword_damage = 31
        self.big_sword_damage = 41
    def atack(self, target):
        ataka = input("")
        if ataka == "1":
            target.HP -= self.punch_damage
        elif ataka == "2":
            target.HP -= self.sword_damage
        elif ataka == "3":
            target.HP -= self.big_sword_damage
        if target.HP > 0 :
            return True
        else:
            return False

class Enemy:
    def __init__(self):
        #self.name = ""
        self.LVL =  0
        self.damage = 20 + 5*self.LVL
        self.HP = 150 + 25*self.LVL
    def atack(self,target):
        target.HP -= self.damage
        if target.HP > 0 :
            return True
        else:
            #target.damage = 0
            return False
hero = Hero_swordsman()
eey = Enemy()
while True:
    next = input("")
    if next == "w":
        action = randint(1,3)
        eey = Enemy()
        if action == 1:
            print ("f")
            eey.name = "Донгминяшь"
            while hero.HP > 0 and eey.HP > 0:
                rzlt=hero.atack(eey)
                if rzlt == True:
                    eey.atack(hero)
        elif action == 2:
            print("h")
            hero.HP += 75
        elif action == 3:
            print("m")
        if hero.HP <= 0:
            print("You dead")
            break
        if eey.HP <= 0:
            print("Enemy dead")