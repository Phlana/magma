import pyglet
from pyglet.gl import *
from pyglet.window import key, mouse
from menu import *

# Tile size
TILE_SIZE = 80
# boolean for pausing and unpausing game
paused = False


# a collection of all the sprites to be drawn on the screen
class GameSprites:
    def __init__(self):
        self.player = pyglet.resource.image("sprites/player.png")
        self.ground = pyglet.resource.image("terrain/ground.png")
        self.wall = pyglet.resource.image("terrain/wall.png")
        self.p_info = pyglet.resource.image("sprites/info.png")


# player class for player data and player movement
class Player:
    def __init__(self):
        # self.image = pyglet.resource.image("sprites/player.png")
        # player values
        self.h = 20  # health
        self.m = 7  # mana
        self.c = 10  # coins
        self.xp = 0  # experience

        self.PosX = 0  # players x position
        self.PosY = 0  # players y position

        self.set_position(4, 4)

    # a function to set the players position to a specific spot in tiles
    def set_position(self, x, y):
        self.PosX = x * TILE_SIZE
        self.PosY = y * TILE_SIZE

    # move positive or negative integer tiles in x direction
    def move_x(self, tiles):
        self.PosX += tiles * TILE_SIZE

    # move positive or negative integer tiles in y direction
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
# class Field:
#     def __init__(self):
#         self.sprite_large = pyglet.image.load("map.png")
#         self.grid = []
#         for y in range(self.sprite_large.width):
#             tmp = []
#             for x in range(self.sprite_large.height):
#                 tmp.append(0)
#             self.grid.append(tmp)
#
#         self.field_x = None
#         self.field_y = None
#         self.field_sprites = []
#
#         self.field_batch = pyglet.graphics.Batch()
#
#         self.build_grid()
#         self.make_batch()
#
#     # builds the grid of the play field given a png with very specific colors
#     def build_grid(self):
#         # reads a color value of a pixel at specified location as RGB
#         def read_pix(self_, pix_x, pix_y):
#             # load specific pixel color
#             pix = self_.sprite_large.get_region(pix_x, pix_y, 1, 1).get_image_data().get_data('RGB', 3)
#             rgb = (pix[0], pix[1], pix[2])
#             # returns color in its equivalent hex code
#             return '%02x%02x%02x' % rgb
#
#         for x in range(self.sprite_large.width):
#             for y in range(self.sprite_large.height):
#                 hex_color = read_pix(self, x, y)
#                 # now find the tile matching this hex color
#                 if hex_color == "c3c3c3":
#                     # add wall at x, y
#                     self.grid[x][y] = 0
#                     print("changed")
#                 elif hex_color == "b97a56":
#                     # add ground at x, y
#                     self.grid[x][y] = 1
#                 # elif hex_color == "":  # additional tile types
#
#     def make_batch(self):
#         height = 0
#         for row in self.grid:
#             width = 0
#             for val in row:
#                 if val == 0:
#                     # self.field_sprites.append(pyglet.sprite.Sprite(sprites.wall,
#                     #                                                x=width * TILE_SIZE, y=height * TILE_SIZE,
#                     #                                                # batch=self.field_batch))
#                     #                                                ))
#                     b_return = self.field_batch.add()
#                     print("wall")
#                 elif val == 1:
#                     # self.field_sprites.append(pyglet.sprite.Sprite(sprites.ground,
#                     #                                                x=width * TILE_SIZE, y=height * TILE_SIZE,
#                     #                                                # batch=self.field_batch))
#                     #                                                ))
#                     print("ground")
#                 # elif val == 2:  # additional tile types
#                 width += 1
#             height += 1
#         self.field_x = width
#         self.field_y = height
#
#     # def draw(self, player_x, player_y):
#     #     for x in range(self.field_x):
#     #         for y in range(self.field_y):
#     #             self.field_sprites[x * self.field_x + self.field_y].draw()
#     #     for tile in self.field_sprites:
#     #         tile.draw()


class Window:
    def __init__(self):
        self.paused = False
        self.window = pyglet.window.Window(1280, 720)
        # self.scene = StartMenu(self.window)

        # glScalef(22.0, 22.0, 22.0)

        # event decorators
        self.on_draw = self.window.event(self.on_draw)
        self.on_key_press = self.window.event(self.on_key_press)
        self.on_mouse_press = self.window.event(self.on_mouse_press)

    # for drawing each frame of the window during gameplay
    def on_draw(self):
        # clearing window for redrawing the frame
        self.window.clear()

        # enabling texture transparency
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        # glClearColor(0.0, 0.0, 0.0, 0.0)
        # glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()

        # draw background
        # field.draw(player.PosX, player.PosY)

        # drawing player
        # field.field_batch.draw()
        sprites.player.blit(601, 321)

        # drawing various entities

        # drawing various info
        # pyglet.graphics.draw(4, GL_POLYGON, ("v2i", (1000, 0, 1280, 0, 1280, 720, 1000, 720)))
        sprites.p_info.blit(0, 640)

    # for detecting if a key has been pressed
    def on_key_press(self, symbol, modifiers):
        print("key pressed")
        player.check_movement(symbol)

    # for detecting if the mouse has been clicked
    def on_mouse_press(self, x, y, button, modifiers):
        print("mouse pressed")


if __name__ == "__main__":
    sprites = GameSprites()
    player = Player()
    # field = Field()
    window = Window()

    pyglet.app.run()

