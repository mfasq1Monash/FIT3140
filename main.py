from kivy import require
from kivy.app import App
from kivy.uix.widget import Widget
from AppController import AppController
from kivy.uix.floatlayout import FloatLayout

#Kivy version check
require('1.8.0')


# class AppController(Widget):
#     # layout = FloatLayout()
#     # layout.add_widget(AppController)


class FunctionalProgrammerApp(App):
    def build(self):
        return AppController()

if __name__ == '__main__':
	FunctionalProgrammerApp().run()
