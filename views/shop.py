import pygame
from pygame.sprite import Group

from constants import (SHOP_ITEM_IMG_OFFSET, SHOP_ITEM_LINE_HEIGHT,
                       SHOP_ITEM_SIZE, SHOP_ITEM_TXT_OFFSET, WHITE)


class ShopView(Group):
    """ The view for the shop window """

    def __init__(self, shop):
        super().__init__()

        # These are the items from the Shop model
        self._items = shop.items
        # These are the sprites of the shop items
        self._sprites = list()

        font = pygame.font.SysFont("arial", 48, bold=True)

        for idx, item in enumerate(self._items):
            # For each shop item, create a surface
            surface = pygame.Surface(SHOP_ITEM_SIZE)
            surface.fill(WHITE)

            # Item image
            surface.blit(item.image, SHOP_ITEM_IMG_OFFSET)

            # Item text
            text = font.render(f"{item.name:.<15} ${item.price}", True, (0, 0, 0))
            surface.blit(text, SHOP_ITEM_TXT_OFFSET)

            # We create a sprite to make it easier to detect collisions / clicks
            sprite = pygame.sprite.Sprite()
            sprite.image = surface
            sprite.rect = sprite.image.get_rect()
            sprite.rect.x = 0
            sprite.rect.y = 20 + SHOP_ITEM_LINE_HEIGHT * idx
            self._sprites.append(sprite)

        # Add all the sprites to the sprite group
        self.add(*self._sprites)

    def display(self, window):
        window.fill(WHITE)
        # Display all the sprites at once
        self.draw(window)
        pygame.display.flip()

    def find_item(self, pos):
        # We look for the shop item matching the sprite that was clicked
        # and return it
        for idx, sprite in enumerate(self._sprites):
            if sprite.rect.collidepoint(pos):
                return self._items[idx]
