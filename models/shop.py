import pygame.font

from constants import SHOP_BUTTON_COLOR, SHOP_BUTTON_TXT_COLOR


class Shop:
    """ The shop has items """

    def __init__(self):
        self._items = list()

    def add_item(self, item):
        self._items.append(item)

    @property
    def items(self):
        return self._items

    def remove_item(self, item):
        self._items.remove(item)

    @staticmethod
    def get_button_image(display_text="$ SHOP"):
        """A helper method to create the "Shop" button.

        It would be better suited elsewhere.
        """

        font = pygame.font.SysFont("arial", 24, bold=True)
        dimensions = font.size(display_text)
        text = font.render(display_text, True, SHOP_BUTTON_TXT_COLOR)
        surface = pygame.Surface((dimensions[0] + 10, dimensions[1] + 10))
        surface.fill(SHOP_BUTTON_COLOR)
        surface.blit(text, (5, 5))

        return surface
