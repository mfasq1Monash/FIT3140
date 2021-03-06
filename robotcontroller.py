'''
Author: Michael Asquith, Aaron Gruneklee
Created: 2014.12.12
Last Modified: 2014.12.23

The brain of the robot. Has access to the robot's I/O, interpreter and
instructions
'''


from interpreter import Interpreter
from robotio import RobotIO
from codeblock import CodeBlock
from maze import Maze

class RobotController():
    """studentProgram is the robot's instructions"""

    def __init__(self):
        self.maze = Maze()
        self.robotio = RobotIO(self.maze)
        

    def executeProgram(self, filename):
        """Executes the robot's program"""
        code = open(filename, 'r')
        inter = Interpreter(self.robotio)
        for line in code:
            inter.interpret(line)

    def getRobotLocationAndFacing(self):
        return self.robotio.getLocationAndFacing()

    def getMaze(self):
        return self.maze.getMaze()
