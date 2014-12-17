'''
Author:        Aaron Gruneklee, Michael Asquith
Created:       2014.12.09
Last Modified: 2014.12.14

List of code blocks to be displayed and manipulated through user interaction.

takes a list of strings and converts them into dragable objects.

***  still need to implement drag and drop and display of draggable code blocks  ***   

'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.listview import ListView
from kivy.properties import ObjectProperty, ListProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from precodebutton import PreCodeButton

class FunctionList(ScrollView):

	code_List = ListProperty(None)

	def __init__(self, theList):
		super(FunctionList, self).__init__()
		self.size_hint = (1, 1)
		self.scroll_type = ['content', 'bars']
		self.bar_width='9dp'
		code_window = GridLayout(cols=1, size_hint=(1, None))
		code_window.bind(minimum_height=code_window.setter('height'),)

		for i in range(len(theList)):
			code_window.add_widget(PreCodeButton(theList[i]))

		self.add_widget(code_window)

	''' insert an instruction into the scrollable list '''
	def insertInstruction(self, name):
		self.code_window.add_widget(PreCodeButton(name, size_hint=(1,None),height=40))

	''' remove an instruction from the scrollable list '''
	def removeInstruction(self, name):
		error('not yet implemented')

	


class testFunctionList(App):
    def build(self):
    	
        return FunctionList(['+ 4 5', '- 3 5', 'define x TRUE', 'if x 5'])

if __name__ == '__main__':
    testFunctionList().run()

