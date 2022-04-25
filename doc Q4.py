n= [6,1,3,5,6,3,1]
a=[]
i=0
product=1
while i<len(n):
    j=n[i]
    if j not in a:
        a.append(j)
        product=product*a[i]
    i+=1
print(a)
print(product)







        


