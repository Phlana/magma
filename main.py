import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import mouse


class GameSprites:
    def __init__(self):
        self.player = pyglet.resource.image("sprites/player.png")
        self.ground = pyglet.resource.image("sprites/terrain/ground.png")
        self.wall = pyglet.resource.image("sprites/terrain/wall.png")


class Player:
    def __init__(self):
        # self.image = pyglet.resource.image("sprites/player.png")

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


class Map:
    def __init__(self):
        self.map = pyglet.image.load("map.png")
        self.grid = []
        self.map_sprites = []
        for y in range(self.map.width):
            tmp = []
            for x in range(self.map.height):
                tmp.append(0)
            self.grid.append(tmp)
        self.map_batch = pyglet.graphics.Batch()

        self.build_map()
        self.make_batch()

    def read_pix(self, pix_x, pix_y):
        # reads a color value of a pixel at specified location as RGB
        pix = self.map.get_region(pix_x, pix_y, 1, 1).get_image_data().get_data('RGB', 3)
        rgb = (pix[0], pix[1], pix[2])
        # returns its equivalent hex code
        return '%02x%02x%02x' % rgb

    def build_map(self):
        # building world
        for x in range(self.map.width):
            for y in range(self.map.height):
                hex_color = self.read_pix(x, y)
                # now find the tile matching this hex color
                if hex_color == "":
                    # add tree at x, y
                    self.grid[x][y] = 1
                    print("changed")

    def make_batch(self):
        height = 0
        for row in self.grid:
            width = 0
            for val in row:
                if val == 0:
                    self.map_sprites.append(pyglet.sprite.Sprite(sprites.ground, x=width*20, y=height*20, batch=self.map_batch))
                    print("ground")
                elif val == 1:
                    self.map_sprites.append(pyglet.sprite.Sprite(sprites.wall, x=width*20, y=height*20, batch=self.map_batch))
                    print("wall")
                width += 1
            height += 1


window = pyglet.window.Window()
sprites = GameSprites()
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

    sprites.player.blit(player.PosX, player.PosY)


@window.event
def on_key_press(symbol, modifiers):
    print("key pressed")
    logic.check_movement(symbol)


pyglet.app.run()
