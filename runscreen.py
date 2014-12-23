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
from robotcontroller import RobotController


class RunScreen(Screen):
    """Screen which displays the maze and the robot."""
    
    def __init__(self, filename, **kwargs):
        super(RunScreen, self).__init__(**kwargs)
        self.run_robot = RobotController()
        self.maze = self.run_robot.getMaze()
        grid = GridLayout()

        # Should use maze methods, not take the maze's grid
        grid.cols = len(self.maze[0])
        grid.rows = len(self.maze)

        self.draw_maze(grid)
        
        self.add_widget(grid)

    def draw_maze(self, grid, prev=None):
        (x, y, _) = self.run_robot.getRobotLocationAndFacing()

        # Populate maze
        for r in range(grid.rows):
            for c in range(grid.cols):
                if c == x and r == y:
                    title = 'Robot.png'
                elif self.maze[r][c] == 1:
                    title = 'Wall.png'
                elif self.maze[r][c] == 0:
                    title = 'Path.png'
                elif self.maze[r][c] == 'S':
                    title = 'Start.png'
                elif self.maze[r][c] == 'G':
                    title = 'Goal.png'
                grid.add_widget(Image(source=title,
                                      allow_stretch=True,
                                      keep_ratio=False))

class TestRunScreen(App):
    def build(self):
        return RunScreen('user_file')

if __name__ == '__main__':
    TestRunScreen().run()
