

class CodeBlock(BoxLayout):
    """A block with an associated function and some number of text
    input arguments"""

    def __init__(self, name, numberOfParameters):
        self.name = name
        self.parameters = ['']*numberOfParameters
        block = self.ids.root
        for argument in self.parameters:
            block.add_widget(TextInput)

    def numberOfParameters(self):
        return len(self.parameters)
        
    def setParameter(self, parameterNum, parameter):
        self.parameter[parameterNum] = parameter

    def __str__(self):
        string = '(' + self.name
        for argument in self.parameters:
            string += ' ' + str(argument)
        string += ')'
        return string
