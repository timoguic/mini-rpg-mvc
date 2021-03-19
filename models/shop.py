import pygame.font


class Shop:
    def __init__(self):
        self._items = list()

    def add_item(self, item):
        self._items.append(item)

    @property
    def items(self):
        return self._items

    def get_item(self, idx):
        return self._items.pop(idx)

    @staticmethod
    def get_button_image(display_text="$ SHOP"):
        font = pygame.font.SysFont("arial", 24, bold=True)
        dimensions = font.size(display_text)
        text = font.render(display_text, True, (200, 200, 200))
        surface = pygame.Surface((dimensions[0] + 10, dimensions[1] + 10))
        surface.fill((0, 100, 0))
        surface.blit(text, (5, 5))

        return surface
