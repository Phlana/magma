import pyglet
from pyglet.gl import *
from pyglet.window import key, mouse


# Tile size
TILE_SIZE = 30


# a collection of all the sprites to be drawn on the screen
class GameSprites:
    def __init__(self):
        self.player = pyglet.resource.image("sprites/player.png")
        self.ground = pyglet.resource.image("terrain/ground.png")
        self.wall = pyglet.resource.image("terrain/wall.png")


# player class for player data and player movement
class Player:
    def __init__(self):
        # self.image = pyglet.resource.image("sprites/player.png")

        self.h = 20  # health
        self.m = 7  # mana
        self.c = 10  # coins
        self.xp = 0  # experience

        self.PosX = 0  # players x position
        self.PosY = 0  # players y position

        self.set_position(38, 32)

    # a function to set the players position to a specific spot in pixels
    def set_position(self, x, y):
        self.PosX = x
        self.PosY = y

    # move positive or negative integer spaces in x direction
    def move_x(self, tiles):
        self.PosX += tiles * TILE_SIZE

    # move positive or negative integer spaces in y direction
    def move_y(self, tiles):
        self.PosY += tiles * TILE_SIZE

    # move player depending on key pressed
    def check_movement(self, symbol):
        if symbol == key.UP:
            self.move_y(1)
        if symbol == key.DOWN:
            self.move_y(-1)
        if symbol == key.RIGHT:
            self.move_x(1)
        if symbol == key.LEFT:
            self.move_x(-1)


# the map image reading and building
class Field:
    def __init__(self):
        self.sprite_large = pyglet.image.load("map.png")
        self.grid = []
        self.field_sprites = []
        for y in range(self.sprite_large.width):
            tmp = []
            for x in range(self.sprite_large.height):
                tmp.append(0)
            self.grid.append(tmp)
        self.field_batch = pyglet.graphics.Batch()

        self.build_field()
        self.make_batch()
        # print(self.read_pix(1, 1))

    # builds the play field given a png with specific colors
    def build_field(self):
        # reads a color value of a pixel at specified location as RGB
        def read_pix(obj, pix_x, pix_y):
            # load specific pixel color
            pix = obj.sprite_large.get_region(pix_x, pix_y, 1, 1).get_image_data().get_data('RGB', 3)
            rgb = (pix[0], pix[1], pix[2])
            # returns color in its equivalent hex code
            return '%02x%02x%02x' % rgb

        for x in range(self.sprite_large.width):
            for y in range(self.sprite_large.height):
                hex_color = read_pix(self, x, y)
                # now find the tile matching this hex color
                if hex_color == "c3c3c3":
                    # add wall at x, y
                    self.grid[x][y] = 1
                    print("changed")
                elif hex_color == "b97a56":
                    # add ground at x, y
                    self.grid[x][y] = 0

    def make_batch(self):
        height = 0
        for row in self.grid:
            width = 0
            for val in row:
                if val == 0:
                    self.field_sprites.append(pyglet.sprite.Sprite(sprites.ground,
                                                                   x=width * TILE_SIZE, y=height * TILE_SIZE,
                                                                   batch=self.field_batch))
                    print("ground")
                elif val == 1:
                    self.field_sprites.append(pyglet.sprite.Sprite(sprites.wall,
                                                                   x=width * TILE_SIZE, y=height * TILE_SIZE,
                                                                   batch=self.field_batch))
                    print("wall")
                width += 1
            height += 1


class Window:
    def __init__(self):
        self.window = pyglet.window.Window(field.sprite_large.width * 10, field.sprite_large.height * 10)
        # glScalef(22.0, 22.0, 22.0)

        # event decorators
        self.on_draw = self.window.event(self.on_draw)
        self.on_key_press = self.window.event(self.on_key_press)
        self.on_mouse_click = self.window.event(self.on_mouse_click)

    # for drawing each frame of the window
    def on_draw(self):
        self.window.clear()

        # # The following two lines will change how textures are scaled.
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        # glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        # glBegin(GL_TRIANGLES)
        # glVertex2f(0, 0)
        # glVertex2f(window.width, 0)
        # glVertex2f(window.width, window.height)
        # glEnd()
        field.field_batch.draw()
        sprites.player.blit(player.PosX, player.PosY)

    # for detecting if a key has been pressed
    def on_key_press(self, symbol, modifiers):
        print("key pressed")
        player.check_movement(symbol)

    # for detecting if the mouse has been clicked
    def on_mouse_click(self, button, modifiers):
        pass


sprites = GameSprites()
player = Player()
field = Field()
window = Window()

pyglet.app.run()
