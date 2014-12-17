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
from kivy.garden.magnet import Magnet



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
            

    


''' a primary block is the base level for the display of the users code '''

class primaryBlock(Magnet):
    dragged = BooleanProperty(False)
    def __init__(self, typeValue):
        super(primaryBlock, self).__init__()
        self.ids.size_hint = (None,None)
        if str(typeValue).capitalize in ['X','Y', 'Z']:
            box = TextInput(text= 'enter value or drag code block', size_hint=(.3,1))
            # box.bind(on_) need to bind to a method to accept value or a codeBlock
            self.add_widget(box)

        else:
            box = Button(text=typeValue, size=(60,80))

            self.add_widget(box)


    def on_touch_down(self, touch, *args):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            self.remove_widget(self)

            self.app.root.add_widget(self)
            self.center = touch.pos
            self.img.center = touch.pos
            return True
 
        return super(DraggableImage, self).on_touch_down(touch, *args)
 
    def on_touch_move(self, touch, *args):
        grid_layout = self.app.root.ids.grid_layout
        float_layout = self.app.root.ids.float_layout
 
        if touch.grab_current == self:
            self.img.center = touch.pos
            if grid_layout.collide_point(*touch.pos):
                grid_layout.remove_widget(self)
                float_layout.remove_widget(self)
 
                for i, c in enumerate(grid_layout.children):
                    if c.collide_point(*touch.pos):
                        grid_layout.add_widget(self, i - 1)
                        break
                else:
                    grid_layout.add_widget(self)
            else:
                if self.parent == grid_layout:
                    grid_layout.remove_widget(self)
                    float_layout.add_widget(self)
 
                self.center = touch.pos
 
        return super(DraggableImage, self).on_touch_move(touch, *args)
 
    def on_touch_up(self, touch, *args):
        if touch.grab_current == self:
            self.app.root.remove_widget(self.img)
            self.add_widget(self.img)
            touch.ungrab(self)
            return True
 
        return super(DraggableImage, self).on_touch_up(touch, *args)

    # def on_touch_down(self, touch):
    #     if self.collide_point(touch.x, touch.y):
    #         self.dragged = True
    
    # def on_touch_move(self, touch):
    #     if self.dragged:
    #         self.center_x = touch.x
    #         self.center_y = touch.y

    # def on_touch_up(self, touch):
    #     if self.dragged:
    #         self.dragged = False



class testCodeBlock(App):
    def build(self):
        
        return CodeBlock('(add x y)')


if __name__ == "__main__":
    testCodeBlock().run()