# -*- coding: utf-8 -*-

from minecrafttools.properties import Properties
from minecrafttools.whitelist  import Whitelist
from minecrafttools.world      import World

import os

class Server:

    def __init__(self, minecraftDirectory):
        self.__properties = Properties(os.path.join(minecraftDirectory, 'server.properties'))
        self.__whitelist  = Whitelist(os.path.join(minecraftDirectory, 'whitelist.json'))
        self.__world      = World(os.path.join(minecraftDirectory, self.__properties.valueOf('level-name')))

    def printWhitelist(self):
        """ Displays the players list """
        for player in self.__whitelist.playersSortedByName():
            print(player.id + ' /// ' + player.name)

    def world(self):
        """ Returns the World
        Returns:
            World
        """
        return self.__world
