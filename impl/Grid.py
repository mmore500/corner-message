from impl.Tile import Tile

class Grid:

    def __init__(self, dim):
        self.grid = [[Tile() for __ in range(dim)] for __ in range(dim)]

        pairs = list(zip(range(-1, dim), range(dim)))

        for y in range(dim):
            for x1, x2 in pairs:
                self.grid[x1][y].link(self.grid[x2][y], 'h', 1)
                self.grid[x2][y].link(self.grid[x1][y], 'h', -1)

        for x in range(dim):
            for y1, y2 in pairs:
                self.grid[x][y1].link(self.grid[x][y2], 'v', 1)
                self.grid[x][y2].link(self.grid[x][y1], 'v', -1)

        self.draw()

    def draw(self):
        print(
            '\n'.join(
                ['\t|'.join(
                    [str(cell) for cell in row]) for row in reversed(list(zip(*self.grid)))]
            )
        )
        print()

    def run(self):
        while self.step():
            pass

    def step(self):
        return any(t.trySendMessage() for r in self.grid for t in r)
