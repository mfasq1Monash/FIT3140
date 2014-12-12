from maze import Maze
from math import cos, sin

class Facing:

    self.nameReference = {'North':0, 'East':90, 'South':180, 'West':270}
    self.angleReference = {0:'North', 90:'East', 180:'South', 270:'West'}

    def __init__(self, string):
        self.name = string
        self.angle = self.nameReference[self.name]

    def vector(self):
        return (self.cos(90 - angle), self.sin(90 - angle))

    def turn(self, n):
        self.angle = (self.angle + 90*n) % 360
        self.name = self.angleReference[self.angle]
        

class RobotIO:

    def __init__(self):
        self.maze = Maze()
        self.xcoord, self.ycoord = self.maze.getStartLocation()
        self.facing = Facing(self.maze.getStartFacing)

    def move(self, n):
        vector = self.facing.getVector()
        for i in range(n):
            if check_wall(vector, 1):
                raise WallHitError
            else:
                (self.xcoord, self.ycoord) += vector

    def turn(self, n):
        self.facing = self.facing.turn(n)

    def check_wall(self, vector, distance):
        return self.maze.isWall((self.xcoord, self.ycoord) + distance*vector)

    def detect_wall(self, dectectRange):
        vector = self.facing.getVector()
        for i in range(detectRange):
            if check_wall(vector, i):
                return i+1
        return i+1

    def detect_goal(self, detectRange):
        raise NotImplementedError
