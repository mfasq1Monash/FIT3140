'''
# Author:        Michael Asquith
# Created:       2014.12.12
# Last Modified: 2014.12.15

A hard coded maze. It has a start location S (and facing South, a goal G,
and can return whether a given square is a wall. All spaces outside the maze
borders are considered walls.

'''

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
        self.xdimension = 9
        self.ydimension = 9

    def getStartLocation(self):
        return (4,0)

    def getStartFacing(self):
        return 'South'

    def isWall(self, xcoord, ycoord):
        if( xcoord < 0 or ycoord < 0 or
            xcoord >= self.xdimension or ycoord >= self.ydimension):
            return True
        if self.grid[ycoord][xcoord] == 1:
            return True
        return False
