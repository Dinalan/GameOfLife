class Cell:
    def __init__(self, pos):
        self.alive = 0
        self.neighbors = self.getneighbors(pos)

    @staticmethod
    def getneighbors(pos):
        neighbors = []

        # UPPER LEFT NEIGHBOR
        neighbors.append((pos[0]-1, pos[1]-1))
        # UPPER NEIGHBOR
        neighbors.append((pos[0]-1, pos[1]))
        # UPPER RIGHT NEIGHBOR
        neighbors.append((pos[0]-1, pos[1]+1))
        # LEFT NEIGHBOR
        neighbors.append((pos[0], pos[1]-1))
        # RIGHT NEIGHBOR
        neighbors.append((pos[0], pos[1]+1))
        # DOWN LEFT NEIGHBOR
        neighbors.append((pos[0]+1, pos[1]-1))
        # DOWN NEIGHBOR
        neighbors.append((pos[0]+1, pos[1]))
        # DOWN RIGHT NEIGHBOR
        neighbors.append((pos[0]+1, pos[1]+1))

        return neighbors

    def getstatus(self) -> int:
        return self.alive

    def update(self, living_grid):
        n = 0
        for neighbor in self.neighbors:
            try:
                n += living_grid[neighbor[0]][neighbor[1]]
            except:
                n += 0

        # CONWAY'S RULES:
        chg = 0
        if self.alive == 1 and n == 2 or n == 3:
            chg = 1
        if self.alive == 0 and n == 3:
            self.alive = 1
            chg = 1
        if chg == 0:
            self.alive = 0
