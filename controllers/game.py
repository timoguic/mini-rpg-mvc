import pygame
import pygame.locals

from models import BigPotion, Hero, MonsterTeam, Shop, SmallPotion, Sword
from views import MainView

from .base import PygameController
from .game_over import GameOverController
from .level_done import LevelDoneController
from .shop import ShopController


class GameController(PygameController):
    def __init__(self):
        pygame.init()
        self._window = pygame.display.set_mode(MainView.WINDOW_SIZE)

        self._hero = Hero()
        self._level = 1
        self._team = MonsterTeam(self._level)

        self._view = MainView(self._window, self._hero)
        self._view.attach_team(self._team)

        self._shop = Shop()
        for item in (Sword(), BigPotion(), SmallPotion(), SmallPotion()):
            self._shop.add_item(item)

    def run(self):
        running = True

        while running:
            self._view.display()
            mouse_position = self._run_loop()
            if mouse_position is False:
                running = False
                continue

            if self._view.has_clicked_shop(mouse_position):
                shop_ctrl = ShopController(self._shop)
                shop_ctrl.run(self._window, self._hero)

            monster = self._view.get_clicked_monster(mouse_position)
            if monster is not None:
                self._hero.attack(monster)
                self._view.display()

            if self._hero.is_dead:
                game_over_ctrl = GameOverController()
                game_over_ctrl.run(self._window)
                running = False
                continue

            if self._team.all_monsters_dead():
                level_done_ctrl = LevelDoneController(self._level)
                level_done_ctrl.run(self._window)

                self._level = self._level + 1
                self._team = MonsterTeam(self._level)
                self._view.attach_team(self._team)
