'''
# Author:        Aaron Gruneklee, Michael Asquith
# Created:       2014.12.18
# Last Modified: 2014.12.18

this class is buttons that are used in the function list.

'''

from kivy.app import App
from kivy.uix.button import Button
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
from codeblock import PrimaryBlock



class PreCodeButton(Button):
	previous_x = NumericProperty(None)
	previous_y = NumericProperty(None)

	code_Blocks = ListProperty([])

	def __init__(self, text, dragLayout, destinationLayout):
		super(PreCodeButton, self).__init__(size_hint=(1,None))
		self.text = text
		parameters = text.replace('(', '( ').replace(')', ' )').split()
		self.MydragLayout = dragLayout
		self.destination_layout = destinationLayout
		for param in parameters:
			self.code_Blocks.append(PrimaryBlock(param))

	def on_touch_down(self, touch, *args):
		if self.collide_point(*touch.pos):
			touch.grab(self)
			
			(self.previous_x, self.previous_y) = self.pos
 			self.center = touch.pos
			return True
		return super(PreCodeButton, self).on_touch_down(touch, *args)

	def on_touch_move(self, touch, *args):
		if touch.grab_current == self:
			self.center = touch.pos

	def on_touch_up(self, touch, *args):
		if touch.grab_current == self:
			if self.destination_layout.collide_point(*touch.pos):
				for iblock in code_Blocks:
					self.destination_layout.add_widget(iblock)
			self.pos = (self.previous_x, self.previous_y)
			
			touch.ungrab(self)
		# need to add primaryblocks to user code window

class TestPreCodeButton(App):
	def build(self):
		return PreCodeButton('(add x y)')


if __name__ == "__main__":
	TestPreCodeButton().run()