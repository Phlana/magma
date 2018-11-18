import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse


class Player:
    def __init__(self):
        self.h = 20  # health
        self.m = 7  # mana
        self.c = 10  # coins
        self.xp = 0  # experience

        self.PosX = 0
        self.PosY = 0


window = pyglet.window.Window()

player = pyglet.resource.image("sprites/player.png")
playerobj = Player()


@window.event
def on_draw():
    window.clear()
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0, 0)
    glVertex2f(window.width, 0)
    glVertex2f(window.width, window.height)
    glEnd()

    player.blit(playerobj.PosX, playerobj.PosY)


@window.event
def on_key_press(symbol, modifiers):
    print("a key was pressed")
    if symbol == key.UP:
        playerobj.PosY += 1
    if symbol == key.DOWN:
        playerobj.PosY -= 1
    if symbol == key.RIGHT:
        playerobj.PosX += 1
    if symbol == key.LEFT:
        playerobj.PosX -= 1


pyglet.app.run()
