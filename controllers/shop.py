import pygame

from views.shop import ShopView

from .base import PygameController


class ShopController(PygameController):
    def __init__(self, shop):
        self._shop = shop
        self._view = ShopView(shop)

    def run(self, window, hero):
        self._view.display(window)
        mouse_position = self._run_loop()
        item_bought = self._view.find_item(mouse_position)
        if item_bought is not None:
            if hero.coins >= item_bought.price:
                self._shop.remove_item(item_bought)
                hero.coins = hero.coins - item_bought.price
                item_bought.use(hero)
            else:
                print("You can't have this.")
