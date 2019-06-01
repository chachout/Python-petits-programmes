def approritrap(f,a,b,n):
    s=((b-a)/(2*n))*sum((f(a+k*((b-a)/n)+f(a+(k+1)*((b-a)/n))) for k in range (n))
    print("L'intégrale de",a,"à",b,"de la fonction est environ égal à",s)