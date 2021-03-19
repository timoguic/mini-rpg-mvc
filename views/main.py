import pygame

from models import Shop


class MainView:
    WINDOW_SIZE = (800, 600)
    SHOP_BUTTON_XY = (10, 10)
    HERO_XY = (0, 300)
    MONSTER_TEAM_XY = (450, 600)

    def __init__(self, window, hero):
        self._window = window
        self._hero = hero
        self._team = None

        self._team_surface = pygame.Surface((450, 600))
        self._team_surface.fill((240, 240, 255))
        self._shop_button = Shop.get_button_image()

    def attach_team(self, team):
        self._team = team

    def display(self):
        self._window.fill((255, 255, 255))
        self._window.blit(self._shop_button, self.SHOP_BUTTON_XY)
        self._hero.update()
        self._window.blit(self._hero.image, self.HERO_XY)

        self._team.update()
        self._team.draw(self._window)

        pygame.display.flip()

    def has_clicked_shop(self, pos):
        if self._shop_button.get_rect().collidepoint(pos):
            return True

        return False

    def get_clicked_monster(self, pos):
        for monster in self._team.sprites():
            if monster.rect.collidepoint(pos):
                return monster

        return None
