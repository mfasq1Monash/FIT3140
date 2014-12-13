from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class FunctionList(list):


	def __init__(self):
	    layout = BoxLayout(orientation = 'vertical')
	    layout = BoxLayout(spacing=10)
	   for element in self:
	   		layout.add_widget(element)