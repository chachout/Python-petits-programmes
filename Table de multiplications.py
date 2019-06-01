for k in range(1,100):
    for x in range(1,100):
        tab=open("table de '\x'.txt","w")
        k=str(k)
        tab.writelines(["/nlignek",k,"fois",x,"égal à",k*x])
        tab.close()
        k=int(k)
        x=int(x)
        x=x+1
    k=k+1
    