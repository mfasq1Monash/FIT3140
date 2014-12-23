'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.12
# Last Modified: 2014.12.23

A display for a maze that is passed as a list of lists

'''

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from robotcontroller import RobotController


class RunScreen(Screen):
    
    def __init__(self, filename, **kwargs):
        super(RunScreen, self).__init__(**kwargs)
        self.run_robot = RobotController()
        self.maze = self.run_robot.getMaze()
        grid = GridLayout()
        grid.cols = len(self.maze[0])
        grid.rows = len(self.maze)
        for r in self.maze:
            for c in self.maze:
                grid.add_widget(Button())
        self.add_widget(grid)

        
        

    def setRobotController(self, newRobotController):
        self.robotController = newRobotController


class TestRunScreen(App):
    def build(self):
        return RunScreen('user_file')

if __name__ == '__main__':
    TestRunScreen().run()
