'''
Author:         Aaron Gruneklee, Michael Asquith
Created:        2014.12.08
Last Modified:  2014.12.15

this represents one block of code that has a function and function arguments


***  currently not returning correct display elements  ***

'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty

class CodeBlock(BoxLayout):
    """A block with an associated function and some number of text
    input arguments"""
    name = ''
    parameters = ['']
    def __init__(self, name, numberOfParameters):
        super(CodeBlock, self).__init__()
        
        self.name = name
        self.parameters = ['']*numberOfParameters
        # self.ids.code_button.text = self.name
        # block = self.ids.root
        # for argument in self.parameters:
        #     block.add_widget(TextInput())

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


class testCodeBlock(App):
    def build(self):
        
        return CodeBlock('test', 2)



if __name__ == "__main__":
    testCodeBlock().run()