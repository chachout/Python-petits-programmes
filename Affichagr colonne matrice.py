def affichagecolonne(A,n) :
    n=n-1
    if len(A[0])<=n:
        print ("erreur il n'y a pas",n+1,"colonnes")
    else :
        y=0
        while y<len(A):
            print(A[y][n])
            y=y+1