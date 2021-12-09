from bg.Cell import Cell
from random import randint

class Grid:

    def __init__(self, ncolumns: int, nrows: int, spawnchance=50) -> None:
        self.grid = []
        for row in range(nrows):
            self.grid.append([])
            for column in range(ncolumns):
                self.grid[-1].append(Cell((row, column)))
                x = randint(-100, 0)
                if x > spawnchance*-1:
                    self.grid[-1][-1].alive = 1

    @staticmethod
    def getlivings(grid):
        living_grid = []
        for row in grid:
            living_grid.append([])
            for cell in row:
                living_grid[-1].append(cell.getstatus())
        return living_grid

    def update(self):
        lvggrid = self.getlivings(self.grid)
        for row in self.grid:
            for cell in row:
                cell.update(lvggrid)

    def getgrid(self):
        return self.getlivings(self.grid)

class BetterGrid:
    def __init__(self, format, prespawn_alivecells=False, preloaded_grid=False):
        if preloaded_grid:
            self.grid = preloaded_grid
        else:
            self.grid = []
            for row in range(format[0]):
                self.grid.append([])
                for cell in range(format[1]):
                    if type(prespawn_alivecells) == int:
                        x = randint(-100, 0)
                        if x > prespawn_alivecells*-1:
                            x = 1
                        else:
                            x = 0
                    else:
                        x = 0
                    self.grid[-1].append(x)
        print("grid", len(self.grid), len(self.grid[-1]))
        print(self)

    def update(self):
        nextgrid = []
        for row in range(len(self.grid)):
            nextgrid.append([])
            for cell in range(len(self.grid[row])):
                nextgrid[-1].append(self.updatecell((row, cell)))

        self.grid = nextgrid
        del nextgrid

    def updatecell(self, pos):
        n = 0
        y = [-1, 0, 1, -1, 1, -1, 0, 1]
        x = [-1, -1, -1, 0, 0, 1, 1, 1]
        for i in range(8):
            try:
                n += self.grid[pos[0]+x[i]][pos[1]+y[i]]
            except:
                n += 0

        if (n == 3) or (n == 2 and self.grid[pos[0]][pos[1]] == 1):
            return 1
        else:
            return 0

    def getgrid(self):
        return self.grid


# DEBUG:
if __name__ == '__main__':
    g = Grid(50, 50)
    for gen in range(3):
        print(g.getgrid())
        g.update()
