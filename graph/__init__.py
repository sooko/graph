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
resource_add_path(os.path.dirname(__file__))
Builder.load_file("graph.kv")

class LabelX(Label):
    pass
class LabelY(Label):
    pass

class Graph(FloatLayout):

    marker_x_color=ListProperty([1,1,1,.5])
    major_x=NumericProperty(1)
    major_y=NumericProperty(1)
    

    ch1_color   =ListProperty([1,0,0,1])
    ch1_points  =ListProperty([0,0])
    ch1_value   =NumericProperty(0)
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


    def start_realtime(self):
        Clock.unschedule(self.do_realtime_plot,.1)
        Clock.schedule_interval(self.do_realtime_plot,.1)
    def stop_realtime(self):
        Clock.unschedule(self.do_realtime_plot,.1)
    
    def reset(self):
        pass
    def on_major_y(self,a,b):
        Clock.unschedule(self.create_major_y,.5)
        Clock.schedule_once(self.create_major_y,.5)
        
    def on_major_x(self,a,b):
        Clock.unschedule(self.create_major_x,.5)
        Clock.schedule_once(self.create_major_x,.5)
    
    def create_major_x(self,dt):
        self.root_x_label.clear_widgets()
        size  =self.plot_area.size
        pos   =self.plot_area.pos
        for i in range(self.major_x):
            scale=size[0] * i / self.major_x
            self.root_x_label.add_widget(LabelX(font_size=self.root_x_label.height*.5,text=str(1+i)))
            with self.plot_area.canvas:
                Color(rgba=self.marker_x_color)
                Line(points=[pos[0]+scale,pos[1] , pos[0]+scale,pos[1]+size[1] ])


    def create_major_y(self,dt):
        self.root_y_label.clear_widgets()
        size  =self.plot_area.size
        pos   =self.plot_area.pos
        for i in range(self.major_y):
            scale= (size[1] * i/self.major_y) + (size[1] /self.major_y)
            self.root_y_label.add_widget(LabelY(font_size=self.root_x_label.height*.5,text=str(self.major_y-i)))
            with self.plot_area.canvas:
                Color(rgba=self.marker_x_color)
                Line(points=[pos[0],pos[1]+scale , pos[0] + size[0] ,pos[1]+scale ])


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


        x = datetime.datetime.now()
        self.date=x.strftime("%c")
    
    def on_size(self,a,b):
        self.reset_all()
    def reset_all(self):
        pass
           
    
    
    