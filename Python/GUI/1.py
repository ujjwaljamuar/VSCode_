from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

def func(x):
    return x**2

interact(func,x=10)

@interact(x=True,y=1.0)
def g(x,y):
    return (x,y)


interact(func,x=widgets.IntSlider(min=-100,max=100,step=1,value=0));

from IPython.display import display

def f(a,b):
    display(a+b)
    return a+b
w=interactive(f,a=10,b=20)

display(w)

# run this with jupyter notebook .