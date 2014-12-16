'''
Author: Michael Asquith, Aaron Gruneklee
Created: 2014.12.08
Last Modified: 2014.12.15

The brain of the robot. Has access to the robot's I/O, interpreter and
instructions
'''


from interpreter import Interpreter
from robotio import RobotIO
from codeblock import CodeBlock

class RobotController():
    """studentProgram is the robot's instructions"""

    def __init__(self, studentProgram):
        self.program = studentProgram
        self.robotio = RobotIO()

    def executeProgram(self):
        """Executes the robot's program"""
        inter = Interpreter(self.robotio)
        for codeBlock in self.program:
            inter.interpret(str(codeBlock))

