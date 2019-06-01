from numpy import *
tab=zeros[[6],[6],[6],[6],[6],[6],[6]]
for i in range(0,7):
    for j in range(0,6):
        if tab[i][j]==tab[i][j+1]==tab[i][j+2]==tab[i][j+3]:
            print ("la partie est terminé")
        else :
            print ("continuer")
        j=j+1
    i=i+1
for j in range(0,6):
    for i in range(0,7):
        if tab[i][j]==tab[i+1][j]==tab[i+2][j]==tab[i+3][j]:
            print ("la partie est terminé")
        else :
            print ("continuer")
        j=j+1
    i=i+1
for i in range(0,7):
    for j in range(0,6):
        if tab[i][j]==tab[i+1][j+1]==tab[i+2][j+2]==tab[i+3][j+3]:
            print ("la partie est terminé")
        else :
            print ("continuer")
        j=j+1
    i=i+1
