b=int(input("Est ce que la température de départ est en fahrenheit [mettre 1] ou en celsius [mettre 0] ou en Kelvin [mettre 2] : " ))
if b==1 :
    f=float(input("température en °F : "))
    c=(f-32)/1.8
    print (f,"°F=",c,"°C")
elif b==2 :
    k=float(input("température en °K : "))
    c=k-273.15
    f=c*1.8+32
    print (k,"°K",c,"°C",f,"°F")
else :
    c=float(input("température en °C : "))
    f=c*1.8+32
    print (c,"°C",f,"°F")
