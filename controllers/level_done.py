import pygame

from views import LevelDoneView

from .base import PygameController


class LevelDoneController(PygameController):
    def __init__(self, level):
        self._view = LevelDoneView(level)

    def run(self, window):
        self._view.display(window)
        self._run_loop()
