#! /usr/bin/env python

import random
from vector import *
from visual_object import *
import pygame

class Asteroid(VisualObject):
    """Asteroid class for drawing asteroids to a surface"""

    def __init__(self, color, rect):
        self.__color = color
        self.__rect = rect
        points = []
        self.__vectors = []
        for i in range(0, random.randint(5,10)):
            points.append((random.randint(rect[0],rect[0]+rect[2]),
                                  random.randint(rect[1],rect[1]+rect[3])))

#        print points

        self.__center = (float(rect[0]+(rect[2]/2)),float(rect[1]+(rect[3]/2)))

#        print self.__center

#        for point in points:
#            self.__vectors.append(VectorFromPoints(self.__center, point))

#        print self.__vectors

        self.__vectors.append(Vector(0,-1*random.randint(1,rect[3]/2)))
        self.__vectors.append(Vector(random.randint(1,rect[2]/2),0))
        self.__vectors.append(Vector(0,random.randint(1,rect[3]/2)))
        self.__vectors.append(Vector(-1*random.randint(1,rect[2]/2),0))

        self.__centerVector = VectorFromPoints((rect[0],rect[1]), self.__center)

#        print self.__centerVector

    # End __init__


    def draw(self, surface, point):
        """draw(surface,point) draws an Asteroid onto surface
        at the named point where the point is the upper leftmost
        corner of the asteroid."""

        center = (point[0] + self.__centerVector.x, point[1] + self.__centerVector.y)
        points = []
        for v in self.__vectors:
            points.append((center[0] + v.x, center[1] + v.y))

#        print points
        pygame.draw.polygon(surface, self.__color, points, 2)

    # End draw

    def __str__(self):
        value = "(" + str(self.__color) + "," + str(self.__rect) + ")"
        return value

    # End __str__


    def __repr__(self):
        value = "Asteroid(" + repr(self.__color) + ", " + repr(self.__rect) + ")"
        return value

    # End __repr__

# End Asteroid

