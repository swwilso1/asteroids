#! /usr/bin/env python

from __future__ import division
import random
from vector import *
from visual_object import *
import pygame
import math


def abs(x):
    if x < 0:
        return -1 * x
    return x

# End abs


class Asteroid(VisualObject):
    """Asteroid class for drawing asteroids to a surface"""

    def __init__(self, color, rect, points=7):
        self.__color = color
        self.__rect = rect
        self.__vectors = []

        self.__center = (float(rect[0]+(rect[2]/2)),float(rect[1]+(rect[3]/2)))

        xBound = rect[2]/2
        yBound = rect[3]/2

        if xBound < yBound:
            radius = xBound
        else:
            radius = yBound

        delta = int(360/points)

        angle = 0

        doShortRadius = random.randint(1,100) > 75

        didShortRadius = random.randint(2, points - 3)

        for i in range(points):
            angle = i * delta

            spareRadius = radius
            
            if doShortRadius and didShortRadius > 0:
                limiter = random.randint(2,3)
                radius = radius * 1/limiter
                didShortRadius -= 1

            if angle >= 0 and angle <= 90:
                newAngle = angle
                if angle == 0:
                    x = radius
                    y = 0
                elif angle == 90:
                    x = 0
                    y = radius
                else:
                    newAngle = math.radians(newAngle)
                    x = abs(math.cos(newAngle)) * radius
                    y = abs(math.sin(newAngle)) * radius
            elif angle > 90 and angle <= 180:
                newAngle = 180 - angle
                if angle == 180:
                    x = -1 * radius
                    y = 0
                else:
                    newAngle = math.radians(newAngle)
                    x = -1 * abs(math.cos(newAngle)) * radius
                    y = abs(math.sin(newAngle)) * radius
            elif angle > 180 and angle <= 270:
                newAngle = 270 - angle
                if angle == 270:
                    x = 0
                    y = -1 * radius
                else:
                    newAngle = math.radians(newAngle)
                    x = -1 * abs(math.sin(newAngle)) * radius
                    y = -1 * abs(math.cos(newAngle)) * radius
            else:
                newAngle = 360-angle
                if angle == 360:
                    x = radius
                    y = 0
                else:
                    newAngle = math.radians(newAngle)
                    x = abs(math.cos(newAngle)) * radius
                    y = -1 * abs(math.sin(newAngle)) * radius

            self.__vectors.append(Vector(x, y))
            radius = spareRadius

        self.__centerVector = VectorFromPoints((rect[0],rect[1]), self.__center)

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

