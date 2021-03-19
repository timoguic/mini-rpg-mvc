import pygame
import pygame.locals

from constants import WINDOW_SIZE
from models import BigPotion, Hero, MonsterTeam, Shop, SmallPotion, Sword
from views import MainView

from .base import PygameController
from .game_over import GameOverController
from .level_done import LevelDoneController
from .shop import ShopController


class GameController(PygameController):
    """The main controller

    This is the main controller. It creates the models, and manages the game
    logic.
    """

    def __init__(self):
        pygame.init()

        # The main window
        self._window = pygame.display.set_mode(WINDOW_SIZE)

        # Instantiate the Hero
        self._hero = Hero()

        # Instantiate the Monsters
        self._level = 1
        self._team = MonsterTeam(self._level)

        # Create the main view
        self._view = MainView(self._window, self._hero)

        # "Attach" the team to the view
        self._view.attach_team(self._team)

        # Create the shop
        self._shop = Shop()

        # Add items to the shop
        # In your project, you probably want to do something fancier...
        for item in (Sword(), BigPotion(), SmallPotion(), SmallPotion()):
            self._shop.add_item(item)

    def run(self):
        """ This method runs the "main loop", and reacts to events (clicks) """
        running = True

        while running:
            # Display the view
            self._view.display()

            # Iheritance FTW - run a Pygame loop until the mouse is clicked
            mouse_position = self._run_loop()

            # Click on the close button
            if mouse_position is False:
                running = False
                continue

            # Click on the shop button
            if self._view.has_clicked_shop(mouse_position):
                # Let's run the shop controller
                shop_ctrl = ShopController(self._shop)
                # Run its loop
                shop_ctrl.run(self._window, self._hero)

            # Did we click on a monster?
            monster = self._view.get_clicked_monster(mouse_position)
            if monster is not None:
                # YAAAAA
                self._hero.attack(monster)
                # Update the display (the monster might be dead)
                self._view.display()

            # Oh noes, me so sad
            if self._hero.is_dead:
                # This shows the game over screen
                game_over_ctrl = GameOverController()
                game_over_ctrl.run(self._window)
                # We are dead - stop the loop
                running = False
                continue

            # Are all monsters dead now?
            if self._team.all_monsters_dead():
                # Yay. Let's show a nice message
                level_done_ctrl = LevelDoneController(self._level)
                level_done_ctrl.run(self._window)

                # We move to the next level
                self._level = self._level + 1

                # Recreate and attach a new team of monsters
                self._team = MonsterTeam(self._level)
                self._view.attach_team(self._team)
