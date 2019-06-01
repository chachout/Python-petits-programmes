import matplotlib.pyplot as love
import numpy as lol
x=lol.linspace(-5,5,100)
love.plot(x,lol.sin(x),marker='o',linestyle='--',label="Sinus")
love.plot(x,lol.cos(x),marker='v',label="Cosinus")
love.title("Fonctions trigonométriques")
love.axis([0,4,0.4,1.4])
love.grid(True)
love.legend()
love.show()