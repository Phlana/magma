"""File for the majority of menu screens"""
from pyglet.window import key, mouse


class Menu:
    def __init__(self):
        self.sprite = None


class StartMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
