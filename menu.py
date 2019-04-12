"""File for the majority of menu screens and scenes"""
import pyglet
from pyglet.window import key, mouse


class Menu(pyglet.window.Window):
    def __init__(self):
        super().__init__()
        self.menu_s = None


class Scene:
    def __init__(self):
        self.bg_s = None


class StartMenu(Menu):
    def __init__(self):
        # Menu.__init__(self)
        super().__init__()


class PauseMenu(Menu):
    def __init__(self):
        super().__init__()


class TravelScene(Scene):
    def __init__(self):
        super().__init__()


class CombatScene(Scene):
    def __init__(self):
        super().__init__()


class BoatCombat(CombatScene):
    def __init__(self):
        super().__init__()
