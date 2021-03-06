'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.18
# Last Modified: 2014.12.23

View which displays the user program on the right and usable function blocks on
the left.

'''


from kivy.app import App
from kivy.properties import ListProperty, ObjectProperty
from functionlist import FunctionList
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from usercodedisplay import UserCodeDisplay




class ProgrammerView(Screen):

	programmer_view = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(ProgrammerView, self).__init__(**kwargs)

		grid = GridLayout()
		grid.cols= 2
		precode = open('function_file', 'r+')
		commands = [line for line in precode]
		usercode = open('user_file', 'r+')
		
		v2 = UserCodeDisplay(usercode.read())
		
		v1 = FunctionList(commands)
		
		grid.add_widget(v1)

		grid.add_widget(v2)

		grid.add_widget(Label(text= 'CODE BLOCKS', size_hint=(1,.05)))
		grid.add_widget(Label(text= 'USER PROGRAM', size_hint=(1,.05)))

		self.add_widget(grid)

		def on_touch_down(self, touch, *args):
			super(ProgrammerView, self).on_touch_down(touch)
	

		def on_touch_move(self, touch):
			pass

		def on_touch_up(self, touch):
			pass

class TestProgrammerView(App):
	def build(self):
		return ProgrammerView()

if __name__ == '__main__':
	TestProgrammerView().run()
