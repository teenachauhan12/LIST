
a=[11000,1050]
i=0
b=[]
while i<len(a):
    while a[i]>0:
        if a[i]%10!=0:
            b.append(a[i])
            break    
        a[i]=a[i]//10    
    i=i+1
print(b)       
        