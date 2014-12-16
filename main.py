'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.08
# Last Modified: 2014.12.15

this is the main controler class it is responsible for displaying the 3 views and
controls the 5 input buttons.

'''

from kivy import require
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty
from codeblock import CodeBlock
from functionlist import FunctionList


#Kivy version check
require('1.8.0')


class FunctionalProgrammerWidget(BoxLayout):
    # set all the properties of the Controller

    text_colour = ListProperty([1, 0, 0, 1])	
    commands = ['+ x y', '- x y', '* x y', '/ x y', '% x y', '> x y', '< x y', '>= x y', '<= x y', '= x y', 'and x y', 'or x y', 'not x y']
    student_Program = ObjectProperty(None)
    code_View = ObjectProperty(None)
    run_View = ObjectProperty(None)
    debug_View = ObjectProperty(None)
    current_view = ObjectProperty(None)
    save_Buttton = ObjectProperty(None)
    load_Buttton = ObjectProperty(None)
    run_Buttton = ObjectProperty(None)
    debug_Buttton = ObjectProperty(None)
    exit_Buttton = ObjectProperty(None)

    def __init__(self):
            super(FunctionalProgrammerWidget, self).__init__()
            # self.ids.predefined_code.add_widget(FunctionList(self.commands))

            self.ids.predefined_code.add_widget(FunctionList(['this',
                'is','a','test']))
            # for command in self.commands:
    #  		cmd = command.split()
    #  		self.cmnds = self.ids.predefined_code.add_widget(FunctionList())
    #  		cmnds.append(cmd[0])

                    # self.ids.predefined_code.add_widget(CodeBlock(cmd[0], len(cmd) - 1))


    ''' saves user program to user defined location '''
    def save_Button(self):
            self.ids.save_Button.text = 'not yet implemented'
                    

    ''' loads a user program from a user defined location '''
    def load_Button(self):
            self.ids.load_Button.text = 'not yet implemented'
                    

    ''' displays maze and robot traversing through the maze '''
    def run_Button(self):
            # current_view = run_View
            self.ids.run_Button.text = 'not yet implemented'
                    

    ''' displays maze and robot traversing through the maze alongside 
    the user program as it steps through the code'''
    def debug_Button(self):
            # current_view = debug_View
            self.ids.debug_Button.text = 'not yet implemented'


class FunctionalProgrammerApp(App):
    def build(self):
        return FunctionalProgrammerWidget()

if __name__ == '__main__':
    FunctionalProgrammerApp().run()
