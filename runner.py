import os
import pygame, sys
from pygame.locals import *


def display(scene_function):
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode((640, 400),0,32)
    scene_function(display)
    pygame.display.update()

    while True:
        clock.tick(40)

def animate(initial_world, scene_function):
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
