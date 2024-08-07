def tow(n,source,dest,aux):
    if n==1:
        print("Move disk one from ",source,"to destination",dest)
        return
    tow(n-1,source,aux,dest)
    print("move disk",n,"from",source,"to destination",dest)
    tow(n-1,aux,dest,source)
    

n=int(input("enter n disk"))
tow(n,'A','b','c')    
