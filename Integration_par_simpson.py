def approsimpson(f,a,b,n):
    s=0
    s=s+((b-a)/6n)*sum((f(a+k*((b-a)/n))+4f(((a+k*((b-a)/n))+(a+(k+1)*((b-a)/n)))/2)+f((a+(k+1)*((b-a)/n)))) for k in range (n))
    print("L'intégrale de",a,"à",b,"de la fonction est environ égal à",s)