from graph import Graph
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.clock import Clock
Builder.load_string("""
<ML>:
    graph:graph
    BoxLayout:
        Button:
            size_hint: .1,1# None
            text: "text"
            color:
        Graph
            id:graph
        BoxLayout:
            orientation: 'vertical'
            size_hint: .1,1#
            ToggleButton
                on_state:graph.start_realtime() if self.state=="down" else graph.stop_realtime() 
            ToggleButton
                min:-7500
                max:7500
                on_press:graph.change_y_label(self.min,self.max,2)
            ToggleButton
            ToggleButton
            


            




""")

class ML(FloatLayout):
    def __init__(self, **kwargs):
        super(ML,self).__init__(**kwargs)  
    def on_size(self,a,b):
        if self.graph:
            self.graph.refresh()



class MyApp(App):
    def build(self):
        return ML()


if __name__=="__main__":
    MyApp().run()