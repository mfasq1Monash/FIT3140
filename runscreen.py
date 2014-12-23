'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.12
# Last Modified: 2014.12.23

A display for a maze that is passed as a list of lists

'''

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from robotcontroller import RobotController


class RunScreen(Screen):
    """Screen which displays the maze and the robot."""
    
    def __init__(self, filename, **kwargs):
        super(RunScreen, self).__init__(**kwargs)
        self.file = filename
        self.run_robot = RobotController()
        self.maze = self.run_robot.getMaze()
        grid = GridLayout()

        # Should use maze methods, not take the maze's grid
        grid.cols = len(self.maze[0])
        grid.rows = len(self.maze)

        self.draw_maze(grid)
        self.add_widget(grid)

        (x, y, _) = self.run_robot.getRobotLocationAndFacing()
        self.oldRobotLocale = (x, y)
        

    def draw_maze(self, grid):            
            
        (x, y, _) = self.run_robot.getRobotLocationAndFacing()

        # Populate maze
        self.imageGrid = []
        for r in range(grid.rows):
            imageRow = []
            for c in range(grid.cols):
                if c == x and r == y:
                    title = 'Robot.png'
                else:
                    title = self.imageName(self.maze[r][c])
                newImage = Image(source=title,
                                 allow_stretch=True,
                                 keep_ratio=False)
                imageRow.append(newImage)
                grid.add_widget(newImage)
            self.imageGrid.append(imageRow)

    def update_maze(self):
        (oldx, oldy) = self.oldRobotLocale
        self.imageGrid[oldy][oldx].source = self.imageName(self.maze[oldy][oldx])
        (newx, newy, _) = self.run_robot.getRobotLocationAndFacing()
        self.imageGrid[newy][newx].source = 'Robot.png'
        self.oldRobotLocale = (newx, newy)

    def imageName(self,symbol):
        if symbol == 1:
            return 'Wall.png'
        if symbol == 0:
            return 'Path.png'
        if symbol == 'S':
            return 'Start.png'
        if symbol == 'G':
            return 'Goal.png'

    def run_code(self):
        Clock.schedule_interval(lambda dt:screen.update_maze(), .5)
        self.run_robot.executeProgram(self.file)

class TestRunScreen(App):
    def build(self):
        screen = RunScreen('user_file')
        Clock.schedule_once(lambda dt:screen.run_code())
        return screen

if __name__ == '__main__':
    TestRunScreen().run()
