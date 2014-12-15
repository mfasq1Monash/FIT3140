from interpreter import Interpreter
from robotio import RobotIO
from codeblock import CodeBlock

class RobotController():
    """A block with an associated function and some number of text
    input arguments"""

    def __init__(self, studentProgram):
        self.program = studentProgram
        self.robotio = RobotIO()

    def executeProgram(self):
        inter = Interpreter(self.robotio)
        for codeBlock in self.program:
            Interpreter.interpret(str(codeBlock))

    def numberOfParameters(self):
        return len(self.parameters)
