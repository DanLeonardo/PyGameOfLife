#!/usr/bin/python3
import pygame as pg
from pygame.locals import *
import argparse
from conway import GameOfLife

class Game:
    def __init__(self):
        self.width = 640
        self.height = 640
        self.fps = 60

        self.running = False
        self.playing = False

        self.step_rate = 0.5
        self.last_step = None

        self.tile_size = 32
        self.tile_width = 20
        self.tile_height = 20
        self.last_tile = None
        self.last_tile_mode = True

        # self.width = self.tile_width * self.tile_size
        # self.height = self.tile_height * self.tile_size

    def _setup(self):
        self.handle_arguments()
        self.screen = pg.display.set_mode((self.width, self.height))
        pg.display.set_caption('Conway\'s Game of Life')
        self.clock = pg.time.Clock()
        self.conway = GameOfLife(self.tile_width, self.tile_height)

    def _handle_events(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                button = event.button

                if not self.playing:
                    tile_x = mouse_x // self.tile_size
                    tile_y = mouse_y // self.tile_size
                    self.last_tile = (tile_x, tile_y)

                    if button == 1:
                        # Left Mouse Button
                        tile = self.conway.get_tile(tile_x, tile_y)
                        if tile is True:
                            self.conway.set_tile(tile_x, tile_y, False)
                            self.last_tile_mode = False
                        elif tile is False:
                            self.conway.set_tile(tile_x, tile_y, True)
                            self.last_tile_mode = True
                    elif button == 3:
                        # Right Mouse Button
                        self.conway.set_tile(tile_x, tile_y, False)
                        self.last_tile_mode = False
                    elif button == 2:
                        # Middle Mouse Button
                        self._start_playing()
                else:
                    if button == 2:
                        # Middle Mouse button
                        self.playing = False
                        self.conway.reset()

            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                buttons = event.buttons

                if not self.playing:
                    tile_x = mouse_x // self.tile_size
                    tile_y = mouse_y // self.tile_size

                    if (tile_x, tile_y) == self.last_tile:
                        break

                    if any(buttons):
                        if buttons[0]:
                            self.conway.set_tile(tile_x, tile_y, self.last_tile_mode)
                            self.last_tile = (tile_x, tile_y)
                        elif buttons[2]:
                            # Right Mouse Button
                            self.conway.set_tile(tile_x, tile_y, False)
                            self.last_tile = (tile_x, tile_y)

    def _update(self):
        if self.playing:
            cur_time = pg.time.get_ticks()
            if cur_time >= self.last_step + self.step_rate * 1000:
                self.last_step += self.step_rate * 1000
                changed = self.conway.step()

                if not changed:
                    print('No Activity Found. Stopping.')
                    self.playing = False

    def _draw(self):
        self.screen.fill((0, 0, 0))

        for y in range(self.tile_height):
            for x in range(self.tile_width):
                tile = self.conway.get_tile(x, y)
                if tile:
                    tile_color = (255, 255, 255)
                else:
                    tile_color = (0, 0, 0)

                tile_rect = pg.Rect(x*self.tile_size, y*self.tile_size, self.tile_size, self.tile_size)
                pg.draw.rect(self.screen, tile_color, tile_rect)
                pg.draw.rect(self.screen, (128, 128, 128), tile_rect, 2)

        pg.display.flip()

    def _start_playing(self):
        self.playing = True
        self.last_step = pg.time.get_ticks()

    def handle_arguments(self):
        argParser = argparse.ArgumentParser();
        argParser.add_argument('-grid',     '--grid-size',      type=int,   help='Size of the grid')
        argParser.add_argument('-grid-h',   '--grid-height',    type=int,   help='Height of the grid')
        argParser.add_argument('-grid-w',   '--grid-width',     type=int,   help='Width of the grid')

        argParser.add_argument('-cell',     '--cell-size',      type=int,   help='Size of each cell')
        argParser.add_argument('-update',   '--update-rate',    type=float,    help='Number of times per second to update')

        args = vars(argParser.parse_args())
        if args['grid_size']:
            self.tile_width = self.tile_height = args['grid_size']
        if args['grid_height']:
            self.tile_height = args['grid_height']
        if args['grid_width']:
            self.tile_width = args['grid_width']

        if args['cell_size']:
            self.tile_size = args['cell_size']
        if args['update_rate']:
            self.step_rate = args['update_rate']

        self.width = self.tile_width * self.tile_size
        self.height = self.tile_height * self.tile_size

    def run(self):
        self._setup()
        self.running = True

        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(self.fps)

if __name__ == '__main__':
    game = Game()
    game.run()
