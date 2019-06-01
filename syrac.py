def syrac(N) :   
    i=0
    while N!=1 :
        if N%2==0:
            N=N/2
            i=i+1
            print(N)
        else :
            N=3*N+1
            i=i+1
            print(N)
    return (i)