'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.12
# Last Modified: 2014.12.23

A display for a maze that is passed as a list of lists

'''

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from robotio import RobotIO


class RunScreen(Screen):
	
	def __init__(self, *kwargs):
		super(RunScreen, self).__init__(**kwargs)




class TestRunScreen(App):
	def build(self):
		return RunScreen()

if __name__ == '__main__':
	TestRunScreen().run()
