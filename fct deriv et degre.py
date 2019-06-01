from numpy import *
def derive(poly) :
    n=len(poly)-1
    if(n==0):
        degrePolyPrime =0
    else :
        degrePolyPrime =n-1
    polyPrime=zeros(degrePolyPrime+1)
    if (n==0) :
        polyPrime[0]=0
    else:
        for indice in range(0,n):
            polyPrime[indice]=(indice+1)*poly[indice+1]
    return(polyPrime)

def derivedeg(poly,deg) :
    for i in range(0,deg):    
        poly=derive(poly)
        
    return(poly)