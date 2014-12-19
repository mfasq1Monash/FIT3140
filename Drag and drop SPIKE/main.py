from kivy.app import app
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class SwallowWidget(Widget):
    # contains two layouts with buttons to drag and drop
    african = ObjectProperty(None)
    for i in range(4):
        african.addwidget(Button(str(i)))

##    european = ObjectProperty(None)
##    for i in range(4,8):
##        european.addwidget(Button(str(i)))



class SwallowApp(App):
    build(self):
        return SwallowWidget()
