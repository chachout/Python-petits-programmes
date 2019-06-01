import matplotlib.pyplot as clairounette
import numpy as chachout
n=20
x=[k*10/n for k in range(n)]
y=[chachout.sin(k*10/n)for k in range(n)]
type(x),type(y)
clairounette.plot(x,y)
clairounette.ylabel('fonction sinus')
clairounette.xlabel("l'axe des abscisses")
clairounette.show()