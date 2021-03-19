import pygame
from pygame.sprite import Group

from .monster_custom import Giant, Magician, Wolf


class MonsterTeam(Group):
    def __init__(self, level=0):
        super().__init__()

        wolves = [Wolf() for _ in range(level % 4)]
        magicians = [Magician()] if level % 4 == 0 else []
        giants = [Giant() for _ in range(level // 3)]

        self.add(*wolves)
        self.add(*magicians)
        self.add(*giants)

    def all_monsters_dead(self):
        for monster in self.sprites():
            if not monster.is_dead:
                return False
        return True

    def update(self):
        super().update()

        for idx, sprite in enumerate(self.sprites()):
            line = idx // 2
            col = idx % 2
            sprite.rect.x = 370 + col * 200
            sprite.rect.y = 20 + line * 190
