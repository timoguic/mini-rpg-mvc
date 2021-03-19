import pygame
from pygame.sprite import Group

from constants import (MONSTER_SPACING_X, MONSTER_SPACING_Y, MONSTERS_OFFSET_X,
                       MONSTERS_OFFSET_Y)

from .monster_custom import Giant, Magician, Wolf


class MonsterTeam(Group):
    """This is a group of monsters. It inherits from pygame.sprite.Group.

    All monsters inside this group are sprites too.
    """

    def __init__(self, level=0):
        super().__init__()

        # Let's pretend we have some logic to create the monsters
        wolves = [Wolf() for _ in range(level % 4)]
        magicians = [Magician()] if level % 4 == 0 else []
        giants = [Giant() for _ in range(level // 3)]

        # Add all the monsters to the group
        self.add(*wolves)
        self.add(*magicians)
        self.add(*giants)

    def all_monsters_dead(self):
        """ We check each monster - if one is not dead, not all monsters are dead """
        for monster in self.sprites():
            if not monster.is_dead:
                return False
        return True

    def update(self):
        """Update the sprite group.

        We display the monsters two by two. We can use modulo (%) and integer division (//)
        to easily compute the coordinates.

        Who thought math classes would come in useful one day?
        """
        super().update()

        for idx, sprite in enumerate(self.sprites()):
            line = idx // 2
            col = idx % 2
            sprite.rect.x = MONSTERS_OFFSET_X + col * MONSTER_SPACING_X
            sprite.rect.y = MONSTERS_OFFSET_Y + line * MONSTER_SPACING_Y
