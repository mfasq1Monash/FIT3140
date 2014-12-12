"""A hard coded maze. It has a start location S (and facing South, a goal G,
and can return whether a given square is a wall."""

class Maze:

    
    def __init__(self):
        self.grid = [[0,1,1,0,'S',0,0,1,0],
                     [0,0,0,1,0,1,0,0,0],
                     [0,1,0,0,0,1,1,0,1],
                     [0,1,0,1,0,0,1,0,1],
                     [0,1,1,1,1,1,0,0,0],
                     [0,0,0,0,0,0,1,1,0],
                     [0,1,0,1,1,0,1,0,0],
                     [0,1,0,0,1,1,1,0,1],
                     [1,1,1,0,'G',1,0,0,0]]

    def getStartLocation(self):
        return (4,0)

    def getStartFacing(self):
        return 'South'

    def isWall(self, xcoord, ycoord):
        if self.grid[ycoord][xcoord] == 1:
            return True
        return False
