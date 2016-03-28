#!/usr/bin/env python
import runner
import pygame
from pygame.draw import *


white=(255,255,255)
blue=(0,0,255)


def scene_static(display):
    display.fill(white)
    rect(display, blue, (200, 150,50,50))


runner.display(scene_static)

