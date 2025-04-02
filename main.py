import pygame as p
import classes
import globals
# screen = p.display.set_mode((globals.width,height))
# screen.fill(grey)
# p.draw.rect(screen,black,(350,350,100,100))
#scene = classes.MainMenuScene()
# run = True
# while run :
#     for event in p.event.get():
#         if event.type == p.QUIT:
#             run = False
#         #elif event.type ==     
#     screen.fill(grey)
#     #scene.draw()
#     p.draw.rect(screen,black,(300,300,100,100))
class Game:
    def __init__(self):
        p.init()
        self.clock = p.time.Clock()
        self.screen = p.display.set_mode((globals.width, globals.height))
    def new_game(self):
        self.playing = True# все спрайты
        self.hero = classes.Hero_swordsman(self)

    def events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                self.playing = False
            # elif event.type == p.KEYDOWN:
            #     if event.key == p.K_RIGHT:
                    # self.hero.rect.x += 20

    def update(self):
        p.display.update()

    def draw(self):
        self.screen.fill(globals.grey)
        self.hero.draw()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(globals.FPS)
g = Game()
g.new_game()
g.main()
p.quit()