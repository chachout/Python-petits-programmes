def dichotomie(f,c,d,i) :
    a=c
    b=d
    while ((b-a)>(2*i)) :
        s=(a+b)/2
        if f(a)*f(s) <= 0 :
            b=s
        else :
            a=s
    return((a+b)/2)