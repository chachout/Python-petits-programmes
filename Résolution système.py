import numpy as np
systeme=np.array([[1,1],
                  [-0.316,--31]])
valeur=np.array([[0.2],
                 [0]])
sol=np.linalg.solve(systeme,valeur)
print("x=",sol[0,0]," et y=",sol[1,0])