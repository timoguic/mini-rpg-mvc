import pygame

from constants import HERO_OFFSET, SHOP_BUTTON_OFFSET, WHITE
from models import Shop


class MainView:
    """The main view

    It is divided in two areas: hero + shop button on the left side,
    and monsters on the right side.
    """

    def __init__(self, window, hero):
        self._window = window
        self._hero = hero
        self._team = None

        self._shop_button = Shop.get_button_image()

    def attach_team(self, team):
        self._team = team

    def display(self):
        # Paints the window white
        self._window.fill(WHITE)
        # Show shop button
        self._window.blit(self._shop_button, SHOP_BUTTON_OFFSET)

        # Update the Hero sprite and display it
        self._hero.update()
        self._window.blit(self._hero.image, HERO_OFFSET)

        # Update the monsters sprite group and display it
        self._team.update()
        self._team.draw(self._window)

        pygame.display.flip()

    def has_clicked_shop(self, pos):
        # Did we click on the shop button?
        if self._shop_button.get_rect().collidepoint(pos):
            return True

        return False

    def get_clicked_monster(self, pos):
        # Did we click on a monster?
        # We use sprite collisions, and return the clicked monster.

        for monster in self._team.sprites():
            if monster.rect.collidepoint(pos):
                return monster

        return None
