from maze import Maze
from math import cos, sin, radians

class Facing:

    nameReference = {'North':0, 'East':90, 'South':180, 'West':270}
    angleReference = {0:'North', 90:'East', 180:'South', 270:'West'}

    def __init__(self, string):
        self.name = string
        self.angle = self.nameReference[self.name]

    def getVector(self):
        return (int(cos(radians(90 - self.angle))), int(sin(radians(self.angle - 90))))

    def turn(self, n):
        self.angle = (self.angle + 90*n) % 360
        self.name = self.angleReference[self.angle]
        

class RobotIO:

    def __init__(self):
        self.maze = Maze()
        self.xcoord, self.ycoord = self.maze.getStartLocation()
        self.facing = Facing(self.maze.getStartFacing())

    def move(self, n):
        vector = self.facing.getVector()
        for i in range(n):
            if check_wall(vector, 1):
                raise WallHitError
            else:
                (self.xcoord, self.ycoord) = (self.xcoord + self.ycoord)
                + vector

    def turn(self, n):
        self.facing = self.facing.turn(n)

    def check_wall(self, unitvector, distance):
        vector = [i*distance for i in unitvector]
        xcheck = self.xcoord + vector[0]
        ycheck = self.ycoord + vector[1]
        return self.maze.isWall(xcheck, ycheck)

    def detect_wall(self, detectRange):
        vector = self.facing.getVector()
        for i in range(1, detectRange+1):
            if self.check_wall(vector, i):
                return i
        return i

    def detect_goal(self, detectRange):
        raise NotImplementedError
