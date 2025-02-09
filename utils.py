import pygame
import engine
import globals

DARK_GREY = (50,50,50)
MUSTARD = (209,206,25)
BLACK = (0,0,0)

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 24)

# function from:
# https://nerdparadise.com/programming/pygameblitopacity
def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)

def drawText(screen, t, x, y, fg, alpha):
    text = font.render(t, True, fg)
    text_rectangle = text.get_rect()
    text_rectangle.topleft = (x,y)

    blit_alpha(screen, text, (x,y), alpha)

heart_image = pygame.image.load('images/heart.png')

def setHealth(entity):
    if entity.battle:
        entity.battle.lives = 3

def setInvisible(entity):
    if entity.animations:
        entity.animations.alpha = 50

def endInvisible(entity):
    if entity.animations:
        entity.animations.alpha = 255

powerups = ['health', 'invisible']

powerupImages = {
    'health' : [pygame.image.load('images/powerup_health.png')],
    'invisible' : [pygame.image.load('images/powerup_invisible.png')]
}

powerupSound = {
    'health' : 'coin',
    'invisible' : 'coin'
}

powerupApply = {
    'health' : setHealth,
    'invisible' : setInvisible
}

powerupEnd = {
    'health' : None,
    'invisible' : endInvisible
}

powerupEffectTimer = {
    'health' : 0,
    'invisible' : 1000
}

def makePowerup(type, x, y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,40,40)
    entityAnimation = engine.Animation(powerupImages[type])
    entity.animations.add('idle', entityAnimation)
    entity.effect = engine.Effect(
        powerupApply[type], 
        powerupEffectTimer[type],
        powerupSound[type],
        powerupEnd[type]
    )
    return entity    

coin0 = pygame.image.load('images/coin_0.png')
coin1 = pygame.image.load('images/coin_1.png')
coin2 = pygame.image.load('images/coin_2.png')
coin3 = pygame.image.load('images/coin_3.png')
coin4 = pygame.image.load('images/coin_4.png')
coin5 = pygame.image.load('images/coin_5.png')

def makeCoin(x,y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,23,23)
    entityAnimation = engine.Animation([coin1, coin2, coin3, coin4, coin5])
    entity.animations.add('idle', entityAnimation)
    entity.type = 'collectable'
    return entity

enemy0 = pygame.image.load('images/spike_monster.png')

def makeEnemy(x,y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,50,26)
    entityAnimation = engine.Animation([enemy0])
    entity.animations.add('idle', entityAnimation)
    entity.type = 'dangerous'
    return entity

playing = pygame.image.load('images/playing.png')
not_playing = pygame.image.load('images/not_playing.png')

idle0 = pygame.image.load('images/vita_00.png')
idle1 = pygame.image.load('images/vita_01.png')
idle2 = pygame.image.load('images/vita_02.png')
idle3 = pygame.image.load('images/vita_03.png')

walking0 = pygame.image.load('images/vita_04.png')
walking1 = pygame.image.load('images/vita_05.png')
walking2 = pygame.image.load('images/vita_06.png')
walking3 = pygame.image.load('images/vita_07.png')
walking4 = pygame.image.load('images/vita_08.png')
walking5 = pygame.image.load('images/vita_09.png')

def setPlayerCameras():

    # 1 player game
    if len(globals.players) == 1:
        p = globals.players[0]
        p.camera = engine.Camera(10,10,810,810)
        p.camera.setWorldPos(p.position.initial.x, p.position.initial.y)
        p.camera.trackEntity(p)
    
    # 2 player game
    if len(globals.players) == 2:
        p1 = globals.players[0]
        p1.camera = engine.Camera(10,10,400,810)
        p1.camera.setWorldPos(p1.position.initial.x, p1.position.initial.y)
        p1.camera.trackEntity(p1)

        p2 = globals.players[1]
        p2.camera = engine.Camera(420,10,400,810)
        p2.camera.setWorldPos(p2.position.initial.x, p2.position.initial.y)
        p2.camera.trackEntity(p2)

    # 3 or 4 player game
    if len(globals.players) >= 3:
        p1 = globals.players[0]
        p1.camera = engine.Camera(10,10,400,400)
        p1.camera.setWorldPos(p1.position.initial.x, p1.position.initial.y)
        p1.camera.trackEntity(p1)

        p2 = globals.players[1]
        p2.camera = engine.Camera(420,10,400,400)
        p2.camera.setWorldPos(p2.position.initial.x, p2.position.initial.y)
        p2.camera.trackEntity(p2)

        p3 = globals.players[2]
        p3.camera = engine.Camera(10,420,400,400)
        p3.camera.setWorldPos(p3.position.initial.x, p3.position.initial.y)
        p3.camera.trackEntity(p3)

        if len(globals.players) == 4:
            p4 = globals.players[3]
            p4.camera = engine.Camera(420,420,400,400)
            p4.camera.setWorldPos(p4.position.initial.x, p4.position.initial.y)
            p4.camera.trackEntity(p4)

def resetPlayer(entity):
    entity.score.score = 0
    entity.battle.lives = 3
    entity.position.rect.x = entity.position.initial.x
    entity.position.rect.y = entity.position.initial.y
    entity.speed = 0
    entity.acceleration = 0.2
    entity.camera.setWorldPos(entity.position.initial.x, entity.position.initial.y)
    entity.direction = 'right'
    entity.animations.alpha = 255
    entity.effect = None

def makePlayer(x,y):
    entity = engine.Entity()
    entity.position = engine.Position(x,y,45,51)
    entityIdleAnimation = engine.Animation([idle0, idle1, idle2, idle3])
    entityWalkingAnimation = engine.Animation([walking0, walking1, walking2, walking3, walking4, walking5])
    entity.animations.add('idle', entityIdleAnimation)
    entity.animations.add('walking', entityWalkingAnimation)
    entity.score = engine.Score()
    entity.battle = engine.Battle()
    entity.intention = engine.Intention()
    entity.acceleration = 0.2
    entity.type = 'player'
    entity.reset = resetPlayer
    return entity
