import pygame
import math

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size=[10,10]):
        self.game = game
        self.pos = list(pos)
        self.e_type = e_type
        self.size = list(size)
        self.velocity = [0,0]
        self.acceleration =[0,0]
        self.speed = 0
        self.direction = 0
    
    def update(self):
        
        # moves the object using speed and velocity. Speed is direction based, and velocity is just x and y
        self.velocity[0] += self.acceleration[0]
        
        self.velocity[1] += self.acceleration[1]
        
        self.pos[0] += self.speed * math.cos(self.direction) 
        
        self.pos[1] += self.speed * math.sin(self.direction) 
        
        self.pos[0] += self.velocity[0]
        
        self.pos[1] += self.velocity[1]

        
    def render(self, surface):
        surface.blit(self.image, self.pos)
    def render_hitbox(self, surface):
        pygame.draw.rect(surface, "#000000", pygame.Rect(self.pos, self.size))
    def render_circle(self, surface):
        pygame.draw.circle(surface, "#000000", self.pos, (self.size[0]+self.size[1])/2)
    
    
    