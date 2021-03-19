import pygame
from pygame.sprite import Sprite

from constants import (HERO_AREA_SIZE, HERO_IMG_OFFSET, HERO_INITIAL_HEALTH,
                       HERO_TXT_OFFSET, WHITE)


class Hero(Sprite):
    """The Hero class defines the hero of our game.

    We make it inherit from pygame.sprite.Sprite, so that
    it is easier to manage.
    """

    def __init__(self):
        super().__init__()

        self.font = pygame.font.SysFont("arial", 24, bold=True)

        # The left side of the main window is for the hero
        self.image = pygame.Surface(HERO_AREA_SIZE)
        self.image.fill(WHITE)

        hero_img = pygame.image.load("assets/img/hero.png").convert_alpha()
        self.image.blit(hero_img, HERO_IMG_OFFSET)

        self._health = HERO_INITIAL_HEALTH
        self._power = 50
        self._coins = 20

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val <= 0:
            val = 0

        self._health = int(val)

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, val):
        self._power = int(val)

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, val):
        if val < 0:
            raise NotImplementedError("We don't do credit, sorry!")
        self._coins = int(val)

    @property
    def is_dead(self):
        return self._health <= 0

    def update(self):
        """This method defines what happens when the sprite should be updated.

        We will paint over the details (health, attack) and blit the values again.
        """

        # Paint white over text
        white_rect = pygame.Surface((HERO_AREA_SIZE[0], 50))
        white_rect.fill(WHITE)
        self.image.blit(white_rect, HERO_TXT_OFFSET)

        text = self.font.render(
            f"HEALTH: {self._health} | ATTACK: {self._power} | ${self.coins}",
            True,
            (0, 0, 0),
        )
        self.image.blit(text, (10 + HERO_TXT_OFFSET[0], HERO_TXT_OFFSET[1]))

    def attack(self, monster):
        """This is a very simple method that attacks a monster.

        You should improve it - ain't nobody got time for that?
        """
        monster.health = 0
        self.health -= 5
