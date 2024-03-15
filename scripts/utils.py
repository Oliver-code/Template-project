import os
import pygame

BASE_IMG_PATH = os.getcwd()+"/assets/images/"

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    # if i was less lazy and didn't use convert alpha
    # img.set_colorkey((0, 0, 0))
    return img
    


