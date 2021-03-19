import pygame
from pygame.sprite import Group

from constants import (SHOP_ITEM_IMG_OFFSET, SHOP_ITEM_LINE_HEIGHT,
                       SHOP_ITEM_SIZE, SHOP_ITEM_TXT_OFFSET, WHITE)


class ShopView(Group):
    def __init__(self, shop):
        super().__init__()
        self._items = shop.items

        self._sprites = list()

        font = pygame.font.SysFont("arial", 48, bold=True)
        for idx, item in enumerate(self._items):
            surface = pygame.Surface(SHOP_ITEM_SIZE)
            surface.fill(WHITE)

            text = font.render(f"{item.name:.<15} ${item.price}", True, (0, 0, 0))
            surface.blit(item.image, SHOP_ITEM_IMG_OFFSET)
            surface.blit(text, SHOP_ITEM_TXT_OFFSET)

            sprite = pygame.sprite.Sprite()
            sprite.image = surface
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = 0
            sprite.rect.y = 20 + SHOP_ITEM_LINE_HEIGHT * idx
            self._sprites.append(sprite)

        self.add(*self._sprites)

    def display(self, window):
        window.fill(WHITE)
        self.draw(window)
        pygame.display.flip()

    def find_item(self, pos):
        for idx, sprite in enumerate(self._sprites):
            if sprite.rect.collidepoint(pos):
                return self._items[idx]
