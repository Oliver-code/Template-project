from cmath import rect
import pygame
import sys

from scripts.entities import Cherry, PhysicsSprite

class Game:
    def __init__(self) -> None:
        pygame.init()
        
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("My game")
        self.screen = pygame.display.set_mode((800, 608))
        self.display = pygame.Surface((800, 608))
        self.camera = [0,0]
        self.render_offset = self.camera
        
        
        self.input_data = []
        
        # To be used by other scripts to check input
        # Is pressed on that frame, is released on that frame, is held on that frame
        self.input = {
            "left" : [False, False, False],
            "right" : [False, False, False],
            "up" : [False, False, False],
            "down" : [False, False, False],
            "jump" : [False, False, False]
        }
        
        # change these for different default bindings. In list format to allow mutiple bindings
        self.input_bindings = {
            "left" : [pygame.K_LEFT],
            "right" : [pygame.K_RIGHT],
            "up" :  [pygame.K_UP],
            "down" : [pygame.K_DOWN],
            "jump" : [pygame.K_LSHIFT, pygame.K_RSHIFT]
        }
                  
    def get_input(self):
        
        # When an input is detected, checks if it is bound in the input bindings(each binding is a list 
        # to allow multiple bindings of the same key), and if so it sets the apropriate self.input value
        # 
        for bindings in self.input_bindings:
            self.input[bindings][0] = False
            self.input[bindings][1] = False
        for event in self.input_data:
                    if event.type == pygame.KEYDOWN:
                        for bindings in self.input_bindings:
                            for keycode in self.input_bindings[bindings]:
                                if keycode == event.key:
                                    self.input[bindings][0] = True
                                    self.input[bindings][2] = True
                    if event.type == pygame.KEYUP:
                        for bindings in self.input_bindings:
                            for keycode in self.input_bindings[bindings]:
                                if keycode == event.key:
                                    self.input[bindings][1] = True
                                    self.input[bindings][2] = False
            
    def run(self):
        
        test_entity = PhysicsSprite(self,"test", [400,100])
        apple = Cherry(self, [100,100])
        
        running = True
        while running:
            # gets input first
            self.input_data = pygame.event.get()
            for event in self.input_data:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
            self.get_input()
            
            # backround fill
            self.display.fill("#FFFFFF")

            # updating
            test_entity.update()
            apple.update
            
            # update camera
            self.render_offset = [round(self.camera[0]),round(self.camera[1])]
            
            # rendering, renders everything in the entities list.
            test_entity.render_circle(self.display) 
            apple.render(self.display)
            
            # everything is rendered to a temporary display, this renders the temporary display onto the actual. 
            # that allows screen scaling and screen movement etc
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            
            # required at end of frame
            pygame.display.update()

            self.clock.tick(50)

            
                        
          
Game().run()
                        
        