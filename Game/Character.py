from Game.Level import *
import constants as c
import pygame

SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
red = (255,0,0)

class Character(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        
        self.faceRight = True
        self.state = c.WAIT
        self.walkSpeed = 4
        self.jumpSpeed = 8
        self.speed_x = 0
        self.speed_y = 0
        self.size = 20
        self.image = pygame.Surface([40, 60])
        self.image.fill(red)
        self.rect = self.image.get_rect()
            
    def stopMove(self):
        self.speed_x = 0
        if (self.speed_y == 0):
            self.state = c.WAIT
    
    def moveLeft(self):
        self.speed_x = self.walkSpeed*-1
        self.faceRight = False
        if not (self.state == c.JUMP):
            self.state = c.WALK
        
    def moveRight(self):
        self.speed_x = self.walkSpeed
        self.faceRight = True
        if not (self.state == c.JUMP):
            self.state = c.WALK
            
    def jump(self, blockList):
        self.state = c.JUMP
        self.rect.y += 2
        collisions = pygame.sprite.spritecollide(self, blockList, False)    
        self.rect.y -= 2    

        if len(collisions) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = self.jumpSpeed*-1
            
    def land(self):
        if (self.speed_x == 0):
            self.state = c.WAIT
        else:
            self.state = c.WALK        
    
    def applyGravity(self, gravity):
        # Always check that we can't fall farther, if we're already falling, then fall faster
        if self.speed_y == 0:
            self.speed_y = 1
        else:
            self.speed_y += .35
            self.state = c.JUMP
        
        # Check to see if we've hit the bottom of the level, if we have stop moving and reset to be even
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.speed_y >= 0:
            if (self.state == c.JUMP):
                self.land()
            self.speed_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            
    def update(self, gravity, blockList):
        self.applyGravity(gravity)      
        
        # Move and check for collisions, if we hit something respawn us beside it
        self.rect.x += self.speed_x        
        collisions = pygame.sprite.spritecollide(self, blockList, False)
        for block in collisions:
            if self.speed_x > 0:
                self.rect.right = block.rect.left
            elif self.speed_x < 0:
                self.rect.left = block.rect.right
                
        self.rect.y += self.speed_y
        collisions = pygame.sprite.spritecollide(self, blockList, False)        
        for block in collisions:
            if self.speed_y > 0:
                self.rect.bottom = block.rect.top
            elif self.speed_y < 0:
                self.rect.top = block.rect.bottom
                
            # We've hit something so stop moving
            if (self.state == c.JUMP):
                self.land()
            self.speed_y = 0

