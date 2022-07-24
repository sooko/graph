from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('graphics', 'width', '1050')
Config.set('graphics', 'height', '550')
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty,StringProperty,ListProperty
from kivy.graphics import Line,Color
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.uix.label import Label
import datetime
from kivy.resources import resource_add_path
from kivy.lang import Builder
import os.path
from kivy.uix.widget import Widget
from kivy.uix.button import Button
resource_add_path(os.path.dirname(__file__))
Builder.load_file("graph.kv")

class GridX(Widget):
    # pass
    color=ListProperty([1,1,1,1])
class GridY(Widget):
    # pass
    color=ListProperty([1,1,1,1])

class LabelX(Label):
    pass
class LabelY(Label):
    pass

class Graph(FloatLayout):
    min_y_label=StringProperty("0")
    min_x_label=StringProperty("0")
    marker_x_color=ListProperty([1,1,1,.5])
    grid_color=ListProperty([1,1,1,.5])
    major_x=NumericProperty(1)
    major_y=NumericProperty(1)
    ch1_color   =ListProperty([1,0,0,1])
    ch1_points  =ListProperty([])
    ch1_value   =NumericProperty(50)
    ch1_max     =NumericProperty(100)
    ch1_min     =NumericProperty(0)
    
    ch2_color   =ListProperty([0,1,0,1])
    ch2_points  =ListProperty([])
    ch2_value   =NumericProperty(0)
    ch2_max     =NumericProperty(10)
    ch2_min     =NumericProperty(0)

    ch3_color   =ListProperty([0,0,1,1])
    ch3_points  =ListProperty([])
    ch3_value   =NumericProperty(0)
    ch3_max     =NumericProperty(10)
    ch3_min     =NumericProperty(0)

    ch4_color   =ListProperty([1,0,1,1])
    ch4_points  =ListProperty([])
    ch4_value   =NumericProperty(0)
    ch4_max     =NumericProperty(10)
    ch4_min     =NumericProperty(0)

    ch5_color   =ListProperty([1,1,0,1])
    ch5_points  =ListProperty([])
    ch5_value   =NumericProperty(0)
    ch5_max     =NumericProperty(10)
    ch5_min     =NumericProperty(0)

    ch6_color   =ListProperty([0,1,1,1])
    ch6_points  =ListProperty([])
    ch6_value   =NumericProperty(0)
    ch6_max     =NumericProperty(10)
    ch6_min     =NumericProperty(0)

    ch7_color   =ListProperty([1,.5,0,1])
    ch7_points  =ListProperty([])
    ch7_value   =NumericProperty(0)
    ch7_max     =NumericProperty(10)
    ch7_min     =NumericProperty(0)

    ch8_color   =ListProperty([0,.5,1,1])
    ch8_points  =ListProperty([])
    ch8_value   =NumericProperty(0)
    ch8_max     =NumericProperty(10)
    ch8_min     =NumericProperty(0)

    count=NumericProperty(0)
    div=NumericProperty(1000)
    date=StringProperty("")
    translate_x=NumericProperty(0)
    runing_x_points=ListProperty([])
    
    def __init__(self, **kwargs):
        super(Graph,self).__init__(**kwargs)
        self.major_x=10
        self.major_y=10
        self.ch1_point=[]
        self.ch2_point=[]
        self.ch3_point=[]
        self.ch4_point=[]
        self.ch5_point=[]
        self.ch6_point=[]
        self.ch7_point=[]
        self.ch8_point=[]
    

    

    def on_major_y(self,a,b):
        Clock.unschedule(self.create_major_y,.5)
        Clock.schedule_once(self.create_major_y,.5)
        
    def on_major_x(self,a,b):
        Clock.unschedule(self.create_major_x,.5)
        Clock.schedule_once(self.create_major_x,.5)
    
    def create_major_x(self,dt):
        self.root_x_label.clear_widgets()
        self.root_grid_x.clear_widgets()
        for i in range(self.major_x):
            self.root_x_label.add_widget(LabelX(font_size=self.root_x_label.height*.5,text=str(1+i)))
            self.root_grid_x.add_widget(GridX(color=self.grid_color))
            
            

            
           


    def create_major_y(self,dt):
        self.root_y_label.clear_widgets()
        self.root_grid_y.clear_widgets()
        for i in range(self.major_y):
            self.root_y_label.add_widget(LabelY(font_size=self.root_x_label.height*.5,text=str(self.major_y-i)))
            self.root_grid_y.add_widget(GridY(color=self.grid_color))
            
            


    def do_realtime_plot(self,dt):
        plot_size   =self.plot_area_line.size
        plot_pos    =self.plot_area_line.pos   
        stroke      = plot_pos[0]+ (plot_size[0] *self.count/self.div*10)
        self.runing_x_points=[stroke,plot_pos[1],stroke,plot_pos[1]+plot_size[1]]
        ch1_y      =  plot_pos[1]+ plot_size[1] *self.ch1_value/(self.ch1_max-self.ch1_min)
        ch2_y      =  plot_pos[1]+ plot_size[1] *self.ch2_value/(self.ch2_max-self.ch2_min)
        ch3_y      =  plot_pos[1]+ plot_size[1] *self.ch3_value/(self.ch3_max-self.ch3_min)
        ch4_y      =  plot_pos[1]+ plot_size[1] *self.ch4_value/(self.ch4_max-self.ch4_min)
        ch5_y      =  plot_pos[1]+ plot_size[1] *self.ch5_value/(self.ch5_max-self.ch5_min)
        ch6_y      =  plot_pos[1]+ plot_size[1] *self.ch6_value/(self.ch6_max-self.ch6_min)
        ch7_y      =  plot_pos[1]+ plot_size[1] *self.ch7_value/(self.ch7_max-self.ch7_min)
        ch8_y      =  plot_pos[1]+ plot_size[1] *self.ch8_value/(self.ch8_max-self.ch8_min)
        
        
        if stroke-plot_pos[0]>plot_size[0]:
            self.translate_x-= plot_size[0]*1/self.div*10
            self.ch1_point.remove(self.ch1_point[0])
            self.ch2_point.remove(self.ch2_point[0])
            self.ch3_point.remove(self.ch3_point[0])
            self.ch4_point.remove(self.ch4_point[0])
            self.ch5_point.remove(self.ch5_point[0])
            self.ch6_point.remove(self.ch6_point[0])
            self.ch7_point.remove(self.ch7_point[0])
            self.ch8_point.remove(self.ch8_point[0])


        self.ch1_point.append([stroke,ch1_y])
        self.ch2_point.append([stroke,ch2_y])
        self.ch3_point.append([stroke,ch3_y])
        self.ch4_point.append([stroke,ch4_y])
        self.ch5_point.append([stroke,ch5_y])
        self.ch6_point.append([stroke,ch6_y])
        self.ch7_point.append([stroke,ch7_y])
        self.ch8_point.append([stroke,ch8_y])
        
        

        self.ch1_points=self.ch1_point
        self.ch2_points=self.ch2_point
        self.ch3_points=self.ch3_point
        self.ch4_points=self.ch4_point
        self.ch5_points=self.ch5_point
        self.ch6_points=self.ch6_point
        self.ch7_points=self.ch7_point
        self.ch8_points=self.ch8_point
        
        self.count +=1



    def refresh(self):
        # pass
        # Clock.unschedule(self.create_major_y,.5)
        # Clock.schedule_once(self.create_major_y,.5)
        # Clock.unschedule(self.create_major_x,.5)
        # Clock.schedule_once(self.create_major_x,.5)
        self.reset_plot()

    def reset_plot(self):
 
        self.ch1_point.clear()#append([stroke,ch1_y])
        self.ch2_point.clear()#append([stroke,ch2_y])
        self.ch3_point.clear()#append([stroke,ch3_y])
        self.ch4_point.clear()#append([stroke,ch4_y])
        self.ch5_point.clear()#append([stroke,ch5_y])
        self.ch6_point.clear()#append([stroke,ch6_y])
        self.ch7_point.clear()#append([stroke,ch7_y])
        self.ch8_point.clear()#append([stroke,ch8_y])
        
        self.ch1_points=self.ch1_point
        self.ch2_points=self.ch2_point
        self.ch3_points=self.ch3_point
        self.ch4_points=self.ch4_point
        self.ch5_points=self.ch5_point
        self.ch6_points=self.ch6_point
        self.ch7_points=self.ch7_point
        self.ch8_points=self.ch8_point


        
        self.count=0
        self.translate_x=0


        

    def start_realtime(self):
        self.stop_realtime()
        self.reset_plot()
        Clock.unschedule(self.do_realtime_plot)
        Clock.schedule_interval(self.do_realtime_plot,.1)
    def stop_realtime(self):
        Clock.unschedule(self.do_realtime_plot,.1)
    
    def change_y_label(self,min,max,decimal):
        self.min_y_label=str(min)
        self.root_y_label.clear_widgets()
        for i in range(self.major_y):
            if decimal!=0:
                lbl=str(round(max - i*(max-min)/self.major_y,decimal))
            else:
                lbl=str(round(max - i*(max-min)/self.major_y))
            self.root_y_label.add_widget(LabelY(font_size=self.root_x_label.height*.5,text=lbl))




