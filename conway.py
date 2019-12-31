import copy

class GameOfLife:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = None
        self._init_grid()

    def _init_grid(self):
        self.grid = []
        for x in range(self.width):
            self.grid.append([False for tile in range(self.height)])

    def print_grid(self):
        if not self.grid:
            return

        for y in range(self.height):
            for x in range(self.width):
                tile = self.get_tile(x, y)
                if tile == False:
                    print('.', end='')
                else:
                    print('#', end='')
            print('\n', end='')

    def step(self):
        tile_counts = [[0 for y in range(self.height)] for x in range(self.width)]
        new_tiles = copy.deepcopy(self.grid)
        change = False

        for y in range(self.height):
            for x in range(self.width):
                tile = self.get_tile(x, y)
                tiles = 0

                # Up
                if self.get_tile(x, y-1):
                    tiles += 1
                # Down
                if self.get_tile(x, y+1):
                    tiles += 1
                # Left
                if self.get_tile(x-1, y):
                    tiles += 1
                # Right
                if self.get_tile(x+1, y):
                    tiles += 1
                # Up-Left
                if self.get_tile(x-1, y-1):
                    tiles += 1
                # Up-Right
                if self.get_tile(x+1, y-1):
                    tiles += 1
                # Down-Left
                if self.get_tile(x-1, y+1):
                    tiles += 1
                # Down-Right
                if self.get_tile(x+1, y+1):
                    tiles += 1

                if tile:
                    if tiles not in (2, 3):
                        # Live tile dies if less than 2 or more than 3 neighbors
                        new_tiles[x][y] = False
                        change = True
                else:
                    if tiles == 3:
                        # Dead tile lives if exactly 3 neighbors
                        new_tiles[x][y] = True
                        change = True

        self.grid = new_tiles
        return change

    def get_tile(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        else:
            return self.grid[x][y]

    def get_tiles(self):
        return self.grid

    def set_tile(self, x, y, live=True):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return None
        else:
            self.grid[x][y] = live

    def reset(self):
        self._init_grid()

if __name__ == '__main__':
    game = GameOfLife(7, 7)
    num_steps = 4

    game.set_tile(1, 1)
    game.set_tile(2, 2)
    game.set_tile(0, 3)
    game.set_tile(1, 3)
    game.set_tile(2, 3)

    print('Starting Grid:')
    game.print_grid()
    print('\n', end='')

    for step in range(num_steps):
        print('Step %d:' % (step+1))
        game.step()
        game.print_grid()
        print('\n', end='')
