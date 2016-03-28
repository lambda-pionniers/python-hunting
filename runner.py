import os
import pygame, sys
from pygame.locals import *


def scene(display, x):
    white=(255,255,255)
    blue=(0,0,255)
    display.fill(white)
    pygame.draw.rect(display, blue, (x, 150,50,50))
    return x+10

def run(initial_world, scene_function):
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((640, 400),0,32)

    world = initial_world

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        world = scene_function(display, world)
        pygame.display.update()
        clock.tick(40)
