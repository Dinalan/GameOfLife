from typing import Tuple

import pygame
import sys

from bg.Grid import Grid, BetterGrid


class Menu:
    # TODO: add a proper menu (after the app though)
    def __init__(self):
        # For the moment the options are set to dummy values
        self.options = {'gridsize': (100, 100), 'tilesize': 8, 'refreshrate': 60}


class App:
    # TODO: Create the main app
    def __init__(self, menu, grid_manager):
        self.WIN = None
        self.options = None
        self.menu = menu
        self.gridmanager = grid_manager

    def start(self):
        self.options = self.menu.options
        self.WIN = pygame.display.set_mode(
            (self.options['gridsize'][0] * self.options['tilesize'],
             self.options['gridsize'][1] * self.options['tilesize']))


class GUI:
    def __init__(self):
        self.menu = Menu()
        self.app = App()
