#a="12456789"
a=int(input("enrte the num"))
a=str(a)
i=0
while i<len(a):
    j=len(a)-(i+1)
    b=int(a[i])*10**j
    print(b,"+",end="")
    i+=1

