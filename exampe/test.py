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
            ch1_min:-750
            ch1_max:750
            
        BoxLayout:
            orientation: 'vertical'
            size_hint: .1,1#
            ToggleButton
                on_state:graph.start_realtime() if self.state=="down" else graph.stop_realtime() 
            ToggleButton
                min:-7500
                max:7500
                on_press:graph.change_y_label(self.min,self.max,0,[1,0,1,1])
            ToggleButton
            ToggleButton
    Slider:
        size_hint:1,.1
        min:-750
        max:750
        value:0
        on_value:graph.ch1_value=self.value
                    


            




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