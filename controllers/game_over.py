from views import GameOverView

from .base import PygameController


class GameOverController(PygameController):
    """ Controller to manage the game over screen """

    def run(self, window):
        # Self explanatory
        view = GameOverView()
        view.display(window)
        self._run_loop()
