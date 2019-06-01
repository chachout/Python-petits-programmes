def approriemann(f,a,b,n):
    s=0
    s=s+((b-a)/n)*sum(f(a+k*((b-a)/n)) for k in range (n))
    print("L'intégrale de",a,"à",b,"de la fonction est environ égal à",s)