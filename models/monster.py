import pygame
from pygame.sprite import Sprite


class Monster(Sprite):
    def __init__(self, level=0):
        super().__init__()
        self.health = 50 + level
        self.power = 10 + level

        self.update()

    @property
    def is_dead(self):
        return self.health <= 0

    def update(self):
        surface = pygame.Surface((180, 180))
        surface.fill((255, 255, 255))
        surface.set_colorkey((255, 255, 255))
        image = pygame.image.load(self.image_file).convert_alpha()

        if self.health <= 0:
            image.set_alpha(100)

        surface.blit(image, (0, 0))

        if self.health <= 0:
            dead = pygame.image.load("assets/img/dead.png").convert_alpha()
            surface.blit(dead, (0, 0))

        font = pygame.font.SysFont("arial", 18, bold=True)
        text = font.render(
            f"{self.__class__.__name__} | HP: {self.health} | AP: {self.power}",
            True,
            (0, 0, 0),
        )

        surface.blit(text, (0, 150))

        self.image = surface
        self.rect = self.image.get_rect()
