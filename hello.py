#!/usr/bin/env python
import runner
import pygame


white=(255,255,255)
blue=(0,0,255)


def scene(display, x):
    display.fill(white)
    pygame.draw.rect(display, blue, (x, 150,50,50))
    return x+10


runner.run(0, scene)


