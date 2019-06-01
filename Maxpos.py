def maxpos(l):
    for i in range(0,len(l)-1):
        if l[i]==max(l):
            print (i+1, max(l))
        else :
            i=i+1
        
        