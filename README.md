# Graph
Real Time Graph for On Board Diagnostic



## Description
to visualize data in real time graphs

## Getting Started


### Installing
```
git clone https://github.com/sooko/graph.git
cd graph
python setup.py install
```
### Usage

### Code Example

```
from graph import Graph
from kivy.app import App

class MyGraph(Graph):
    pass


class MyApp(App):
    def build(self):
        return MyGraph()


if __name__=="__main__":
    MyApp().run()


```



## Authors

Contributors names and contact info

ex. Mochamad Burhanudin
