import pygame

from views.shop import ShopView

from .base import PygameController


class ShopController(PygameController):
    def __init__(self, shop):
        self._shop = shop
        # We will have access to the shop in the view
        self._view = ShopView(shop)

    def run(self, window, hero):
        """ Does anyone read my docstrings? I wonder. """

        self._view.display(window)

        # Run the loop (inheritance)
        mouse_position = self._run_loop()

        # We can determine which item was bought based on the mouse click
        item_bought = self._view.find_item(mouse_position)

        # ME WANTS THIS
        if item_bought is not None:
            # Let's see if I can buy it
            if hero.coins >= item_bought.price:
                self._shop.remove_item(item_bought)
                hero.coins = hero.coins - item_bought.price
                # OH YES - ME LIKEY
                item_bought.use(hero)
            else:
                # Just paid your rent in Vancouver?
                print("You don't have enough money to buy this item.")
