from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty


class AppController(BoxLayout):

	student_Program = ObjectProperty(None)
	code_View = ObjectProperty(None)
	run_View = ObjectProperty(None)
	debug_View = ObjectProperty(None)

	def __init__(self):
		return self
	
		def save_Button(student_Program):
			pass
			#raise(Not Implemented Error)

		def load_Button():
			pass
			# raise(Not Implemented Error)

		def run_Button():
			pass
			# raise(Not Implemented Error)

		def debug_Button():
			pass
			# raise(Not Implemented Error)