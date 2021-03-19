import pygame

from constants import (LEVEL_DONE_COLOR, LEVEL_DONE_MSG_RECT,
                       LEVEL_DONE_TXT_OFFSET, WHITE, WINDOW_SIZE)


class LevelDoneView:
    def __init__(self, level):
        self._level = level

    def display(self, window):
        surface = pygame.Surface(WINDOW_SIZE, pygame.SRCALPHA)
        surface.fill((0, 0, 0, 50))
        window.blit(surface, (0, 0))

        pygame.draw.rect(window, LEVEL_DONE_COLOR, LEVEL_DONE_MSG_RECT)
        font = pygame.font.SysFont("arial", 48, bold=True)
        text = font.render(f"Level {self._level} completed!", True, WHITE)
        window.blit(text, LEVEL_DONE_TXT_OFFSET)
        pygame.display.flip()
