import pygame, os
from Character import *
import constants as c

class Hero(Character):
    def __init__(self):
        Character.__init__(self)
        self.spriteSheet = pygame.image.load(os.path.join('chrono.png'))
        self.image = self.get_image(7, 0, 18, 34)
        self.size = self.image.get_height()
        self.rect = self.image.get_rect()
        self.frameCount = 0;
        self.build_animations()
        
    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height])
        rect = image.get_rect()

        image.blit(self.spriteSheet, (0, 0), (x, y, width, height))
        image = pygame.transform.scale(image,
                                   (int(rect.width*c.SIZE_MULTIPLIER),  # @UndefinedVariable
                                    int(rect.height*c.SIZE_MULTIPLIER)))
        return image
    
    def build_animations(self):
        self.right_walk = []
        self.left_walk = []
        
        self.rightStand = self.get_image(7, 0, 14, 34)
        self.leftStand = pygame.transform.flip(self.rightStand, True, False)
        
        self.right_walk.append(self.get_image(52, 0, 15, 34))
        self.right_walk.append(self.get_image(77, 0, 21, 34))
        self.right_walk.append(self.get_image(102, 0, 15, 34))
        self.right_walk.append(self.get_image(125, 0, 14, 34))
        self.right_walk.append(self.get_image(147, 0, 22, 34))
        self.right_walk.append(self.get_image(176, 0, 14, 34))        
        
        for image in self.right_walk:
            mirror_image = pygame.transform.flip(image, True, False)
            self.left_walk.append(mirror_image) 
            
        self.right_jump = self.get_image(26, 0, 21, 34)
        self.left_jump = pygame.transform.flip(self.right_jump, True, False)
            
    def getWalk(self):
        list_length = len(self.right_walk)
        for x in range (0, list_length):
            if self.frameCount < (x*c.FRAME_DELAY)+c.FRAME_DELAY:
                if self.faceRight:
                    self.image = self.right_walk[x]
                else:
                    self.image = self.left_walk[x]
                break
        self.frameCount += 1
        if self.frameCount > (list_length)*c.FRAME_DELAY:
            self.frameCount = 0 
                   
        
    def update(self, gravity, blockList):        
        if (self.state == c.WALK):
            self.getWalk()
        elif(self.state == c.JUMP):
            if (self.faceRight):
                self.image = self.right_jump
            else:
                self.image = self.left_jump
        else:
            if (self.faceRight):
                self.image = self.rightStand
            else:
                self.image = self.leftStand
            
        Character.update(self, gravity, blockList)