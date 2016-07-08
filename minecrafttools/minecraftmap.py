# -*- coding: utf-8 -*-

from PIL                           import Image, ImageDraw
from minecrafttools.intcoordinates import IntCoordinates
from minecrafttools.intdimensions  import IntDimensions

import itertools
import os
import sys

class MinecraftMap:

    def __init__(self, dimension, coordinates, colorsMap):
        """ Creates a MinecraftMap object
        Params:
            dimension (integer):          dimension (nether = -1, surface = 0, end = ?)
            coordinates (IntCoordinates): top left coordinates
            colorsMap (ColorsMap):        list of colors ID and the dimensions of the map
        """
        self.__dimension   = int(dimension)
        self.__coordinates = coordinates
        self.__colorsMap   = colorsMap

    def coordinates(self):
        """ Returns the coordinates of the map
        Returns:
            IntCoordinates
        """
        return self.__coordinates

    def dimensions(self):
        """ Returns the dimensions of the map
        Returns:
            IntDimensions
        """
        return IntDimensions(
            self.__colorsMap.width(),
            self.__colorsMap.height()
        )

    def id(self, coordinates):
        """ Returns the color id at the given coordinates
        Params:
            coordinates (IntCoordinates): the coordinates of the color id
        Returns:
            integer
        Raises:
            IndexError when the coordinates are out of bound
        """
        return self.__colorsMap.id(coordinates)

    def scale(self):
        """ Returns the map scale
        Returns:
            integer
        """
        return self.__colorsMap.scale()

    def type(self):
        """ Returns the map type (surface, nether, end, etc)
        Returns:
            integer
        """
        # TODO MLG: return a string (or a map type object) instead of an integer
        return self.__dimension
