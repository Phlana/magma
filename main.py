import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse


class Player:
    def __init__(self):
        self.image = pyglet.resource.image("sprites/player.png")

        self.h = 20  # health
        self.m = 7  # mana
        self.c = 10  # coins
        self.xp = 0  # experience

        self.PosX = 0  # players x position
        self.PosY = 0  # players y position


class Logic:
    def check_movement(self, symbol):
        if symbol == key.UP:
            player.PosY += 1
        if symbol == key.DOWN:
            player.PosY -= 1
        if symbol == key.RIGHT:
            player.PosX += 1
        if symbol == key.LEFT:
            player.PosX -= 1


window = pyglet.window.Window()
player = Player()
logic = Logic()


@window.event
def on_draw():
    window.clear()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    # glBegin(GL_TRIANGLES)
    # glVertex2f(0, 0)
    # glVertex2f(window.width, 0)
    # glVertex2f(window.width, window.height)
    # glEnd()

    player.image.blit(player.PosX, player.PosY)


@window.event
def on_key_press(symbol, modifiers):
    print("key pressed")
    logic.check_movement(symbol)


pyglet.app.run()
