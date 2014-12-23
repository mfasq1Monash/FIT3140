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
from codeblock import PrimaryBlock, CodeBlock
from kivy.uix.relativelayout import RelativeLayout


class UserCodeDisplay(RelativeLayout):

	def __init__(self, userProgram):
		super(UserCodeDisplay, self).__init__()
		layout = GridLayout(cols=6)


		program_file = userProgram.replace('(', '( ').replace(')', ' )').split()
		program = program_file		
		for element in program:
			layout.add_widget(PrimaryBlock(element))
		
		self.add_widget(layout)




	def on_textinput(self):
		return True

	# def on_touch_up(self, touch, *args):
	# 	if self.collide_point(*touch.pos):
	# 		pass
	# 	pass
	def on_touch_down(self, touch, *args):
		super(UserCodeDisplay, self).on_touch_down(touch)
		pass	

	def valid_syntax(self):
		if 'x' not in program:
			return True
		return False




class testUserCodeDisplay(App):

	

	def build(self):
		return UserCodeDisplay('(test x y')


if __name__ == '__main__':
	testUserCodeDisplay().run()