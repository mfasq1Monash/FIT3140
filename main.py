'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.08
# Last Modified: 2014.12.19

this is the main controler class it is responsible for displaying the 3 views and
controls the 5 input buttons.

'''

from kivy import require
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, ObjectProperty
# from codeblock import CodeBlock
from functionlist import FunctionList
from kivy.uix.screenmanager import ScreenManager, Screen
from programmerview import ProgrammerView
from robotcontroller import RobotController
from runscreen import RunScreen


#Kivy version check
require('1.8.0')
__version__ = '0.1'


class FunctionalProgrammerWidget(BoxLayout):
    # set all the properties of the Controller

    text_colour = ListProperty([1, 0, 0, 1])
    # current_view = ObjectProperty(None)	
    # programmer_view = ObjectProperty(None)
    # run_View = ObjectProperty(None)
    # debug_View = ObjectProperty(None)
    save_Buttton = ObjectProperty(None)
    load_Buttton = ObjectProperty(None)
    run_Buttton = ObjectProperty(None)
    debug_Buttton = ObjectProperty(None)
    exit_Buttton = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(FunctionalProgrammerWidget, self).__init__(**kwargs)
        self.current_view = ScreenManager()
        self.pv = ProgrammerView(name='pv')
        self.current_view.add_widget(self.pv)
        self.rv = RunScreen('user_file', name='rv')
        self.current_view.add_widget(self.rv)
        self.current_view.current = 'pv'
        self.add_widget(self.current_view)

        
          



    ''' saves user program to user defined location '''
    def save_Button(self):
            self.ids.save_Button.text = 'not yet implemented'
                    

    ''' loads a user program from a user defined location '''
    def load_Button(self):
        self.ids.load_Button.text = 'not yet implemented'
                    

    ''' displays maze and robot traversing through the maze '''
    def run_Button(self):
            if self.current_view.current == 'pv':
                program = open('user_file', 'r').read()
                if 'x' not in program:
                    self.ids.run_Button.text = program
                    self.current_view.current = 'rv'
                    self.rv.run_code()
                    self.ids.run_Button.text = 'BACK'
                    # run_robot = RobotController()
                    # run_robot.executeProgram('user_file')
            elif self.current_view.current == 'rv':
                self.current_view.current = 'pv'
                self.ids.run_Button.text = 'RUN'
                
            else:
                self.ids.run_Button.text = 'variables not defined'

    def reset_Button(self):
        self.ids.reset_button.text = 'not yet implemented'


    ''' displays maze and robot traversing through the maze alongside 
    the user program as it steps through the code'''
    def debug_Button(self):
            # current_view = debug_View
            self.ids.debug_Button.text = 'not yet implemented'

    


class FPWScreenManager(ScreenManager):
    pass



class FunctionalProgrammerApp(App):
    def build(self):

        return FunctionalProgrammerWidget()

if __name__ == '__main__':
    # import pdb; pdb.set_trace()
    FunctionalProgrammerApp().run()
