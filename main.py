from kivy import require
from kivy.app import App
from kivy.uix.widget import Widget


#Kivy version check
require('1.8.0')


class AppController(Widget):
    pass


class FunctionalProgrammerApp(App):
    def build(self):
        return AppController()

if __name__ == '__main__':
    FunctionalProgrammerApp().run()
