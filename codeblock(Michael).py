

class CodeBlock():
    """A block with an associated function and some number of text
    input arguments"""

    def __init__(self, name, numberOfParameters):
        self.name = name
        self.parameters = ['']*numberOfParameters

    def numberOfParameters(self):
        return len(self.parameters)

    def __str__(self):
        string = '(' + self.name
        for argument in self.parameters:
            string += ' ' + str(argument)
        string += ')'
        return string
