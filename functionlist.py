'''
Author:        Aaron Gruneklee, Michael Asquith
Created:       2014.12.09
Last Modified: 2014.12.14

List of code blocks to be displayed and manipulated through user interaction.

takes a list of strings and converts them into dragable objects.

***  still need to implement drag and drop and display of draggable code blocks  ***   

'''
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.listview import ListView
from kivy.properties import ObjectProperty

class FunctionList(BoxLayout):

	code_List = ObjectProperty(None)

	def __init__(self, theList):
		super(FunctionList, self).__init__
		layout = ListView(item_strings = theList)
		theCode = self.ids.code_List
		theCode.add_widget(layout)