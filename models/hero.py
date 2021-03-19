import pygame
from pygame.sprite import Sprite


class Hero(Sprite):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.SysFont("arial", 24, bold=True)

        self.image = pygame.Surface((350, 300))
        self.image.fill((255, 255, 255))

        hero_img = pygame.image.load("assets/img/hero.png").convert_alpha()
        self.image.blit(hero_img, (30, 10))

        self._health = 100
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
        if val <= 0:
            raise NotImplementedError("We don't do credit, sorry!")
        self._coins = int(val)

    def update(self):
        # Paint white over text, then draw it again
        white_rect = pygame.Surface((350, 50))
        white_rect.fill((255, 255, 255))
        self.image.blit(white_rect, (0, 250))

        text = self.font.render(
            f"HEALTH: {self._health} | ATTACK: {self._power} | ${self.coins}",
            True,
            (0, 0, 0),
        )
        self.image.blit(text, (10, 250))

    def attack(self, monster):
        monster.health = 0
        self.health -= 5
