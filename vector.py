#! /usr/bin/env python

from __future__ import division
import math
import sys

class Vector(object):

    """Simple Vector operation class"""

    def __init__(self, *values):
        # Check that all arguments are numeric:
        for i in values:
            if not (isinstance(i, int) or isinstance(i, float)):
                raise ValueError("Argument " + repr(i) + " is not a numeric value.")

        if len(values) > 3 or len(values) < 2:
            raise AssertionError("Too many arguments, only 2D and 3D Vectors supported")

        self.__values = values
                
    # End __init__


    @property
    def x(self):
        return self.__values[0]

    # End property x


    @property
    def y(self):
        return self.__values[1]

    # End property y


    @property
    def z(self):
        if len(self.__values) < 3:
            raise ValueError("Vector does not have a z value")
        return self.__values[2]

    # End property z


    @property
    def magnitude(self):
        sum = 0
        for component in self.__values:
            sum += component**2

        return math.sqrt(sum)

    # End property magnitude


    def normalize(self):
        magnitude = self.magnitude
        newValues = []
        for i in range(0, len(self.__values)):
            newValues.append(self.__values[i] / magnitude)

        self.__values = newValues

    # End normalize


    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.__values) != len(other.__values):
                raise ValueError("Vectors have differing dimensions")

            newValues = []
            for i in range(0, len(self.__values)):
                newValues.append(self.__values[i] + other.__values[i])
            return Vector(*newValues)
        elif (isinstance(other, int) or isinstance(other, float)):
            newValues = []
            for i in range(0, len(self.__values)):
                newValues.append(self.__values[i] + other)
            return Vector(*newValues)
        else:

            raise ValueError("No method for adding Vector and objects of " + str(type(other)))
        
    # End __add__


    def __sub__(self, other):
        if isinstance(other, Vector):
            if len(self.__values) != len(other.__values):
                raise ValueError("Vectors have differing dimensions")

            newValues = []
            for i in range(0, len(self.__values)):
                newValues.append(self.__values[i] - other.__values[i])
            return Vector(*newValues)
        elif (isinstance(other, int) or isinstance(other, float)):
            newValues = []
            for i in range(0, len(self.__values)):
                newValues.append(self.__values[i] - other)
            return Vector(*newValues)
        else:

            raise ValueError("No method for subtracting objects of " + str(type(other)) + " from Vector")

    # End __sub__


    def __mul__(self, scalar):
        newValues = []
        for i in range(0, len(self.__values)):
            newValues.append(self.__values[i] * scalar)
        return Vector(*newValues)

    # End __mul__


    if sys.version_info[0] > 2:

        def __truediv__(self, scalar):
            newValues = []
            for i in range(0, len(self.__values)):
                newValues.append(self.__values[i] / scalar)
            return Vector(*newValues)

        # End __truediv__

    else:
        
        def __div__(self, scalar):
            newValues = []
            for i in range(0, len(self.__values)):
                newValues.append(self.__values[i] / scalar)
            return Vector(*newValues)

        # End __div__


    def __neg__(self):
        newValues = []
        for i in range(0, len(self.__values)):
            newValues.append(-self.__values[i])
        return Vector(*newValues)

    # End __neg__

    def __getitem__(self, index):
        return float(self.__values[index])

    # End __getitem__

    def __setitem__(self, index, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise ValueError("Right hand side is not a numeric value")

        self.__values[index] = float(value)

    # End __setitem__


    def __len__(self):
        return len(self.__values)

    # End __len__


    def __format(self, prefix, formatFunction):
        theString = prefix + "("
        for i in range(0, len(self.__values)):
            theString += formatFunction(self.__values[i])
            if i < (len(self.__values) - 1):
                theString += ", "
            
        return theString + ")"

    # End __str__
        

    def __str__(self):
        return self.__format("",str)

    # End __str__


    def __repr__(self):
        return self.__format("Vector",repr)

    # End __repr__


# End Vector


def VectorFromPoints(point1, point2):
    if len(point1) != len(point2):
        raise ValueError("Points have different dimensions")

    newValues = []
    for i in range(0, len(point1)):
        newValues.append(point2[i] - point1[i])

    return Vector(*newValues)

# End VectorFromPoints

