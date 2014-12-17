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


class userCodeDisplay(GridLayout):

	def __init__(self):
		super(userCodeDisplay, self).__init__()

	def on_textinput(self):
		pass

	def on_touch_up(self, touch, *args):
		pass

	def on_touch_down(self, touch, *args):
		pass	





class testUserCodeDisplay(App):

	def test_tree_display(s):
		tree_code = '(/ (+, 3, y), 9) '
        display_tree(tree_code)

    def build(self):
    	return userCodeDisplay()


if__name__ == '__main__':
	testUserCodeDisplay().run()