#!/usr/bin/env python
import runner
import pygame
from pygame.draw import *


white=(255,255,255)
blue=(0,0,255)


def scene(display, x):
    display.fill(white)
    rect(display, blue, (x, 150,50,50))
    return x+10


runner.animate(0, scene)
