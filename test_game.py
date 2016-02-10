#! /usr/bin/env python

import pygame
from pygame.locals import *
from asteroid import *
from sys import exit
from random import randint
from time import sleep

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    
    randomBox = pygame.Rect(randint(0,539),randint(0,379),50,50)
    randomColor = pygame.Color(randint(100,255),0,0)

    
    randomPoint = (randint(0,589),randint(0,429))

    randomAsteroidPoints = randint(6,12)

    a = Asteroid(randomColor, randomBox, randomAsteroidPoints)

    a.draw(screen, randomPoint)

    print a

    pygame.display.update()

    sleep(1)

