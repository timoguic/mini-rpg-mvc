import pygame


class ShopItem:
    pass


class Sword(ShopItem):
    name = "Sword"
    price = 10
    image = pygame.image.load("assets/img/sword.png")

    def use(self, hero):
        hero.power = int(hero.power * 1.5)


class SmallPotion(ShopItem):
    name = "Small potion"
    price = 5
    image = pygame.image.load("assets/img/small_potion.png")

    def use(self, hero):
        hero.health = int(hero.health + 50)


class BigPotion(ShopItem):
    name = "Big potion"
    price = 10
    image = pygame.image.load("assets/img/big_potion.png")

    def use(self, hero):
        hero.health = 100
