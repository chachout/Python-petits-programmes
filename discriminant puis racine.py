import numpy as np
def discriminant(a,b,c):
    d=b**2-4*a*c
    return d
a=float(input("Rentrer le coefficient de degré 2 : "))
b=float(input("Rentrer le coefficient de degré 1 : "))
c=float(input("Rentrer le coefficient de degré 0 : "))
d=discriminant(a,b,c)
if d==0 :
    print("L'équation a pour discriminant 0 et admet donc une racine double",-b/(2*a))
elif d>0 :
    print("L'équation a pour discriminant", d, "et admet donc admet deux racines simples",(-b-np.sqrt(d))/(2*a),(-b+np.sqrt(d))/(2*a))
else:
    print("L'équation a pour discriminant", d, "et admet donc n'admet pas de racines réels")
