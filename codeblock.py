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
from kivy.properties import ListProperty, ObjectProperty, BooleanProperty
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
# from kivy.garden.magnet import Magnet



''' the code Block is a group of primary blocks that make 
up a block of code that can be dragged and dropped '''

class CodeBlock(GridLayout):
    """A block with an associated function and some number of text
    input arguments"""
    dragged = BooleanProperty(False)

    def __init__(self, name):
        super(CodeBlock, self).__init__()
        layout = BoxLayout(orientation= 'horizontal')

        
        parameters = name.replace('(', '( ').replace(')', ' )').split()
        self.cols = len(parameters)
        for param in parameters:
            layout.add_widget(PrimaryBlock(param))

        self.add_widget(layout)
            

    


''' a primary block is the base level for the display of the users code '''

class PrimaryBlock(BoxLayout):
    dragged = BooleanProperty(False)
    app = ObjectProperty(None)
    def __init__(self, typeValue):
        super(PrimaryBlock, self).__init__()
        self.ids.size_hint = (None,None)
        if typeValue in ['X','Y', 'Z','x', 'y', 'z']:
            box = TextInput(text= 'enter value or drag code block', size_hint=(.3,1))
            
            self.add_widget(box)

        else:
            box = Button(text=typeValue, size=(60,80))

            self.add_widget(box)


    
    

  

    def on_textinput(self):
        
        # super(TextInput, self)
        self = self.addCode(self.text)


class testCodeBlock(App):
    def build(self):
        
        return CodeBlock('(add x y)')


if __name__ == "__main__":
    testCodeBlock().run()