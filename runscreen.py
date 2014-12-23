'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.12
# Last Modified: 2014.12.15

A display for a maze that is passed as a list of lists

'''

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from robotio import RobotIO


class RunView(Screen):
	
	def __init__(self, ):
		pass




class TestRunView(App):
	def build(self):
		return RunView()

if __name__ == '__main__':
	TestRunView().run()
