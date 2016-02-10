#! /usr/bin/env python

import pygame
from pygame.locals import *
from asteroid import *
from sys import exit
from random import randint
from time import sleep
from vector import *

pygame.init()
screen = pygame.display.set_mode((640,480),0,32)

randomBox = pygame.Rect(randint(0,539),randint(0,379),50,50)
randomColor = pygame.Color(randint(100,255),0,0)

    
position = Vector(randint(0,589),randint(0,429))

randomAsteroidPoints = randint(6,12)

a = Asteroid(randomColor, randomBox, randomAsteroidPoints)

clock = pygame.time.Clock()

speed = .05 # pixels / millisecond
heading = Vector(0,0)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == MOUSEBUTTONDOWN:
            destination = (event.pos[0], event.pos[1])
            heading = VectorFromPoints(position, destination)
            heading.normalize()

    screen.fill((0,0,0))
    a.draw(screen, position)

    timePassed = clock.tick(30)
    distanceMoved = timePassed * speed
    position += heading * distanceMoved
    pygame.display.update()

    
