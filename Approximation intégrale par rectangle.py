def approrectangle(f,x,y,z): 
#x première valeur, y dernière, z nombre de rectangle, e écart d'un rectangle
    e=(y-x)/z
    d=x
    i=0
    while d<y+e:
        l=e
        s=d-e
        h=f(s)
        i=i+l*h
        d=d+e
    print("L'intégrale de",x,"à",y,"de la fonction est environ égal à",i)