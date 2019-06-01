import matplotlib.pyplot as pypl
import numpy as np
from math import pi
t=np.linspace(-pi,3*pi,1000)
y=np.cos(t)
pypl.plot(t,y)

ys=np.sin(t)
pypl.plot(t,ys)
pypl.legend(['cosinus','sinus'],loc='upper left')
pypl.show()
