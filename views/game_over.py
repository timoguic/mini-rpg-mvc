import pygame

from constants import WHITE


class GameOverView:
    def display(self, window):
        """ Displays an image, and "You lost!" in top left corner """

        background = pygame.image.load("assets/img/game_over.png").convert_alpha()
        font = pygame.font.SysFont("arial", 72, bold=True)
        text = font.render("You lost!", True, (0, 0, 0))
        window.fill(WHITE)
        window.blit(background, (0, 0))
        window.blit(text, (30, 30))
        pygame.display.flip()
