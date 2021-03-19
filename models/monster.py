import pygame
from pygame.sprite import Sprite

from constants import MONSTER_SIZE, MONSTER_TXT_OFFSET, WHITE


class Monster(Sprite):
    """ Base class for the monsters. Most of the logic is fake. """

    def __init__(self, level=0):
        super().__init__()
        # Improve this
        self.health = 50 + level
        self.power = 10 + level

        # Update the display (health / power)
        self.update()

    @property
    def is_dead(self):
        return self.health <= 0

    def update(self):
        """We update the sprite here. We create a new surface, and blit
        - the image
        - the text for the monster
        """

        surface = pygame.Surface(MONSTER_SIZE)
        surface.set_colorkey((255, 255, 255))
        surface.fill(WHITE)
        image = pygame.image.load(self.image_file).convert_alpha()

        if self.health <= 0:
            # A good monster is a dead monster
            # In which case, we had an opacity layer because it just looks good
            image.set_alpha(100)

        # Blit the monster image
        surface.blit(image, (0, 0))

        if self.health <= 0:
            # It's a dead monster - blit the dead skull on top of it
            dead = pygame.image.load("assets/img/dead.png").convert_alpha()
            surface.blit(dead, (0, 0))

        # Create the descriptive text for the monster
        font = pygame.font.SysFont("arial", 18, bold=True)
        text = font.render(
            f"{self.__class__.__name__} | HP: {self.health} | AP: {self.power}",
            True,
            (0, 0, 0),
        )

        surface.blit(text, MONSTER_TXT_OFFSET)

        self.image = surface
        self.rect = self.image.get_rect()
