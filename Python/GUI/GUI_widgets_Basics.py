import ipywidgets as widgets

w=widgets.IntSlider()

from IPython.display import display
display(w)

display(w)
w.close()

w=widgets.IntSlider()
display(w)
w.value=50

w.max=2000

a=widgets.FloatText()
b=widgets.FloatSlider()
display(a,b)

mylink=widgets.jslink((a,'value'),(b,'value'))