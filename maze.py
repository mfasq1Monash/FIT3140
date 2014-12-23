'''
# Author:        Michael Asquith, Aaron Gruneklee
# Created:       2014.12.12
# Last Modified: 2014.12.23

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

    def isItem(self, xcoord, ycoord, item):
        if (0 <= xcoord and self.xdimension > xcoord and
            0 <= ycoord and self.ydimension > ycoord):
            
            return self.grid[ycoord][xcoord] == item
        return False
            
    def isWall(self, xcoord, ycoord):
        if( xcoord < 0 or ycoord < 0 or
            xcoord >= self.xdimension or ycoord >= self.ydimension):
            return True
        if self.isItem(xcoord, ycoord, 1):
            return True
        return False

    def isGoal(self, xcoord, ycoord):
        return self.isItem(xcoord, ycoord, 'G')

if __name__ == '__main__':
    maze = Maze()
    failed_tests = []

    # isWall
    tests = [[(1,0),'Wall in maze', True],
             [(0,0),'Corner',False],
             [(8,8),'Corner',False],
             [(0,-1),'Too small Y', True],
             [(-1,0),'Too small X', True],
             [(8,9),'Too big Y', True],
             [(9,8),'Too big X', True]]

    for i in range(len(tests)):
        curr = tests[i]
        result = maze.isWall(curr[0][0], curr[0][1])
        if result != curr[2]:
            failed_tests.append(curr)
        print "Test ", i
        print curr[0], "should return", curr[2], "\n", result 
        print

    if failed_tests: print "failed tests are:"
    for i in range(len(failed_tests)):
        print "Test ", i, " ", failed_tests[i]
    raw_input()
