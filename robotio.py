'''
Author:        Michael Asquith, Aaron Gruneklee
Created:       2014.12.12
Last Modified: 2014.12.23

The input and output controls of a robot. It can turn 90 degree angles, move a
given number of spaces in its current direction and detect walls and goals
in front of itself.

'''

from maze import Maze
from math import cos, sin, radians

"""Class used by the robot to determine which direction it is facing"""
class Facing:
    """direction must North, East, South or West"""
    nameReference = {'North':0, 'East':90, 'South':180, 'West':270}
    angleReference = {0:'North', 90:'East', 180:'South', 270:'West'}

    def __init__(self, direction):
        self.name = direction
        self.angle = self.nameReference[self.name]

    def getVector(self):
        """Returns a unit vector based on the current direction"""
        return (int(cos(radians(90 - self.angle))), int(sin(radians(self.angle - 90))))

    def turn(self, n):
        """Turns 90 degrees clockwise n times"""
        self.angle = (self.angle + 90*n) % 360
        self.name = self.angleReference[self.angle]
        

class RobotIO:
    """The input and output of a robot."""

    def __init__(self, newMaze=Maze()):
        self.maze = newMaze
        self.xcoord, self.ycoord = self.maze.getStartLocation()
        self.facing = Facing(self.maze.getStartFacing())

    def move(self, n):
        """Attempt to move n spaces in the robot's current direction.
        Cannot move into a space with a wall in it.
        """
        vector = self.facing.getVector()
        for i in range(n):
            if self.check_wall(vector, 1):
                break
            else:
                self.xcoord += vector[0]
                self.ycoord += vector[1]

    def turn(self, n):
        """Make n 90 degree clockwise turns."""
        self.facing.turn(n)

    def check_wall(self, unitvector, distance):
        """Checks if there is a wall *distance* in the direction *unitvector*"""
        vector = [i*distance for i in unitvector]
        xcheck = self.xcoord + vector[0]
        ycheck = self.ycoord + vector[1]
        return self.maze.isWall(xcheck, ycheck)

    def detect_wall(self, detectRange):
        """Detects the first wall directly in front of the robot within detectRange"""
        vector = self.facing.getVector()
        for i in range(1, detectRange+1):
            if self.check_wall(vector, i):
                return i
        return i

    def detect_goal(self, detectRange):
        for i in range(-detectRange, detectRange+1):
            for j in range(-detectRange, detectRange+1):
                if self.maze.isGoal(self.xcoord + i, self.ycoord + j):
                    return abs(i) + abs(j)
        return 2*detectRange
                

    def getLocationAndFacing(self):
        """Returns the robot's location and direction"""
        return (self.xcoord, self.ycoord, self.facing.name)

if __name__ == '__main__':
    robot = RobotIO()
    failed_tests = []

    # Move and turn
    print "---Move and turn---"
    tests = [
        ['m', 0, 'Control',                  4,0,'South'],
        ['m', 2, 'Moving South',             4,2,'South'],
        ['t', 1, 'Turning once',             4,2,'West'],
        ['m', 1, 'Moving West',              3,2,'West'],
        ['t', 2, 'Turning twice',            3,2,'East'],
        ['m', 1, 'Moving East',              4,2,'East'],
        ['m', 2, 'Moving into a wall',       4,2,'East'],
        ['t', 3, 'Turning thrice',           4,2,'North'],
        ['m', 6, 'Moving to the maze edge',  4,0,'North']]

    for i in range(len(tests)):
        curr = tests[i]
        
        if curr[0] == 'm':
            robot.move(curr[1])
            result = [robot.xcoord, robot.ycoord]
            if result != tests[i][3:5]:
                failed_tests.append(curr)
                
        if curr[0] == 't':
            robot.turn(curr[1])
            result = robot.facing.name
            if result != tests[i][-1]:
                failed_tests.append(curr)
                
        print "Test ", i
        print curr[0], "should return", curr[3:], "\n", result 
        print

    if failed_tests:
        print "failed tests are:"
    else:
        print "turn and move pass"
        
    for i in range(len(failed_tests)):
        print failed_tests[i]
    raw_input()
        

    # Detect Wall

    print "---Detect Wall---"
    robot = RobotIO()
    failed_tests = []
    tests = [
        [4, 'Detect range too big',         5],
        [4, 'Detect range exact',           4],
        [3, 'Detect range too small',       3],
        [2, 'Detect range too big (turned)',6],
        [2, 'Detect range exact (turned)',  2],
        [1, 'Detect range too small',       1],
        [1, 'Detecting into wall',          5]]

    for i in range(len(tests)):
        curr = tests[i]

        if i == 3 or i == 6:
            robot.turn(1)

        result = robot.detect_wall(curr[2])
        if curr[0] != result:
            failed_tests.append(curr)

        print "Test ", i
        print curr[2], "should return", curr[0], "\n", result
        print

    if failed_tests:
        print "failed tests are:"
    else:
        print "detect wall pass"
        
    for i in range(len(failed_tests)):
        print failed_tests[i]
    raw_input()
    
    # Detect Goal

    print "---Detect Goal---"
    robot = RobotIO()
    failed_tests = []
    tests = [
        [4, 8, 'On goal', 0, 4],
        [3, 8, 'One x co-ord away', 1, 10],
        [5, 8, 'One x co-ord away', 1, 10],
        [4, 7, 'One y co-ord away', 1, 10],
        [4, 9, 'One y co-ord away', 1, 10],
        [3, 7, 'One diagonal space away', 2, 10],
        [-378, 200, 'A long distance away', 574, 400],
        [-378, 200, 'Too far away', 20, 10]]

    for i in range(len(tests)):
        curr = tests[i]
        robot.xcoord = curr[0]; robot.ycoord = curr[1]
        result = robot.detect_goal(curr[4])
        if curr[3] != result:
            failed_tests.append(curr)

        print "Test ", i
        print curr[0:2], "should return", curr[3], "\n", result
        print

    if failed_tests:
        print "failed tests are:"
    else:
        print "detect goal pass"
        
    for i in range(len(failed_tests)):
        print failed_tests[i]
    raw_input()
