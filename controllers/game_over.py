from views import GameOverView

from .base import PygameController


class GameOverController(PygameController):
    def run(self, window):
        view = GameOverView()
        view.display(window)
        self._run_loop()
