import sys, pygame # @UnusedWildImport @UnusedImport
from Game.Character import *  # @UnusedWildImport
from Game.Hero import * # @UnusedWildImport
from Game.Level import * # @UnusedWildImport


pygame.init()

SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
red = (255,0,0)
black = (0,0,0)
gravity = 0.09

clock = pygame.time.Clock() 

blockList = pygame.sprite.Group()

hero = Hero()
active_sprite_list = pygame.sprite.Group()
active_sprite_list.add(hero)

block = Platform(400,10)
block.rect.x = 400
block.rect.y = 550
blockList.add(block)

def getKeys(events):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.moveLeft()
            if event.key == pygame.K_RIGHT:
                hero.moveRight()
            if event.key == pygame.K_UP:
                hero.jump(blockList)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT: 
                hero.stopMove()
            if event.key == pygame.K_RIGHT:
                hero.stopMove()    

screen = pygame.display.set_mode(SIZE)
screen.fill(black)

while 1:
    events = pygame.event.get() 
    for event in events:
        if event.type == pygame.QUIT: sys.exit()
    getKeys(events)
            
    screen.fill(black)
    active_sprite_list.update(gravity, blockList)
    active_sprite_list.draw(screen)
    
    blockList.draw(screen)
    
    clock.tick(60)
    pygame.display.flip() 
pygame.quit ()
    