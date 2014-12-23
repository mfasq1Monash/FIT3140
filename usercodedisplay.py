'''
Author:        Aaron Gruneklee, Michael Asquith
Created:       2014.12.16
Last Modified: 2014.12.16

tree of code blocks to be displayed and manipulated through user interaction.

this forms the display of the user code

***  still need to implement drag and drop and display of draggable code blocks  ***   

'''

from kivy.app import App
from kivy.uix.treeview import TreeView, TreeViewNode
from kivy.uix.gridlayout import GridLayout



class UserCodeDisplay(GridLayout):

	def __init__(self, userProgram):
		super(UserCodeDisplay, self).__init__()
		program = userProgram.replace('(', '( ').replace(')', ' )').split()		
		for 

	def on_textinput(self):
		self = PrimaryBlock(self.text)
		pass

	def on_touch_up(self, touch, *args):
		if self.collide_point(*touch.pos):
			pass
		pass
	def on_touch_down(self, touch, *args):
		pass	





class testUserCodeDisplay(App):

	

	def build(self):
		return UserCodeDisplay()


if __name__ == '__main__':
	testUserCodeDisplay().run()