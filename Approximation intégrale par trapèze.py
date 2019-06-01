def approtrapèze(f,x,y,z): 
#x première valeur, y dernière, z nombre de rectangle, e écart d'un rectangle
    e=(y-x)/z
    d=x #d est le point de départ de chaque intervalle
    i=0
    while d<y+e:
        h=e
        s=d-e
        t=d
        b=f(s)
        B=f(t)
        i=i+((h*(B+b))/2)
        d=d+e
    print("L'intégrale de",x,"à",y,"de la fonction est environ égal à",i)