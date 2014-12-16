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
from kivy.properties import ObjectProperty

class FunctionList(BoxLayout):

	code_List = ObjectProperty(None)

	def __init__(self, theList):
		super(FunctionList, self).__init__()
		# self.code_List = 
		for i in range(len(theList)):
			self.add_widget(Button(text=theList[i]))






class testFunctionList(App):
    def build(self):
    	
        return FunctionList(['+ 4 5', '- 3 5', 'define x TRUE', 'if x 5'])

if __name__ == '__main__':
    testFunctionList().run()

