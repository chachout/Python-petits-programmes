from numpy import *
n=int (input ("lala : "))
poly=zeros(n+1)
for indice in range(0,n+1):
    s="lala"+str(indice)+' : '
    Val=input(s)
    poly[indice]=int(Val)
print (poly)
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
print("derivee" , polyPrime)