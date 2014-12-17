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
		



class treeViewTextInput(textInput, TreeViewNode):
	super(treeViewWidget, self).__init__()


	def on_textinput(self):
		





class testUserCodeDisplay(App):

	def test_tree_display(s):
		tree_code = '(/ (+, 3, y), 9) '
        display_tree(tree_code)

    def build(self):
    	return userCodeDisplay()


if__name__ == '__main__':
	testUserCodeDisplay().run()