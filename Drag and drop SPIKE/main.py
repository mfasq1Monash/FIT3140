from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class SwallowWidget(Widget):
    # contains two layouts with buttons to drag and drop
    african = ObjectProperty(None)
    for i in range(4):
    	# *** african is None you need to make it a uix (layout) subclass 
    	# to be able to add widgets *** 
        african.add_widget(Button(str(i)))

##    european = ObjectProperty(None)
##    for i in range(4,8):
##        european.addwidget(Button(str(i)))



class SwallowApp(App):
    def build(self):
        return SwallowWidget()
