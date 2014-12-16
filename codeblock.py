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
            layout.add_widget(primaryBlock(param))

        self.add_widget(layout)
            

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.dragged = True
    
    def on_touch_move(self, touch):
        if self.dragged:
            self.center_x = touch.x
            self.center_y = touch.y

    def on_touch_up(self, touch):
        if self.dragged:
            self.selected = False


''' a primary block is the base level for the display of the users code '''

class primaryBlock(Widget):

    def __init__(self, typeValue):
        super(primaryBlock, self).__init__()
        self.ids.size_hint = (None,None)
        if str(typeValue).capitalize == 'X' or 'Y':
            box = TextInput(text= 'enter value or drag code block', size_hint=(.3,1))
            # box.bind(on_) need to bind to a method to accept value or a codeBlock
            self.add_widget(box)

        else:
            box = Label(text=typeValue, size=(60,80))

            self.add_widget(box)

        



class testCodeBlock(App):
    def build(self):
        
        return CodeBlock('(add 5 5)')


if __name__ == "__main__":
    testCodeBlock().run()