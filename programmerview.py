'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.18
# Last Modified: 2014.12.18

this is the main controler class it is responsible for displaying the 3 views and
controls the 5 input buttons.

'''


from kivy.app import App
from kivy.properties import ListProperty, ObjectProperty
from functionlist import FunctionList
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label




class ProgrammerView(Screen):

	programmer_view = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(ProgrammerView, self).__init__(**kwargs)
		grid = GridLayout()
		grid.cols= 2
		precode = open('function_file', 'r+')
		commands = []
		for line in precode:
			commands.append(line)
		v2 = FunctionList([], grid, None)
		v2.destinationLayout = v2
		v1 = FunctionList(commands, grid, v2)
		
		grid.add_widget(v1)

		grid.add_widget(v2)

		grid.add_widget(Label(text= 'CODE BLOCKS', size_hint=(1,.05)))
		grid.add_widget(Label(text= 'USER PROGRAM', size_hint=(1,.05)))

		self.add_widget(grid)




class TestProgrammerView(App):
	def build(self):
		return ProgrammerView()

if __name__ == '__main__':
	TestProgrammerView().run()