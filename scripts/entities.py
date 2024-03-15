import pygame
import math
from scripts.utils import load_image
class PhysicsSprite:
    def __init__(self, game, e_type, pos, size=[10,10]):
        self.game = game
        self.pos = list(pos)
        self.size = list(size)
        self.velocity = [0,0]
        self.acceleration =[0,0]
        self.speed = 0
        self.direction = 0
        
        self.e_type = e_type
        #set an image for each type of object
        self.image = None
    
    def update(self):
        
        # moves the object using speed and velocity. Speed is direction based, and velocity is just x and y
        self.velocity[0] += self.acceleration[0]
        
        self.velocity[1] += self.acceleration[1]
        
        self.pos[0] += self.speed * math.cos(self.direction) 
        
        self.pos[1] += self.speed * math.sin(self.direction) 
        
        self.pos[0] += self.velocity[0]
        
        self.pos[1] += self.velocity[1]

        
    def render(self, surface):
        offset = self.game.render_offset
        draw_offset = (self.pos[0] - offset[0], self.pos[1] - offset[1])
        surface.blit(self.image, draw_offset)
    def render_hitbox(self, surface):
        offset = self.game.render_offset
        draw_offset = (self.pos[0] - offset[0], self.pos[1] - offset[1])
        pygame.draw.rect(surface, "#000000", pygame.Rect(draw_offset, self.size))
    def render_circle(self, surface):
        offset = self.game.render_offset
        draw_offset = (self.pos[0] - offset[0], self.pos[1] - offset[1])
        pygame.draw.circle(surface, "#000000", draw_offset, (self.size[0]+self.size[1])/2)
    
class Apple(PhysicsSprite):
    def __init__(self, game, pos, size=[10,10]):
        super().__init__(game, 'apple', pos, size)
        
        self.image = load_image("cherry1.png")
        