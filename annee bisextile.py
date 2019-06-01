annee=input("Choisissez une année : ")
if annee%100==0 and annee%400!=0 :
    print(annee,"n'est pas une année bisextile.")
else :
    print(annee,"est une année bisextile.")