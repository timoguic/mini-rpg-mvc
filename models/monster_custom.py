""" We can define some custom classes based on our main Monster class.

For brevity reasons, I kept them very simple. Yours would be more complicated.
"""

from .monster import Monster


class Wolf(Monster):
    image_file = "assets/img/wolf.png"


class Giant(Monster):
    image_file = "assets/img/giant.png"


class Magician(Monster):
    image_file = "assets/img/magician.png"
