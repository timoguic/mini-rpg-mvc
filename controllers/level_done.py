import pygame

from views import LevelDoneView

from .base import PygameController


class LevelDoneController(PygameController):
    def __init__(self, level):
        # We save the current when instantiating the view
        self._view = LevelDoneView(level)

    def run(self, window):
        """ Nothing fancy here, but thanks for reading it """
        self._view.display(window)
        self._run_loop()
