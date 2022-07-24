import os
from setuptools import setup
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "graph",
    version = "0.0.1",
    author = "Mochamad Burhanudin",
    author_email = "hansmotor89@gmail.com",
    description = ("Simple Graph for kivy"),
    license = "BSD",
    keywords = "kivy graph",
    url = "https://github.com/sooko/graph.git",
    packages=['graph', ],
    long_description=read('README.md'),
    package_data={'': ['graph.kv']},
    include_package_data=True,
    install_requires=[],


)