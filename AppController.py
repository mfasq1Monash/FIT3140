from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty


class AppController(BoxLayout):
	
	student_Program = ObjectProperty(None)
	code_View = ObjectProperty(None)
	run_View = ObjectProperty(None)
	debug_View = ObjectProperty(None)
	current_view = ObjectProperty(None)
	import pdb; pdb.set_trace()


	def __init__(self):
		pass#current_View = code_View 
		# return self
	
	def save_Button(self, student_Program):
		self.text = 'not yet implemented'
			

	def load_Button(self):
		self.text = 'not yet implemented'
			

	def run_Button(self):
		# current_view = run_View
		self.text = 'not yet implemented'
			

	def debug_Button(self):
		# current_view = debug_View
		self.text = 'not yet implemented'
